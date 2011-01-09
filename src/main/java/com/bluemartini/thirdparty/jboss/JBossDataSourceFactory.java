package com.bluemartini.thirdparty.jboss;

import java.util.*;
import javax.naming.InitialContext;
import java.sql.*;
import com.bluemartini.database.*;
import com.bluemartini.dna.*;
import com.bluemartini.server.BMAppServer;
import com.bluemartini.server.BMApplication;

/**
 * JBoss Datasource factory
 * This factory is generic and could used by any Java EE application servers.
 * Retrieve the JDNI name from <website>.appconfig.dna > pool > jndiName
 * 
 * @author yannick.robin
 */

public class JBossDataSourceFactory extends BMDataSourceFactory {
    private HashMap hSources_ = new HashMap();
    private Properties props_; // save for diagnostics

    public synchronized boolean supportsDataSource(BMDatabase bmDB, DNAList dnaPool) throws BMException {
        String sName = bmDB.getDBName();
        javax.sql.DataSource ds = (javax.sql.DataSource)hSources_.get(sName);
        if (ds != null) return true;

        // Data source only available if a class name is set.

        String dataSourceName = bmDB.getDBDataSourceName();
        return ((dataSourceName != null) && (dataSourceName.length() > 0));
    }
    
    public String getJNDIName(BMDatabase bmDB, DNAList dnaPool)
    {
        String jndiName = dnaPool.getString("jndiName");
        if(jndiName == null)
        {			
			BMApplication application = BMApplication.getApplication();
	        String appName = application.getName();
        	jndiName = "jdbc/" + appName + "." + bmDB.getDBName();
        }
        return jndiName;
    }
    
    public synchronized javax.sql.DataSource getDataSource(BMDatabase bmDB, DNAList dnaPool) throws BMException
    {	
    	javax.sql.DataSource dataSource = null;
    	InitialContext ctx = null;
    	String jndiDBAlias = null;
		try {
			
			BMAppServer appserver = BMAppServer.getAppServer();
			Hashtable htEnv = appserver.getInitialContextEnvironment(null);			
			ctx = new InitialContext(htEnv);
	        
			jndiDBAlias = "java:" + getJNDIName(bmDB, dnaPool);
			
			dataSource = (javax.sql.DataSource)ctx.lookup(jndiDBAlias); 
				
			if (dnaPool.getBoolean("initMinimum", true)) {
                int initCap = dnaPool.getAsInteger("initialCapacity", 0);
                Connection[] conn = new Connection[initCap];
                for (int i = 0; i < initCap; i++) {
                    conn[i] = dataSource.getConnection();
                }
                for (int i = 0; i < initCap; i++) {
                	BMLog.log(BMLog.COMPONENT_SYSTEM, 2, "Closing init connection[" + i + "] " + conn[i]);
                    conn[i].close();
                }
            }
			
		} catch (Exception e) {
			BMLog.log(BMLog.COMPONENT_SYSTEM, 0, "Failed to find DataSource : " + jndiDBAlias);
            DNAList params = new DNAList();
            params.setString("jndiDBAlias", jndiDBAlias);
            params.merge(bmDB.getExceptionParams());
            throw new BMException("DATA_SOURCE_FACTORY_FAILURE", e, params);
		}
		
    	return dataSource;
    }
    
    public Properties getProperties() {
        return props_;
    }

    /**
     * Get the underlying vendor connection object.
     */
    public Connection getVendorConnection(Connection conn) {
        return super.getVendorConnection(conn);
    }
}


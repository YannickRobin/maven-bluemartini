package com.bluemartini.thirdparty.weblogic;

import java.lang.String;

import com.array.core.Intv;
import com.bluemartini.core.*;
import com.bluemartini.database.*;
import com.bluemartini.dna.*;
import com.bluemartini.server.*;
import java.util.*;
import java.io.File;
import java.sql.SQLException;
import java.sql.Connection;
import javax.naming.*;
import javax.sql.*;

/**
 * Fix to configure JNDI in *.appconfig.dna
 * @author Yannick Robin
*/

public aspect WebLogicDataSourceFactoryAspect {	

    private static final String JNDI_PREFIX = "com.bluemartini.dbpool";
	
	DataSource around(BMDatabase bmDB, DNAList dnaPool) throws BMException
	: execution(public DataSource WebLogicDataSourceFactory.getDataSource(BMDatabase, DNAList)) && args(bmDB, dnaPool)
	{
    	DataSource ds;
    	
    	String jndiName = dnaPool.getString("jndiName");
    	if (jndiName == null)
    	{
    		String poolName = dnaPool.getString("name");
        	if (poolName == null)
        		poolName = bmDB.getDBName();
        	poolName = getApplicationPoolName(poolName);
    		jndiName = JNDI_PREFIX + "." + poolName;
    	}
        BMAppServer appServer = BMAppServer.getAppServer();
        Hashtable htEnv = appServer.getInitialContextEnvironment(null);
        try {
            InitialContext ctxt = new InitialContext(htEnv);
            ds = (DataSource) ctxt.lookup(jndiName);
        } catch (Exception e) {
    		throw new BMException("POOL_JNDI_LOOKUP_FAILED", e, bmDB.getExceptionParams());
        }
        return ds;
	}
	
    private static String getApplicationPoolName(String poolName) {
        BMApplication application = BMApplication.getApplication();
        String appName = application.getName();
        if (appName != null) {
            poolName = appName + "." + poolName;
        }

        return poolName;
    }	
			
} 

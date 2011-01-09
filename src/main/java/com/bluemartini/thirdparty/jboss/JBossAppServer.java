package com.bluemartini.thirdparty.jboss;

import java.util.Hashtable;

import javax.naming.Context;

import com.bluemartini.core.JNDIUtil;
import com.bluemartini.dna.BMException;
import com.bluemartini.server.BMAppServer;
import com.bluemartini.server.BMServerException;

/**
 * JBoss App Server class
 * This factory is generic and could used by any Java EE application servers.
 * 
 * @author yannick.robin
 */

public class JBossAppServer extends BMAppServer {
	public static final int TYPE_JBOSS = 4;
    private static final String INITIAL_CONTEXT_FACTORY_NAME = "org.jnp.interfaces.NamingContextFactory";
    private static final String WEB_APPLICATION_CLASS_NAME = "com.bluemartini.thirdparty.jboss.JBossWebApplication";

    public JBossAppServer() throws BMServerException {
    }

    /**
    ** Overrides BMAppServer method
    */
    public int getType() {
        return TYPE_JBOSS;
    }

    public String getWebApplicationClassName() {
        return WEB_APPLICATION_CLASS_NAME;
    }
    
	@Override
	public void exitOnFailure() throws BMServerException {
		return;
	}
	
	  /**
	   ** Get the protocol used to access a JNDI tree hosted by the app server.
	   **
	   ** @return  a protocol that can be used in a URL when accessing the JNDI tree
	   */
	  public String getJNDIProtocol() {
	    return "jnp";
	  }	
	
	  /**
	   * Get a URL to access the JNDI tree on the given host and port.  Both
	   * the host and port are optional.
	   *
	   * @param  host  host used to access the JNDI tree
	   * @param  port  port used to access the JNDI tree
	   *
	   * @return  a URL that can be used to access the JNDI tree, or <tt>null</tt> if no host is given
	   */
	  public String getJNDIURL(String host, Integer port) {
	    String jndiURL = null;

	    if (host != null) {
	      StringBuffer buffer = new StringBuffer();
	      buffer.append(getJNDIProtocol());
	      buffer.append("://");
	      buffer.append(host);
	      buffer.append(":");
	      if (port != null) {
	        buffer.append(port);
	      } else {
	        buffer.append(getDefaultListenPort());
	      }

	      jndiURL = buffer.toString();
	      
	    }

	    return jndiURL;
	  }
	  
	    public String getInitialContextFactoryName() {
	        return INITIAL_CONTEXT_FACTORY_NAME;
	    }
	  
	    public Hashtable<String, Object> getInitialContextEnvironment(String url){
	        return getInitialContextEnvironment(url, ctxSecPrn_, ctxSecCrd_);
	    }
	    public Hashtable<String, Object> getInitialContextEnvironment(String url, String timestamp1, String timestamp2) {
	        java.util.Hashtable<String, Object> jndiProps = new java.util.Hashtable<String, Object>();
	        jndiProps.put(Context.INITIAL_CONTEXT_FACTORY, getInitialContextFactoryName());
	        jndiProps.put(Context.URL_PKG_PREFIXES,"org.jboss.naming:org.jnp.interfaces");
	        if (url != null) {
	        	jndiProps.put(Context.PROVIDER_URL, url);          
	        }
	        if (timestamp1 != null) {
	        	jndiProps.put(Context.SECURITY_PRINCIPAL, timestamp1);
	        }
	        if (timestamp2 != null) {
	        	jndiProps.put(Context.SECURITY_CREDENTIALS, timestamp2);
	        }
	        return jndiProps;
	    }
	  

	    /**
	     * Get a JNDIUtil instance for the given JNDI URL.
	     *
	     * @param  url  url used to access the JNDI tree
	     *
	     * @return  a JNDIUtil that can be used to access the JNDI tree. If url is <b>null</b>, the JNDIUtil returned will
	     * contain an InitialContext that is created using the default environment variables.
	     *
	     * @see javax.naming.InitialContext
	     * @see WebSphereJNDIUtil
	     */
	    public JNDIUtil getJNDIUtil(String url) throws BMException {
	        JNDIUtil jndiUtil = null;
	        try {
	            if( url != null ) {
	                Hashtable<String, Object> jndiEnv = getInitialContextEnvironment(url);
	                jndiUtil = new JBossJNDIUtil(jndiEnv);
	            }
	            else {
	                jndiUtil = new JBossJNDIUtil();
	            }
	        }
	        catch (Exception e) {
	            throw new BMException("JNDI_INITIALIZATION_FAILED", e, null);
	        }
	        return(jndiUtil);
	    }
	    
}

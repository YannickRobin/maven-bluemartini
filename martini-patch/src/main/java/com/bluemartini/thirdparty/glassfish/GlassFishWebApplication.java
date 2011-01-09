package com.bluemartini.thirdparty.glassfish;

import com.bluemartini.dna.BMException;
import com.bluemartini.server.BMWebApplication;
import javax.servlet.ServletContext;

/**
 * Represents a web application within a GlassFish server.
 * 
 * @author yannick.robin
 */

public class GlassFishWebApplication extends BMWebApplication {

    /**
     * Create a web application.
     *
     * @param  servletContext  servlet context
     *
     * @exception  com.bluemartini.dna.BMException  if a fatal error occurs
     */
    public GlassFishWebApplication(ServletContext servletContext) throws BMException {

        super(servletContext);
        initWebApplication(servletContext);
    }

    /**
     * Initialize information according to the <tt>web.xml</tt> file.
     *
     * @param  servletContext  servlet context
     *
     * @internal
     */
    private void initWebApplication(ServletContext servletContext) throws BMException {

        // Application server information can only be loaded when
        // a context is available.

        if (servletContext == null) {
            return;
        }    
        
    }
}

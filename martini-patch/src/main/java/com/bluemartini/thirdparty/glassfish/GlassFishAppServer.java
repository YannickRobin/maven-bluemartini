package com.bluemartini.thirdparty.glassfish;

import com.bluemartini.server.BMAppServer;
import com.bluemartini.server.BMServerException;

/**
 * GlassFish App Server class
 * This factory is generic and could used by any Java EE application servers.
 * 
 * @author yannick.robin
 */

public class GlassFishAppServer extends BMAppServer {
	public static final int TYPE_GLASSFISH = 3;
    private static final String WEB_APPLICATION_CLASS_NAME = "com.bluemartini.thirdparty.glassfish.GlassFishWebApplication";

    public GlassFishAppServer() throws BMServerException {
    }

    /**
    ** Overrides BMAppServer method
    */
    public int getType() {
        return TYPE_GLASSFISH;
    }

    public String getWebApplicationClassName() {
        return WEB_APPLICATION_CLASS_NAME;
    }
    
	@Override
	public void exitOnFailure() throws BMServerException {
		return;
	}
}

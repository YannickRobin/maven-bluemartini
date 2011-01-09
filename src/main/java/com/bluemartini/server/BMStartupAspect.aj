package com.bluemartini.server;

import java.lang.String;
import java.util.HashMap;

/**
 * Fix restart error when the application is redeployed 
 * @author Yannick Robin
*/ 
 
public aspect BMStartupAspect {	
	
	String around(String name, String config, HashMap args)
	: execution(public String BMStartup.startup(String, String, HashMap)) && args(name, config, args)
	{
		System.out.println("*** martini-patch loaded ***");
		BMStartup.isStarted_ = false;
		return proceed(name, config, args);
	}
		
}
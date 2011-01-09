package com.bluemartini.server;

import java.lang.String;
import java.util.HashMap;

/**
 * Indicate martini-patch is loaded
 * @author Yannick Robin
*/ 
 
public aspect BMStartupAspect {	
	
	before(String name, String config, HashMap args)
	: execution(public String BMStartup.startup(String, String, HashMap)) && args(name, config, args)
	{
		System.out.println("*** martini-patch loaded ***");
	}
		
}
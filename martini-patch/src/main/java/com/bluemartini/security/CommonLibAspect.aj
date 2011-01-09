package com.bluemartini.security;

import java.lang.String;
import java.lang.StringBuilder;
import java.io.File;

import com.bluemartini.core.BMSystem;

/**
 * Fix to load security files in deployed mode.
 * Exception: javax.crypto.BadPaddingException: Given final block not properly padded
 * @author Yannick Robin
*/

privileged aspect CommonLibAspect {
	
	pointcut initFilePaths(CommonLib myCommonLib) : execution(private void CommonLib.initFilePaths()) && this(myCommonLib);
	
	void around(CommonLib myCommonLib) : initFilePaths(myCommonLib)
	{    	
    	String bmsSecurityDir = BMSystem.getProperty("BMS_SECURITY_DIR");
    	System.out.println("******************************* BMS_SECURITY_DIR = " + bmsSecurityDir);
        if (bmsSecurityDir != null){
            //passFile_ = bmsSecurityDir + "/" + passFile_;
            //storeFile_ = bmsSecurityDir + "/" + storeFile_;
            //backFile_ = bmsSecurityDir + "/" + backFile_;
            myCommonLib.passFile_ = (new StringBuilder()).append(BMSystem.getProperty("BMS_SECURITY_DIR")).append(File.separatorChar).append("common.lib").toString();
            myCommonLib.storeFile_ = (new StringBuilder()).append(BMSystem.getProperty("BMS_SECURITY_DIR")).append(File.separatorChar).append("security.jks").toString();
            myCommonLib.backFile_ = (new StringBuilder()).append(BMSystem.getProperty("BMS_SECURITY_DIR")).append(File.separatorChar).append("network.lib").toString();
        }
	}
}

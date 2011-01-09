package com.bluemartini.app;

import java.lang.String;

import com.bluemartini.app.wizards.VersionChooserWizard;
import com.bluemartini.core.Constants;
import com.bluemartini.dna.*;
import com.bluemartini.security.BMAccessControl;
import com.bluemartini.server.BMClient;
import com.bluemartini.ui.*;
import com.bluemartini.util.*;

/**
 * Fix to use local EAC
 * @author Yannick Robin
*/

public aspect VersionUtilAspect {	
	
	void around(BusinessObject boNewVersion)
	: execution(public static void VersionUtil.setNewVersion(BusinessObject)) && args(boNewVersion)
	{
		System.out.println("VersionUtil fix!!!!");
        BMAccessControl.refresh();

        if (boNewVersion == null) return;

        Integer iCurrentVersionID_ = BMThreadManager.getCurrentVersionID();
        Integer iNewVersionID_ = boNewVersion.getIntegerID();

        if ((iCurrentVersionID_ != null) &&
            (iCurrentVersionID_.equals(iNewVersionID_))) return;

        BMThreadManager.setCurrentVersionID(iNewVersionID_);
        VersionUtil.boCurrentVersion_ = boNewVersion;

        BaseFrame frame = BaseApp.getBaseFrame();
        BusinessObject boEnv;
        // get the environment for the version
        try {

            Integer envID = BMContext.getEnvIDForVersion(iNewVersionID_);

             // get the environment business object
             boEnv = BMContext.createBusinessObject("ENVIRONMENT");
             boEnv.setInteger("env_id", envID);
             //YRO CUSTOM Change to run embedded EAC
             DNAList dnaEnvOut = BMClient.executeBusinessAction("EACGetObjectDetail", boEnv, null);
             //DNAList dnaEnvOut = BMClient.executeBusinessAction("GetObjectDetail", boEnv, null, "eac");
             boEnv = dnaEnvOut.getBusinessObject("ENVIRONMENT");

            if (boEnv == null) {
                throw new BMException("ENVIRONMENT_OBJECT_NULL");
            }

            String sDesc = boEnv.getString("shortDesc");
            if (sDesc == null || sDesc.length() == 0) {
                sDesc = boEnv.getString("name");
            }

            // set the application's window title
            frame.setTitle(BMContext.getAppConfig().getString("title") + " : " + sDesc);

            BlueMartiniMerchandiser.selectedLocaleOne.setInteger
                ("localeID", LocaleUtil.getDefaultLocaleID());
            BlueMartiniMerchandiser.selectedLocaleTwo.setInteger
                ("localeID", LocaleUtil.getDefaultLocaleID());


            AttributeUtil.uncacheAllAttributes(iCurrentVersionID_, false);


        } catch (BMException bme)  {

             BMLog.log(BMLog.COMPONENT_ED, 0, bme.getMessage());
             return;

        }

        return;
    }
	
		
} 

package com.bluemartini.remotedesktop.util;

import java.lang.String;

import com.bluemartini.dna.BMException;
import com.bluemartini.dna.BusinessObjectArray;
import com.bluemartini.dna.DNAList;
import com.bluemartini.server.BMClient;

/**
 * Fix to use local EAC
 * @author Yannick Robin
*/

public aspect UserGroupUtilAspect {	
		
	BusinessObjectArray around(Long userID) throws BMException
	: execution(public static BusinessObjectArray UserGroupUtil.getGroups(Long)) && args(userID)
    {

      BusinessObjectArray groups = null;
      // build where clause
      String sql = "USG_ID IN "
      + "(SELECT UUG_USG_ID FROM USER_USR_GRP WHERE UUG_USA_ID="
      + userID
      + ")";

      //TODO: setObject is not working, so cannot pass in bindarray
      DNAList dnaIn = new DNAList();
      dnaIn.setString("where", sql);
      dnaIn.setString("type", "USER_GROUP");
      DNAList dnaOut = BMClient.executeBusinessAction("EACGetObjects", dnaIn);
      groups = dnaOut.getBusinessObjectArray("USER_GROUP_ARRAY");

      return groups;
    }	
		
}
package ${package}.tools.testbatch;

import com.bluemartini.core.BMUtil;
import com.bluemartini.dna.BMContext;
import com.bluemartini.dna.BMException;
import com.bluemartini.dna.BMLog;
import com.bluemartini.dna.BMThreadManager;
import com.bluemartini.dna.BusinessObject;
import com.bluemartini.util.HTMLVersionUtil;
import com.bluemartini.util.MainApp;

/**
 *
 */

public class TestBatchDB extends MainApp {
	private static String sAppConfig_ = BMUtil.getHome() + "${artifactId}/config/testbatchdb.appconfig.dna";

	protected TestBatchDB() {
		super("TestBatchDB", sAppConfig_);
		setEnvironmentOption(true, true);
	}

	public static void main(String[] args) {
		new TestBatchDB().mainImpl(args);
	}

	protected void setupOptions() {
		setEnvironmentOption(true, true);
		super.setupOptions();
	}

	public void run() throws BMException {
		
		//Set pubVersion for published environment
		boolean bUsePubVersions = BMContext.getAppConfig().getBoolean("usePubVersions", false);
		HTMLVersionUtil.setUsePubVersions(bUsePubVersions);
		if (HTMLVersionUtil.isUsingPubVersions())
		{
			//@TODO Add an optional option to the command line in order to set the pubVersion
			BusinessObject boVersion = HTMLVersionUtil.getDefaultVersion();
			BMThreadManager.setCurrentPubVersionID(boVersion.getInteger("pve_id"));
			BMLog.log(BMLog.COMPONENT_SYSTEM, 0, "Current pub version is " + BMThreadManager.getCurrentPubVersionID());
		}
		
		TestBatchConfig testBatchConfig = TestBatchConfig.getInstance();
		System.out.println(testBatchConfig.getMessage());
		
	}

}





		

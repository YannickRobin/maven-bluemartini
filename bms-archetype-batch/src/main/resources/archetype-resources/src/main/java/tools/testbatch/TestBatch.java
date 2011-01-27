package ${package}.tools.testbatch;

import com.bluemartini.core.BMUtil;
import com.bluemartini.dna.BMException;
import com.bluemartini.util.MainApp;

/**
 *
 */

public class TestBatch extends MainApp {
	private static String sAppConfig_ = BMUtil.getHome() + "${artifactId}/config/testbatch.appconfig.dna";

	protected TestBatch() {
		super("TestBatch", sAppConfig_);
		setEnvironmentOption(true, true);
	}

	public static void main(String[] args) {
		new TestBatch().mainImpl(args);
	}

    public boolean isDatabaseInitRequired() {
        return false;
    }
    
	protected void setupOptions() {
		setEnvironmentOption(false, false);
		super.setupOptions();
	}

	public void run() throws BMException {		
		TestBatchConfig testBatchConfig = TestBatchConfig.getInstance();
		System.out.println(testBatchConfig.getMessage());		
	}

}
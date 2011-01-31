package ${package}.tools.testbatch;

import com.bluemartini.core.BMUtil;
import com.bluemartini.dna.BMContext;
import com.bluemartini.dna.BMException;
import com.bluemartini.util.MainApp;

/**
 * Created by maven-bluemartini archetype
 * For test only
 * @author Yannick Robin
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
		String message = BMContext.getConfig("testbatch.dna").getString("message", "Message is missing");				
		System.out.println(message);	
	}

}
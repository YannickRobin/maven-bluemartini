package ${package}.tools.testbatch;

import com.bluemartini.dna.BMContext;
import com.bluemartini.dna.BMException;
import com.bluemartini.dna.DNAList;

/**
 * Test batch config class
 * 
 *
 * @author Yannick Robin
 */

public class TestBatchConfig {
	private static TestBatchConfig INSTANCE = null;
	private static DNAList config;
	private static String message;
	
	/**
	 * Singleton pattern
	 * Hidden constructor
	 * @throws BMException 
	 */
	private TestBatchConfig() {}
	
	/**
	 * Singleton pattern
	 * @return TestBatchConfig instance
	 * @throws BMException 
	 */
	public static synchronized TestBatchConfig getInstance() throws BMException
	{
		if (INSTANCE == null)
		{		
			config = BMContext.loadAndMergeDNAsFromModules("testbatch.dna", null);
			if (config == null){
				throw new BMException("testbatch.dna is missing");
			}
			
			message = config.getString("message", "Message is missing");
			
			INSTANCE = new TestBatchConfig();
		}
		
		return INSTANCE;
	}
	
	public String getMessage()
	{
		return message;
	}
	
}

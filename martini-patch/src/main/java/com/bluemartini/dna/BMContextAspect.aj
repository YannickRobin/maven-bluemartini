package com.bluemartini.dna;

import java.lang.String;
import java.lang.StringBuffer;
import java.lang.ClassLoader;
import java.lang.Thread;
import java.util.Enumeration;
import java.io.IOException;
import java.net.URL;
import com.bluemartini.dna.DNAList;
import com.bluemartini.dna.BMException;
import com.bluemartini.core.Constants;

/**
 * Fix to read DNA configuration files from JAR's
 * @author Yannick Robin
*/

public aspect BMContextAspect {	

    /** File separator used when requesting resources */
    private static char JAVA_SEPARATOR = '/';

	pointcut readModuleConfigFile(String sModulePath, String fileName, StringBuffer sbErrors)
	: execution(public static DNAList BMContext.readModuleConfigFile(String, String, StringBuffer)) && args(sModulePath, fileName, sbErrors);

	/**
	 * If module path starts with "!", config file should be loaded
	 * as a resource.
	 */	
	DNAList around(String sModulePath, String fileName, StringBuffer sbErrors)
	: readModuleConfigFile(sModulePath, fileName, sbErrors)	
	{
		if (sModulePath.startsWith("!"))
		{
			return readModuleConfigFileFromResource(sModulePath, fileName, sbErrors);
		}
		return proceed(sModulePath, fileName, sbErrors);
	}
	
	/**
	 * Get config file from classloader
	 */	
    private static DNAList readModuleConfigFileFromResource(String sModulePath, String fileName, StringBuffer sbErrors)
    {	
    	sModulePath = sModulePath.substring(1);

        String[] files = getFileNames(fileName);        
        // try all known extensions in order
        for(String file : files) {
        	String resource = sModulePath + JAVA_SEPARATOR + file;
    		ClassLoader cl = Thread.currentThread().getContextClassLoader();
			Enumeration<URL> urls = null;
			try {
				urls = cl.getResources(resource);
			} catch (IOException e) {
				e.printStackTrace();
				sbErrors.append(e.toString());				
			}
			DNAList dna = new DNAList();
            while(urls!=null && urls.hasMoreElements())
            {
            	URL url = urls.nextElement();

	        	int format = 0;
	        	String encoding = null;
	        	boolean readFilesAsResources = BMContext.isStandAlone();
	        	int mergeOptions = 0;
	        	
	        	
	        	try {
	    			DNAList dnaTemp = DNAList.readDNAFile(url, encoding, format, mergeOptions);
	    			dna.move(dnaTemp);
	        	} catch (BMException e) {
	    			e.printStackTrace();
	                sbErrors.append("Failed to load DNA file ("+url.toString()+"):\n\n"
	                            + e.toString());
	                return null;
	        	}
    		}
            return dna;
        }
		return null;
    }
    
    /**
     * DNA configuration file extensions in search order.
     */
    private static final String[] EXTENSIONS = new String[] {
        Constants.DN8_FILE_EXTENSION,  // .dn8
        Constants.DNA_FILE_EXTENSION,  // .dna
        Constants.XDNA_FILE_EXTENSION  // .dna.xml
    };
        
    /**
     * Create an array of all the file names we should try for a given name in
     * order.
     * 
     * @param filename
     *            the file we want
     * @return the possible names
     */
    private static String[] getFileNames(String filename) {
        String[] result = new String[EXTENSIONS.length];
        
        // trim away any known extension
        String stem = filename;
        for( String ext : EXTENSIONS ) {
            if( stem.endsWith(ext) ) {
                stem = stem.substring(0,stem.length()-ext.length());
                break;
            }
        }
        
        result[0] = filename;
        
        // try all known extensions in order
        int j=1;
        for(int i=0;i<EXTENSIONS.length;i++) {
            String res = stem + EXTENSIONS[i];
            if( ! res.equals(filename) ) {
                if( j==result.length ) {
                    String[] tmp = new String[result.length+1];
                    System.arraycopy(result,0,tmp,0,result.length);
                }
                result[j] = res;
                j++;
            }
        }

        return result;
    }    
    			
} 
 

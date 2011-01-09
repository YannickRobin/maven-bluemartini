package com.bluemartini.thirdparty.jboss;

import javax.naming.*;
import java.util.*;

import com.bluemartini.core.JNDIUtil;


/**
 * JBoss specific JNDI connection
 * @author Yannick Robin
 */
public class JBossJNDIUtil extends JNDIUtil
{

	  protected Hashtable jndiProps_;
	  protected InitialContext initialContext_;
	  private static Hashtable registeredObjects_ = new Hashtable();
	  private static final String INITIAL_CONTEXT_FACTORY_NAME = "org.jnp.interfaces.NamingContextFactory";

	  /**
	  * Construct an initialized JNDIUtil object.
	  * @param jndiServerURL the url of the JNDI Server in String form. May not be <b>null</b>
	  * @param initialContextFactoryName name of the class to use for the initial context
	  * factory. May not be <b>null</b>
	  */
	  public JBossJNDIUtil(String jndiServerURL, String initialContextFactoryName) throws NamingException
	  {
	    Hashtable jndiProps = new Hashtable();
	    jndiProps.put(Context.INITIAL_CONTEXT_FACTORY, initialContextFactoryName);
	    jndiProps.put(Context.PROVIDER_URL, jndiServerURL);
	    jndiProps.put(Context.URL_PKG_PREFIXES,"org.jboss.naming:org.jnp.interfaces");
	    
	    init(jndiProps);
	  }
	  
	  /**
	   * Construct a JNDIUtil object.
	   * @param jndiProps properties file which describes all of the JNDI settings for
	   * the current JNDI provider. May be <b>null<b>.
	   */
	  public JBossJNDIUtil( Hashtable jndiProps )
	    throws NamingException
	  {    
	    init(jndiProps);
	  }

	  /**
	   * Construct a JNDIUtil object.
	   * Constructs the InitialContext using the default System properties
	   */
	  public JBossJNDIUtil()
	    throws NamingException
	  {
	    this(null);
	  }	  

	  /**
	   * Bind an object to the JNDI tree. Calls bind(String, Object, true)
	   * @param name name to bind to the tree
	   * @param obj object to bind to the tree
	   * @see javax.naming.InitialContext#bind(String, Object)
	   */
	  public void bind(String name, Object obj) throws NamingException
	  {
		  bind(name, obj);
	  }

	  /**
	   * Bind an object to the JNDI tree.
	   * @param name name to bind to the tree
	   * @param obj object to bind to the tree
	   * @param registerObject register object to be destroy by shutdown
	   * @see javax.naming.InitialContext#bind(String, Object)
	   */
	  public void bind(String name, Object obj, boolean registerObject) throws NamingException
	  {
		  //JBoss specific @see createSubContext()
		  createSubContext(name);
		  super.bind(name, obj, registerObject);
	  }

	  /**
	   * Rebind an object to the JNDI tree. Calls bind(String, Object, true)
	   * @param name name to bind to the tree
	   * @param obj object to bind to the tree
	   * @see javax.naming.InitialContext#rebind(String, Object)
	   */
	  public void rebind( String name, Object obj) throws NamingException
	  {
		  rebind(name, obj, true);
	  }

	  /**
	   * Rebind an object to the JNDI tree.
	   * @param name name to bind to the tree
	   * @param obj object to bind to the tree
	   * @param registerObject register object to be destroy by shutdown
	   * @see javax.naming.InitialContext#rebind(String, Object)
	   */
	  public void rebind( String name, Object obj, boolean registerObject) throws NamingException
	  {
		if( registerObject )
		  registerObject(name);
		
		//JBoss specific @see com.bluemartini.thirdparty.jboss.JBossJNDIUtil#createSubContext(String)
		createSubContext(name);
		
		super.rebind(name, obj, registerObject);
	  }
  
	/**
	* Parse name and create JNDI sub-context (i.e: com/bluemartini/bizact/<app>)
	* With WebLogic, WebSphere and JBoss AS 4, JNDI sub-context is auto-created by ctx.bind/rebind. 
	* With JBoss AS 5 JNDI binding do not work if the sub-context do not exist and need to be created manually.
	* @param name to bind to the tree
	*/
  
	public void createSubContext(String sName) throws NamingException 
	{
		Context ctx = getInitialContext();
		NameParser nameParser = ctx.getNameParser(sName); 
		Name name = nameParser.parse(sName);
		    
		for(int n = 0; n < name.size(); n ++)
		{
			String atom = name.get(n);
			try
			{
				Object object = ctx.lookup(atom);
				ctx = (Context) object;
			}
			catch(NamingException e)
			{	// No binding exists, create a subcontext
				ctx = ctx.createSubcontext(atom);
			}
		}  
	}
}
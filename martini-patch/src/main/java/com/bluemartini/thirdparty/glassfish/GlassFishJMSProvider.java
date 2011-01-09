package com.bluemartini.thirdparty.glassfish;

import javax.naming.*;
import javax.jms.*;
import javax.jms.Queue;
import com.bluemartini.core.*;
import com.bluemartini.dna.*;
import com.bluemartini.jms.*;
import com.bluemartini.server.*;

/**
 * WebLogic-specific GlassFish provider.  Performs client and server
 * JMS initialization.
 *
 * @author Yannick Robin
 */

public class GlassFishJMSProvider extends JMSProvider {

    /**
     * Called immediately after instantiation.
     */

    protected void initProvider() throws BMException {
        super.initProvider();
    }

    /**
     * Initialize the provider for use by a JMS client.
     *
     * @param jndiURL URL for JNDI tree
     * @param dnaJMSConfig client configuration
     */
    public void initClient(String jndiURL, DNAList dnaJMSConfig) throws BMException {
        super.initClient(jndiURL, dnaJMSConfig);
    }

    /**
     * Initialize the provider for use by a JMS server.
     *
     * @param jndiURL URL for JNDI tree
     * @param dnaJMSConfig server configuration
     */
    public void initServer(String jndiURL, DNAList dnaJMSConfig) throws BMException {
        super.initServer(jndiURL, dnaJMSConfig);
    }

    /**
     * Retrieve the context used to retrieve the JMS JNDI tree.
     *
     * @param  sURL  url used to retrieve the JNDI context
     * @param  dnaJMSConfig  jms configuration information
     *
     * @return  the JMS JNDI context
     */
    public Context getJMSContext(String sURL, DNAList dnaJMSConfig) throws BMException {
        BMAppServer appServer = BMAppServer.getAppServer();
        try {
            JNDIUtil jndiUtil = appServer.getJNDIUtil(sURL);
            InitialContext ic = jndiUtil.getInitialContext();
            return ic;
        } catch (Exception ne) {
            throw new BMException("JMS_JNDI_FACTORY_FAILURE", ne, null);
        }
    }

    /**
     * Initialize the connection factories on the server.  The factories
     * themselves will be accessed by clients via the JNDI tree.
     *
     * @param  ctxt  the current JNDI context
     */

    public void initConnectionFactories(Context ctxt) throws BMException {
        return;
    }

    /**
     * Create a JMS Topic given a TopicSession and bind into JNDI tree.
     * Default implementation should usually be sufficient.
     *
     * @param  context  JNDI context into which the topic will be bound
     * @param  topicName  Topic and JNDI name
     * @param  topicSession  TopicSession used to create the topic
     *
     * @return  the requested Topic
     */

    public Topic createTopic(Context context, String topicName, TopicSession topicSession) throws BMException {
        return null;
    }

    /**
     * Create a JMS Queue given a QueueSession and bind into JNDI tree.
     * Default implementation should usually be sufficient.
     *
     * @param  context  JNDI context into which the queue will be bound
     * @param  queueName  Queue and JNDI name
     * @param  queueSession QueueSession used to create the queue
     *
     * @return  the requested Queue
     */

    public Queue createQueue(Context context, String queueName, QueueSession queueSession) throws BMException {
        return null;
    }
}

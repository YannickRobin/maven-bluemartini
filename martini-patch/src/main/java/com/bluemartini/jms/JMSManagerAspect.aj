package com.bluemartini.jms;

import java.lang.String;

import com.bluemartini.core.BMSystem;
import com.bluemartini.dna.*;
import com.bluemartini.server.BMServer;
import com.bluemartini.server.BMWebApplication;

import javax.jms.*;
import javax.naming.Context;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Stack;
import java.util.Vector;

/**
 * Add maxAbortAttempt (default is 5)
 * @author Yannick Robin
*/

privileged aspect JMSManagerAspect {	

	pointcut initConnection(JMSManager myJMSManager) : execution(private void JMSManager.initConnection()) && this(myJMSManager);
	
	void around(JMSManager myJMSManager) : initConnection(myJMSManager)
	{
    	//YRO CUSTOM
    	int maxAbortAttempt = myJMSManager.dnaJMSConfig_.getInteger("maxAbortAttempt", 5);
    	int attempt = 0;
    	
        while (!myJMSManager.bConnected_ && !BMThreadManager.aborted() && attempt<maxAbortAttempt)
        {
        	attempt++;
            try {

                // Retrieve JNDI context
                myJMSManager.ctx_ = myJMSManager.jmsProvider_.getJMSContext(myJMSManager.sURL_, myJMSManager.dnaJMSConfig_);

                // Get a TopicConnection to the JMS server
                System.out.println("BM JMS:  Creating Topic Connection to JMS Server " + myJMSManager.sURL_);
                DNAList dnaFactoryConfig = myJMSManager.dnaJMSConfig_.getList("topicConnectionFactory");
                myJMSManager.topicConnection_ = JMSUtil.getTopicConnection(myJMSManager.ctx_, dnaFactoryConfig);
                if (!BMServer.isOnServer())
                  // method not allowed in a webcontainer
                  myJMSManager.topicConnection_.setExceptionListener(myJMSManager.exceptionListener_);

                // Get a Queue Connection to the JMS server
                System.out.println("BM JMS:  Creating Queue Connection to JMS Server " + myJMSManager.sURL_);
                dnaFactoryConfig = myJMSManager.dnaJMSConfig_.getList("queueConnectionFactory");
                myJMSManager.queueConnection_ = JMSUtil.getQueueConnection(myJMSManager.ctx_, dnaFactoryConfig);
                if (!BMServer.isOnServer())
                  // method not allowed in a webcontainer
                  myJMSManager.queueConnection_.setExceptionListener(myJMSManager.exceptionListener_);

                System.out.println("BM JMS:  Successfully connected to JMS Server " + myJMSManager.sURL_);
                myJMSManager.bConnected_ = true;

                // increment connectionID
                myJMSManager.connectionID_ = myJMSManager.connectionID_ + 1;
            }
            catch (Exception e)
            {
                System.out.println("BM JMS:  Connect to JMS Server " + myJMSManager.sURL_ + " failed.  Will retry in " + myJMSManager.nSleepSecs_ + " seconds");
                BMLog.log(BMLog.COMPONENT_JMS, 0, "BM JMS:  Unable to create connection to server: " + myJMSManager.sURL_, e);
                if (e instanceof JMSException) {
                    Exception le = ((JMSException)e).getLinkedException();
                    if (le != null )
                        BMLog.log(BMLog.COMPONENT_JMS, 0, "BM JMS: Linked Exception: ", le);
                }

                myJMSManager.cleanup(true);
                try {
                    Thread.sleep(myJMSManager.nSleepSecs_ * 1000);
                } catch (InterruptedException ie) {}
            }
        }	 
	}	
}    
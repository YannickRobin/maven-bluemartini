from os import environ
wls_domain="/home/yannick/apps/bea/user_projects/domains/BlueMartiniDev"
serverName="AdminServer"
readDomain(wls_domain)

jmsName = ""
if jmsName == "":
   jmsName=serverName

cd('/')
try:
   create(jmsName + '.BMJMSServer', 'JMSServer')
except  Exception,udt:
   print "The JMS server exists"
cd('/')
 
persistenceEnabled = false
if persistenceEnabled :
    storePool = ""
    storeDir = ""
    if storePool != None :
        try:
            create(jmsName + '.BMJMSJDBCStore', 'JDBCStore')
        except  Exception,udt:
            pass
        poolName = "com.bluemartini.dbpool." + jmsName + "." + storePool
        cd('/JDBCStore/' + jmsName + '.BMJMSJDBCStore')
        set('DataSource',poolName)
        cd('/JMSServer/' + jmsName + '.BMJMSServer')
        set('PersistentStore', jmsName + '.BMJMSJDBCStore')
        cd('/JDBCStore/' + jmsName + '.BMJMSJDBCStore')
        set('Target',target)
    if storeDir != None :
         try:
            create(storeDir, 'FileStore')
         except  Exception,udt:
            pass
         cd('/JMSServer/' + jmsName + '.BMJMSServer')
         set('PersistentStore', storeDir)
         cd('/FileStore/' + storeDir)
         set('Target',serverName)

cd('/')

try:
   create(jmsName + 'BMJMSSystemResource', 'JMSSystemResource')
except  Exception,udt:
   pass
cd('JMSSystemResource/' + jmsName + 'BMJMSSystemResource/JmsResource/NO_NAME_0')

try:
   create(jmsName + '.BMJMSTemplate','Template')
except  Exception,udt:
   pass

try:
  create('com.bluemartini.PublishVersionTopic','Topic')
except Exception, e:
  pass
cd('Topic/com.bluemartini.PublishVersionTopic')
set('JNDIName', 'com.bluemartini.PublishVersionTopic')
set('SubDeploymentName', jmsName + 'TopicsAndQueues')
cd('../..')

try:
  create('com.bluemartini.DBUtilTopic','Topic')
except Exception, e:
  pass
cd('Topic/com.bluemartini.DBUtilTopic')
set('JNDIName', 'com.bluemartini.DBUtilTopic')
set('SubDeploymentName', jmsName + 'TopicsAndQueues')
cd('../..')




   
try:
   create('bluemartini.jms.BMTopicConnectionFactory', 'ConnectionFactory')
except  Exception,udt:
   pass

cd('ConnectionFactory/bluemartini.jms.BMTopicConnectionFactory')
set('JNDIName', 'bluemartini.jms.BMTopicConnectionFactory')
set('SubDeploymentName', jmsName + 'TopicSupDeployment')

cd('/')
cd('JMSSystemResource/' + jmsName + 'BMJMSSystemResource')
try:
   create(jmsName + 'TopicSupDeployment', 'SubDeployment')
except  Exception,udt:
   pass
 
cd('/JMSSystemResource/' + jmsName + 'BMJMSSystemResource/JmsResource/NO_NAME_0')

try:
   create('bluemartini.jms.BMQueueConnectionFactory', 'ConnectionFactory')
except  Exception,udt:
   pass

cd('ConnectionFactory/bluemartini.jms.BMQueueConnectionFactory')
set('JNDIName', 'bluemartini.jms.BMQueueConnectionFactory')
set('SubDeploymentName', jmsName + 'QueueSupDeployment')

cd('/')
cd('JMSSystemResource/' + jmsName + 'BMJMSSystemResource')
try:
   create(jmsName + 'QueueSupDeployment', 'SubDeployment')
except  Exception,udt:
   pass
cd('/')
cd('JMSSystemResource/' + jmsName + 'BMJMSSystemResource')
try:
   create(jmsName + 'TopicsAndQueues', 'SubDeployment')
except  Exception,udt:
   pass
assign('JMSServer', jmsName + '.BMJMSServer', 'Target', serverName)
assign('JMSSystemResource', jmsName + 'BMJMSSystemResource', 'Target', serverName)

assign('JMSSystemResource.SubDeployment', jmsName + 'BMJMSSystemResource.'+ jmsName +'TopicSupDeployment', 'Target', jmsName + '.BMJMSServer')
assign('JMSSystemResource.SubDeployment', jmsName + 'BMJMSSystemResource.'+ jmsName +'QueueSupDeployment', 'Target', jmsName + '.BMJMSServer')
assign('JMSSystemResource.SubDeployment', jmsName + 'BMJMSSystemResource.'+ jmsName +'TopicsAndQueues', 'Target', jmsName + '.BMJMSServer')

updateDomain()
closeDomain()


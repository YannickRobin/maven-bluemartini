

# ************* RESOURCES SCRIPT FOR ${artifactId} ************ 

import os, sys
bms_cell="POSEIDONCell01"
bms_cluster=""
bms_node="POSEIDONNode01"
bmsserver="BM_${artifactId}"
db2_instance_home="null"
oracle_home="C:/Apps/oracle/product/10.2.0/db_1"

server = AdminConfig.getid("/Node:" + bms_node + "/Server:" + bmsserver + "/" )
node = AdminConfig.getid("/Node:" + bms_node + "/" )

if (len(node) == 0):
        print "Unable to find node: "+bms_node
        sys.exit(1)
        
# Check for the existence of the jdbc providers
availableJDBCProviders = AdminTask.listJDBCProviders("-scope Node=" + bms_node)

jdbcProviderName = "";
dbVendor = 'oracle'
providerName = ""
if dbVendor.startswith("db2"):
	providerName = "DB2 JDBC Provider"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.DB2DataStoreHelper"]
elif dbVendor.startswith("oracle"):
	providerName = "Oracle JDBC Driver"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper"]
if len(availableJDBCProviders) > 0:
        provLen = len(availableJDBCProviders) - 1
        provList = availableJDBCProviders[1:provLen].split(")")
        for nextJdbcProvider in provList:
            if len(nextJdbcProvider) > 0:
	       	    nextJdbcProvider = nextJdbcProvider + ')'
	            if  (nextJdbcProvider.startswith(providerName)):
	            	jdbcProviderName = nextJdbcProvider

#JDBC Provider and its props may be in vars
if (jdbcProviderName == ""):
	#Set DB2 JDBC Provider
	if providerName.startswith("DB2 JDBC Provider"):
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "COM.ibm.db2.jdbc.DB2ConnectionPoolDataSource"]
		if not db2_instance_home.endswith("/"):
			db2_instance_home = db2_instance_home + "/" 
		classpath = ["classpath", db2_instance_home + "sqllib/java"]
		nativepath = ["nativepath", db2_instance_home + "sqllib/lib"]
		jdbcattrs = [jdbc_name, implCN, classpath, nativepath]
	elif providerName.startswith("Oracle JDBC Driver"):
	#Set Oracle JDBC Driver
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "oracle.jdbc.pool.OracleConnectionPoolDataSource"]
		classpath = ["classpath", oracle_home + "/jdbc/lib/ojdbc14.jar"]
		jdbcattrs = [jdbc_name, implCN, classpath]
	else :
		print "Unknown JDBC provider. Please try to re-configure it."
		sys.exit(1)
	
	jdbcProviderName = AdminConfig.create("JDBCProvider", node, jdbcattrs )
	print "The JDBCProvider " + jdbcProviderName + " successfully created.\n"	 
else : 	
	print "The JDBC Provider " + jdbcProviderName + " already exists.\n"	 
	
dbnameAttr = [["name", "databaseName"], ["value", 'martini'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
urlAttr = [["name", "URL"], ["value", 'jdbc:oracle:thin:@POSEIDON:1521:BM1'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
dsListname = ["name", "${artifactId}.store"]
jndiListName = ["jndiName", "jdbc/${artifactId}.store"]
#userAttr = [["name", "user"], ["value", 'bm101_STORE'], ["type", "java.lang.String"]] 
#passwordAttr = [["name", "password"], ["value", 'martini'], ["type", "java.lang.String"]]
# newprops = [userAttr, passwordAttr, dbnameAttr]
newprops = [dbnameAttr, urlAttr]
psAttr = ["propertySet", [["resourceProperties", newprops]]]

# create authentication data
print "Creating JAASAuthData object for component-managed authentication, user bm101_STORE ..." 
try:
	aliasName = "BMJAASAuthData_bm101_STORE"
	sec = AdminConfig.getid("/Cell:" + bms_cell + "/Security:/")
	aliasAttr = ["alias", aliasName]
	descAttr = ["description", "Authentication information when component-managed"]
	useridAttr = ["userId", "bm101_STORE"]
	passwordAttr = ["password", "martini"]
	attrs = []
	attrs.append(aliasAttr)
	attrs.append(descAttr)
	attrs.append(useridAttr)
	attrs.append(passwordAttr)
	appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 
	print "done."
except:
	# note: if I catch exception here, the script interrupts... crap
	print "An exception occured,  probably the authentication data already exists."
	
authAlias = ["authDataAlias", aliasName]
dsAttrs = [dsListname, jndiListName, dshelper, authAlias, psAttr]



# create the datasources
print "Creating DataSource ${artifactId}.store ...  "
availableDsrc = ""
availableDatasources = AdminTask.listDatasources("-scope Node=" + bms_node)
if len(availableDatasources) > 0:
	dSrcLen = len(availableDatasources) - 1
	dSrcList = availableDatasources.split()
	for nextDatasource in dSrcList:
		if  (nextDatasource.startswith("${artifactId}.store")):
			availableDsrc = nextDatasource            

if (availableDsrc == ""):
	newds = AdminConfig.create('DataSource', jdbcProviderName, dsAttrs)
	initialCapacity = '10'
	maxCapacity = '20'
	cpAttrs = []
	if (initialCapacity != '' and maxCapacity != ''):
		minConnectionsAttr = ["minConnections", initialCapacity]
		maxConnectionsAttr = ["maxConnections", maxCapacity]
		cpAttrs = [minConnectionsAttr, maxConnectionsAttr]
		
	AdminConfig.create('ConnectionPool', newds, cpAttrs)
	print "done."	
else : 
	print "The datasource " + availableDsrc + " already exists.\n"	 

   
# use this script to set the custom variable
print "Setting the invokeFiltersCompatibility variable ..."
var = "com.ibm.ws.webcontainer.invokefilterscompatibility"
server = AdminConfig.getid("/Cell/" + bms_cell + "/Node/" + bms_node \
	+ "/Server/" + bmsserver + "/")
serverWebContainer = AdminConfig.list("WebContainer", server)
attrs = [["name", var], \
				["value", "true"], \
				["description", "compatibility mode"]]
try: 
	AdminConfig.create("Property", serverWebContainer, attrs)
except: 
	print "The variable com.ibm.ws.webcontainer.invokefilterscompatibility already set."
print "done."


server = AdminConfig.getid("/Node:" + bms_node + "/Server:" + bmsserver + "/" )
node = AdminConfig.getid("/Node:" + bms_node + "/" )

if (len(node) == 0):
        print "Unable to find node: "+bms_node
        sys.exit(1)
        
# Check for the existence of the jdbc providers
availableJDBCProviders = AdminTask.listJDBCProviders("-scope Node=" + bms_node)

jdbcProviderName = "";
dbVendor = 'oracle'
providerName = ""
if dbVendor.startswith("db2"):
	providerName = "DB2 JDBC Provider"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.DB2DataStoreHelper"]
elif dbVendor.startswith("oracle"):
	providerName = "Oracle JDBC Driver"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper"]
if len(availableJDBCProviders) > 0:
        provLen = len(availableJDBCProviders) - 1
        provList = availableJDBCProviders[1:provLen].split(")")
        for nextJdbcProvider in provList:
            if len(nextJdbcProvider) > 0:
	       	    nextJdbcProvider = nextJdbcProvider + ')'
	            if  (nextJdbcProvider.startswith(providerName)):
	            	jdbcProviderName = nextJdbcProvider

#JDBC Provider and its props may be in vars
if (jdbcProviderName == ""):
	#Set DB2 JDBC Provider
	if providerName.startswith("DB2 JDBC Provider"):
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "COM.ibm.db2.jdbc.DB2ConnectionPoolDataSource"]
		if not db2_instance_home.endswith("/"):
			db2_instance_home = db2_instance_home + "/" 
		classpath = ["classpath", db2_instance_home + "sqllib/java"]
		nativepath = ["nativepath", db2_instance_home + "sqllib/lib"]
		jdbcattrs = [jdbc_name, implCN, classpath, nativepath]
	elif providerName.startswith("Oracle JDBC Driver"):
	#Set Oracle JDBC Driver
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "oracle.jdbc.pool.OracleConnectionPoolDataSource"]
		classpath = ["classpath", oracle_home + "/jdbc/lib/ojdbc14.jar"]
		jdbcattrs = [jdbc_name, implCN, classpath]
	else :
		print "Unknown JDBC provider. Please try to re-configure it."
		sys.exit(1)
	
	jdbcProviderName = AdminConfig.create("JDBCProvider", node, jdbcattrs )
	print "The JDBCProvider " + jdbcProviderName + " successfully created.\n"	 
else : 	
	print "The JDBC Provider " + jdbcProviderName + " already exists.\n"	 
	
dbnameAttr = [["name", "databaseName"], ["value", 'martini'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
urlAttr = [["name", "URL"], ["value", 'jdbc:oracle:thin:@POSEIDON:1521:BM1'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
dsListname = ["name", "${artifactId}.main"]
jndiListName = ["jndiName", "jdbc/${artifactId}.main"]
#userAttr = [["name", "user"], ["value", 'bm101_MAIN'], ["type", "java.lang.String"]] 
#passwordAttr = [["name", "password"], ["value", 'martini'], ["type", "java.lang.String"]]
# newprops = [userAttr, passwordAttr, dbnameAttr]
newprops = [dbnameAttr, urlAttr]
psAttr = ["propertySet", [["resourceProperties", newprops]]]

# create authentication data
print "Creating JAASAuthData object for component-managed authentication, user bm101_MAIN ..." 
try:
	aliasName = "BMJAASAuthData_bm101_MAIN"
	sec = AdminConfig.getid("/Cell:" + bms_cell + "/Security:/")
	aliasAttr = ["alias", aliasName]
	descAttr = ["description", "Authentication information when component-managed"]
	useridAttr = ["userId", "bm101_MAIN"]
	passwordAttr = ["password", "martini"]
	attrs = []
	attrs.append(aliasAttr)
	attrs.append(descAttr)
	attrs.append(useridAttr)
	attrs.append(passwordAttr)
	appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 
	print "done."
except:
	# note: if I catch exception here, the script interrupts... crap
	print "An exception occured,  probably the authentication data already exists."
	
authAlias = ["authDataAlias", aliasName]
dsAttrs = [dsListname, jndiListName, dshelper, authAlias, psAttr]



# create the datasources
print "Creating DataSource ${artifactId}.main ...  "
availableDsrc = ""
availableDatasources = AdminTask.listDatasources("-scope Node=" + bms_node)
if len(availableDatasources) > 0:
	dSrcLen = len(availableDatasources) - 1
	dSrcList = availableDatasources.split()
	for nextDatasource in dSrcList:
		if  (nextDatasource.startswith("${artifactId}.main")):
			availableDsrc = nextDatasource            

if (availableDsrc == ""):
	newds = AdminConfig.create('DataSource', jdbcProviderName, dsAttrs)
	initialCapacity = '10'
	maxCapacity = '20'
	cpAttrs = []
	if (initialCapacity != '' and maxCapacity != ''):
		minConnectionsAttr = ["minConnections", initialCapacity]
		maxConnectionsAttr = ["maxConnections", maxCapacity]
		cpAttrs = [minConnectionsAttr, maxConnectionsAttr]
		
	AdminConfig.create('ConnectionPool', newds, cpAttrs)
	print "done."	
else : 
	print "The datasource " + availableDsrc + " already exists.\n"	 

   
# use this script to set the custom variable
print "Setting the invokeFiltersCompatibility variable ..."
var = "com.ibm.ws.webcontainer.invokefilterscompatibility"
server = AdminConfig.getid("/Cell/" + bms_cell + "/Node/" + bms_node \
	+ "/Server/" + bmsserver + "/")
serverWebContainer = AdminConfig.list("WebContainer", server)
attrs = [["name", var], \
				["value", "true"], \
				["description", "compatibility mode"]]
try: 
	AdminConfig.create("Property", serverWebContainer, attrs)
except: 
	print "The variable com.ibm.ws.webcontainer.invokefilterscompatibility already set."
print "done."


server = AdminConfig.getid("/Node:" + bms_node + "/Server:" + bmsserver + "/" )
node = AdminConfig.getid("/Node:" + bms_node + "/" )

if (len(node) == 0):
        print "Unable to find node: "+bms_node
        sys.exit(1)
        
# Check for the existence of the jdbc providers
availableJDBCProviders = AdminTask.listJDBCProviders("-scope Node=" + bms_node)

jdbcProviderName = "";
dbVendor = 'oracle'
providerName = ""
if dbVendor.startswith("db2"):
	providerName = "DB2 JDBC Provider"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.DB2DataStoreHelper"]
elif dbVendor.startswith("oracle"):
	providerName = "Oracle JDBC Driver"
	dshelper = ["datasourceHelperClassname", "com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper"]
if len(availableJDBCProviders) > 0:
        provLen = len(availableJDBCProviders) - 1
        provList = availableJDBCProviders[1:provLen].split(")")
        for nextJdbcProvider in provList:
            if len(nextJdbcProvider) > 0:
	       	    nextJdbcProvider = nextJdbcProvider + ')'
	            if  (nextJdbcProvider.startswith(providerName)):
	            	jdbcProviderName = nextJdbcProvider

#JDBC Provider and its props may be in vars
if (jdbcProviderName == ""):
	#Set DB2 JDBC Provider
	if providerName.startswith("DB2 JDBC Provider"):
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "COM.ibm.db2.jdbc.DB2ConnectionPoolDataSource"]
		if not db2_instance_home.endswith("/"):
			db2_instance_home = db2_instance_home + "/" 
		classpath = ["classpath", db2_instance_home + "sqllib/java"]
		nativepath = ["nativepath", db2_instance_home + "sqllib/lib"]
		jdbcattrs = [jdbc_name, implCN, classpath, nativepath]
	elif providerName.startswith("Oracle JDBC Driver"):
	#Set Oracle JDBC Driver
		jdbc_name = ["name", providerName]
		implCN = ["implementationClassName", "oracle.jdbc.pool.OracleConnectionPoolDataSource"]
		classpath = ["classpath", oracle_home + "/jdbc/lib/ojdbc14.jar"]
		jdbcattrs = [jdbc_name, implCN, classpath]
	else :
		print "Unknown JDBC provider. Please try to re-configure it."
		sys.exit(1)
	
	jdbcProviderName = AdminConfig.create("JDBCProvider", node, jdbcattrs )
	print "The JDBCProvider " + jdbcProviderName + " successfully created.\n"	 
else : 	
	print "The JDBC Provider " + jdbcProviderName + " already exists.\n"	 
	
dbnameAttr = [["name", "databaseName"], ["value", 'martini'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
urlAttr = [["name", "URL"], ["value", 'jdbc:oracle:thin:@POSEIDON:1521:BM1'], ["type", "java.lang.String"], ["description", "This is a required property"]]	
dsListname = ["name", "${artifactId}.clickstream"]
jndiListName = ["jndiName", "jdbc/${artifactId}.clickstream"]
#userAttr = [["name", "user"], ["value", 'bm101_CLICKSTREAM'], ["type", "java.lang.String"]] 
#passwordAttr = [["name", "password"], ["value", 'martini'], ["type", "java.lang.String"]]
# newprops = [userAttr, passwordAttr, dbnameAttr]
newprops = [dbnameAttr, urlAttr]
psAttr = ["propertySet", [["resourceProperties", newprops]]]

# create authentication data
print "Creating JAASAuthData object for component-managed authentication, user bm101_CLICKSTREAM ..." 
try:
	aliasName = "BMJAASAuthData_bm101_CLICKSTREAM"
	sec = AdminConfig.getid("/Cell:" + bms_cell + "/Security:/")
	aliasAttr = ["alias", aliasName]
	descAttr = ["description", "Authentication information when component-managed"]
	useridAttr = ["userId", "bm101_CLICKSTREAM"]
	passwordAttr = ["password", "martini"]
	attrs = []
	attrs.append(aliasAttr)
	attrs.append(descAttr)
	attrs.append(useridAttr)
	attrs.append(passwordAttr)
	appauthdata = AdminConfig.create("JAASAuthData", sec, attrs) 
	print "done."
except:
	# note: if I catch exception here, the script interrupts... crap
	print "An exception occured,  probably the authentication data already exists."
	
authAlias = ["authDataAlias", aliasName]
dsAttrs = [dsListname, jndiListName, dshelper, authAlias, psAttr]



# create the datasources
print "Creating DataSource ${artifactId}.clickstream ...  "
availableDsrc = ""
availableDatasources = AdminTask.listDatasources("-scope Node=" + bms_node)
if len(availableDatasources) > 0:
	dSrcLen = len(availableDatasources) - 1
	dSrcList = availableDatasources.split()
	for nextDatasource in dSrcList:
		if  (nextDatasource.startswith("${artifactId}.clickstream")):
			availableDsrc = nextDatasource            

if (availableDsrc == ""):
	newds = AdminConfig.create('DataSource', jdbcProviderName, dsAttrs)
	initialCapacity = '10'
	maxCapacity = '20'
	cpAttrs = []
	if (initialCapacity != '' and maxCapacity != ''):
		minConnectionsAttr = ["minConnections", initialCapacity]
		maxConnectionsAttr = ["maxConnections", maxCapacity]
		cpAttrs = [minConnectionsAttr, maxConnectionsAttr]
		
	AdminConfig.create('ConnectionPool', newds, cpAttrs)
	print "done."	
else : 
	print "The datasource " + availableDsrc + " already exists.\n"	 

   
# use this script to set the custom variable
print "Setting the invokeFiltersCompatibility variable ..."
var = "com.ibm.ws.webcontainer.invokefilterscompatibility"
server = AdminConfig.getid("/Cell/" + bms_cell + "/Node/" + bms_node \
	+ "/Server/" + bmsserver + "/")
serverWebContainer = AdminConfig.list("WebContainer", server)
attrs = [["name", var], \
				["value", "true"], \
				["description", "compatibility mode"]]
try: 
	AdminConfig.create("Property", serverWebContainer, attrs)
except: 
	print "The variable com.ibm.ws.webcontainer.invokefilterscompatibility already set."
print "done."


AdminConfig.save()
sys.exit(0)

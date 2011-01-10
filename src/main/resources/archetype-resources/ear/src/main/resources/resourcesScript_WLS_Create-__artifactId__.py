from os import environ
wls_domain="/home/yannick/apps/bea/user_projects/domains/BlueMartiniDev"
serverName="AdminServer"
readDomain(wls_domain)

cd('/')

try:
   create('com.bluemartini.dbpool.${artifactId}.eac','JDBCSystemResource')
except  Exception,udt:
   print "The system resource already exist. Trying to re-configure it.\n"

cd("JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.eac/JdbcResource/com.bluemartini.dbpool.${artifactId}.eac")
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', 'oracle.jdbc.driver.OracleDriver')
set('URL','jdbc:oracle:thin:@triton:1521:BM')
set('PasswordEncrypted', 'martini')
create('myProps','Properties')

cd('Properties/NO_NAME_0')

try:
    create('user','Property')
except  Exception,udt:
   print "The property \"user\" already exist. Trying to re-configure it.\n"

cd('Property/user')
cmo.setValue('martini_eac')

cd('../..')

try:
    create('protocol','Property')
except  Exception,udt:
   print "The property \"protocol\" already exist. Trying to re-configure it.\n"

cd('Property/protocol')
cmo.setValue('')

cd('../..')
sVendor = "oracle"
if sVendor == "microsoft":
    try:
        create('CodePageOverride','Property')
    except  Exception,udt:
        print "The property \"CodePageOverride\" already exist. Trying to re-configure it.\n"
    cd('Property/CodePageOverride')
    cmo.setValue('Cp1252')

cd('/JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.eac/JdbcResource/com.bluemartini.dbpool.${artifactId}.eac')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
value = "10"
if value != "" : set('InitialCapacity',int(value))

value = "20"
if value != "" : set('MaxCapacity',int(value))

value = "5"
if value != "" : set('CapacityIncrement',int(value))

value = "15"
if value != "" : set('ShrinkFrequencySeconds',int(value))

value = "TWIST"
if value != "" : set('TestTableName',value)

set('RemoveInfectedConnections',false)

assign('JDBCSystemResource', "com.bluemartini.dbpool.${artifactId}.eac", 'Target', serverName)

cd('/')

try:
   create('com.bluemartini.dbpool.${artifactId}.store','JDBCSystemResource')
except  Exception,udt:
   print "The system resource already exist. Trying to re-configure it.\n"

cd("JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.store/JdbcResource/com.bluemartini.dbpool.${artifactId}.store")
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', 'oracle.jdbc.driver.OracleDriver')
set('URL','jdbc:oracle:thin:@triton:1521:BM')
set('PasswordEncrypted', 'martini')
create('myProps','Properties')

cd('Properties/NO_NAME_0')

try:
    create('user','Property')
except  Exception,udt:
   print "The property \"user\" already exist. Trying to re-configure it.\n"

cd('Property/user')
cmo.setValue('martini_STORE')

cd('../..')

try:
    create('protocol','Property')
except  Exception,udt:
   print "The property \"protocol\" already exist. Trying to re-configure it.\n"

cd('Property/protocol')
cmo.setValue('')

cd('../..')
sVendor = "oracle"
if sVendor == "microsoft":
    try:
        create('CodePageOverride','Property')
    except  Exception,udt:
        print "The property \"CodePageOverride\" already exist. Trying to re-configure it.\n"
    cd('Property/CodePageOverride')
    cmo.setValue('Cp1252')

cd('/JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.store/JdbcResource/com.bluemartini.dbpool.${artifactId}.store')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
value = "10"
if value != "" : set('InitialCapacity',int(value))

value = "20"
if value != "" : set('MaxCapacity',int(value))

value = "5"
if value != "" : set('CapacityIncrement',int(value))

value = "15"
if value != "" : set('ShrinkFrequencySeconds',int(value))

value = "TWIST"
if value != "" : set('TestTableName',value)

set('RemoveInfectedConnections',false)

assign('JDBCSystemResource', "com.bluemartini.dbpool.${artifactId}.store", 'Target', serverName)

cd('/')

try:
   create('com.bluemartini.dbpool.${artifactId}.main','JDBCSystemResource')
except  Exception,udt:
   print "The system resource already exist. Trying to re-configure it.\n"

cd("JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.main/JdbcResource/com.bluemartini.dbpool.${artifactId}.main")
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', 'oracle.jdbc.driver.OracleDriver')
set('URL','jdbc:oracle:thin:@triton:1521:BM')
set('PasswordEncrypted', 'martini')
create('myProps','Properties')

cd('Properties/NO_NAME_0')

try:
    create('user','Property')
except  Exception,udt:
   print "The property \"user\" already exist. Trying to re-configure it.\n"

cd('Property/user')
cmo.setValue('martini_MAIN')

cd('../..')

try:
    create('protocol','Property')
except  Exception,udt:
   print "The property \"protocol\" already exist. Trying to re-configure it.\n"

cd('Property/protocol')
cmo.setValue('')

cd('../..')
sVendor = "oracle"
if sVendor == "microsoft":
    try:
        create('CodePageOverride','Property')
    except  Exception,udt:
        print "The property \"CodePageOverride\" already exist. Trying to re-configure it.\n"
    cd('Property/CodePageOverride')
    cmo.setValue('Cp1252')

cd('/JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.main/JdbcResource/com.bluemartini.dbpool.${artifactId}.main')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
value = "10"
if value != "" : set('InitialCapacity',int(value))

value = "20"
if value != "" : set('MaxCapacity',int(value))

value = "5"
if value != "" : set('CapacityIncrement',int(value))

value = "15"
if value != "" : set('ShrinkFrequencySeconds',int(value))

value = "TWIST"
if value != "" : set('TestTableName',value)

set('RemoveInfectedConnections',false)

assign('JDBCSystemResource', "com.bluemartini.dbpool.${artifactId}.main", 'Target', serverName)

cd('/')

try:
   create('com.bluemartini.dbpool.${artifactId}.clickstream','JDBCSystemResource')
except  Exception,udt:
   print "The system resource already exist. Trying to re-configure it.\n"

cd("JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.clickstream/JdbcResource/com.bluemartini.dbpool.${artifactId}.clickstream")
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', 'oracle.jdbc.driver.OracleDriver')
set('URL','jdbc:oracle:thin:@triton:1521:BM')
set('PasswordEncrypted', 'martini')
create('myProps','Properties')

cd('Properties/NO_NAME_0')

try:
    create('user','Property')
except  Exception,udt:
   print "The property \"user\" already exist. Trying to re-configure it.\n"

cd('Property/user')
cmo.setValue('martini_CLICKSTREAM')

cd('../..')

try:
    create('protocol','Property')
except  Exception,udt:
   print "The property \"protocol\" already exist. Trying to re-configure it.\n"

cd('Property/protocol')
cmo.setValue('')

cd('../..')
sVendor = "oracle"
if sVendor == "microsoft":
    try:
        create('CodePageOverride','Property')
    except  Exception,udt:
        print "The property \"CodePageOverride\" already exist. Trying to re-configure it.\n"
    cd('Property/CodePageOverride')
    cmo.setValue('Cp1252')

cd('/JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.clickstream/JdbcResource/com.bluemartini.dbpool.${artifactId}.clickstream')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
value = "10"
if value != "" : set('InitialCapacity',int(value))

value = "20"
if value != "" : set('MaxCapacity',int(value))

value = "5"
if value != "" : set('CapacityIncrement',int(value))

value = "15"
if value != "" : set('ShrinkFrequencySeconds',int(value))

value = "TWIST"
if value != "" : set('TestTableName',value)

set('RemoveInfectedConnections',false)

assign('JDBCSystemResource', "com.bluemartini.dbpool.${artifactId}.clickstream", 'Target', serverName)

cd('/')

try:
   create('com.bluemartini.dbpool.${artifactId}.search','JDBCSystemResource')
except  Exception,udt:
   print "The system resource already exist. Trying to re-configure it.\n"

cd("JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.search/JdbcResource/com.bluemartini.dbpool.${artifactId}.search")
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', 'jdbc.searchserver.SSDriver')
set('URL','jdbc:searchserver:SearchServer_5.4')
set('PasswordEncrypted', 'martini')
create('myProps','Properties')

cd('Properties/NO_NAME_0')

try:
    create('user','Property')
except  Exception,udt:
   print "The property \"user\" already exist. Trying to re-configure it.\n"

cd('Property/user')
cmo.setValue('martini')

cd('../..')

try:
    create('protocol','Property')
except  Exception,udt:
   print "The property \"protocol\" already exist. Trying to re-configure it.\n"

cd('Property/protocol')
cmo.setValue('')

cd('../..')
sVendor = "fulcrum"
if sVendor == "microsoft":
    try:
        create('CodePageOverride','Property')
    except  Exception,udt:
        print "The property \"CodePageOverride\" already exist. Trying to re-configure it.\n"
    cd('Property/CodePageOverride')
    cmo.setValue('')

cd('/JDBCSystemResource/com.bluemartini.dbpool.${artifactId}.search/JdbcResource/com.bluemartini.dbpool.${artifactId}.search')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
value = "2"
if value != "" : set('InitialCapacity',int(value))

value = "20"
if value != "" : set('MaxCapacity',int(value))

value = "5"
if value != "" : set('CapacityIncrement',int(value))

value = "15"
if value != "" : set('ShrinkFrequencySeconds',int(value))

value = ""
if value != "" : set('TestTableName',value)

set('RemoveInfectedConnections',false)

assign('JDBCSystemResource', "com.bluemartini.dbpool.${artifactId}.search", 'Target', serverName)

updateDomain()
closeDomain()



from os import environ
wls_domain="/home/yannick/apps/bea/user_projects/domains/BlueMartiniDev"
serverName="AdminServer"
readDomain(wls_domain)

cd('/')

try:
   delete('com.bluemartini.dbpool.${artifactId}.main','JDBCSystemResource')
except  Exception,udt:
   print "com.bluemartini.dbpool.${artifactId}.main doesn't exist.\n"

try:
   delete('com.bluemartini.dbpool.${artifactId}.search','JDBCSystemResource')
except  Exception,udt:
   print "com.bluemartini.dbpool.${artifactId}.search doesn't exist.\n"

try:
   delete('com.bluemartini.dbpool.${artifactId}.store','JDBCSystemResource')
except  Exception,udt:
   print "com.bluemartini.dbpool.${artifactId}.store doesn't exist.\n"
   
try:
   delete('com.bluemartini.dbpool.${artifactId}.eac','JDBCSystemResource')
except  Exception,udt:
   print "com.bluemartini.dbpool.${artifactId}.eac doesn't exist.\n"
   
try:
   delete('com.bluemartini.dbpool.${artifactId}.clickstream','JDBCSystemResource')
except  Exception,udt:
   print "com.bluemartini.dbpool.${artifactId}.clickstream doesn't exist.\n"

updateDomain()
closeDomain()
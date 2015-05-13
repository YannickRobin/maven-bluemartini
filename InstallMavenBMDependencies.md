Blue Martini proprietary files (jar archives and configuration files) cannot be shared in an open-source repository. So before using `maven-bluemartini`, install files from `bms-commerce-10.1.1.X.jar` to your Maven repository as described below.<br />

## Install BM jar archives ##

```
set BMS_HOME=<your bms path>

call mvn install:install-file -Dfile=%BMS_HOME%\core\classes\martini.jar -DgroupId=com.bluemartini.core -DartifactId=martini -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\eac\classes\eac.jar -DgroupId=com.bluemartini.eac -DartifactId=eac -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\isell\classes\isell.jar -DgroupId=com.bluemartini.isell -DartifactId=isell -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\ant\lib\ant-martini.jar -DgroupId=com.bluemartini.ant -DartifactId=ant-martini -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\AdvisorSvr.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=AdvisorSvr -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\AdvCommon.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=AdvCommon -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\Advisor.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=Advisor -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\adb55sync.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=adb55sync -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\kdCalc.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=kdCalc -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\log4j-1.2.13.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=log4j-1.2.13 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\commons-httpclient-3.0.1.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=commons-httpclient-3.0.1 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\DSadmin.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=DSadmin -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\xmlrpc-1.1.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=xmlrpc-1.1 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\commons-logging.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=commons-logging -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\akamaizer.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=akamaizer -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\cybersource.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=cybersource -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\oromatcher2.0.2.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=oromatcher2.0.2 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\ssjdbc50.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=ssjdbc50 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\activation.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=activation -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\mail.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=mail -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\jgl3.1.0.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=jgl3.1.0 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\sqljdbc.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=sqljdbc -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\bcmail-jdk14-136.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=bcmail-jdk14-136 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\bcprov-jdk14-136.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=bcprov-jdk14-136 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\commons-codec-1.2.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=commons-codec-1.2 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\drools-compiler-4.0.7.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=drools-compiler-4.0.7 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\drools-core-4.0.7-JBRULES-1817.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=drools-core-4.0.7-JBRULES-1817 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\drools-core-4.0.7.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=drools-core-4.0.7 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\janino-2.5.10.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=janino-2.5.10 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\mvel-1.3.1-java1.4.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=mvel-1.3.1-java1.4 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\antlr-runtime-3.0.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=antlr-runtime-3.0 -Dversion=10.1.1.0 -Dpackaging=jar
call mvn install:install-file -Dfile=%BMS_HOME%\thirdparty\classes\javassist.jar -DgroupId=com.bluemartini.thirdparty -DartifactId=javassist -Dversion=10.1.1.0 -Dpackaging=jar
```

## Install DNA configuration files ##

`maven-bluemartini` is able to load DNA configuration files inside jar archive. This way, it is possible to define it as Maven dependencies.

  * Create and install `martini-config.jar`:
    * Create the following directory structure `martini-config\META-INF\bluemartini\core` in a temporary folder
    * Copy `%BMS_HOME%\core\config\*.*` to `martini-config\META-INF\bluemartini\core`. _Note it can be a fresh Blue Martini installation but you have to ensure you have run `bms dbinit`._
    * Execute the following commands:
```
  > cd martini-config
  > jar cvf martini-config.jar *
  > mvn install:install-file -Dfile=martini-config.jar -DgroupId=com.bluemartini.core -DartifactId=martini-config -Dversion=10.1.1.0 -Dpackaging=jar
```
  * Create and install `eac-config.jar`:
    * Create the following directory structure `eac-config\META-INF\bluemartini\eac` in a temporary folder
    * Copy `%BMS_HOME%\eac\config\eac` to `eac-config\META-INF\bluemartini\eac`
    * Execute the following commands:
```
  > cd eac-config
  > jar cvf eac-config.jar *
  > mvn install:install-file -Dfile=eac-config.jar -DgroupId=com.bluemartini.eac -DartifactId=eac-config -Dversion=10.1.1.0 -Dpackaging=jar
```

## Internal repository manager ##
For team development, we recommend you use an internal repository manager and replace `install` command by `deploy`.
<br />
i.e.:`mvn deploy:deploy-file -Dfile=$BMS_HOME/core/classes/martini.jar -DgroupId=com.bluemartini.core -DartifactId=martini -Dversion=10.1.1.0 -Dpackaging=jar -Durl=http://<my repository url>`
<br />
If you use `Nexus`:
  * Click on `Browse Repositories,`
  * Right click on the `3rd Party` repository and choose `Upload Artifact.`
  * Select `Gave parameters`
  * In the `Upload Artifact` form, choose the JAR to upload, then populate the `group id`, `artifact id`, `version`, and other fields.
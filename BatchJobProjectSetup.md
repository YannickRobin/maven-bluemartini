This document describes the steps to create a project for BM batch jobs using [maven-bluemartini](http://code.google.com/p/maven-bluemartini).

# Prerequisite #

## Maven installation ##
  * Download and install `Maven 3`
  * Add `MAVEN_HOME` variable to your system
  * Add `<MAVEN_HOME>\bin` to your `PATH`

## Install _maven-bluemartini_ dependencies ##

See [InstallMavenBMDependencies](InstallMavenBMDependencies.md).

# Generate project #

  * From Eclipse workspace, execute the following commands:
```
  > mvn archetype:generate -B -DarchetypeGroupId=com.bluemartini.archetypes -DarchetypeArtifactId=bms-archetype-batch -DarchetypeVersion=1.0.0 -DarchetypeRepository=http://maven-bluemartini.googlecode.com/svn/repository/ -DgroupId=com.mycompany.myproject -DartifactId=myproject -Dversion=1.0.0-SNAPSHOT
  > rename myproject myproject-batch
  > cd myproject-batch
  > mvn assembly:assembly
```

# Set up Eclipse project #

  * Install Eclipse
  * Install [M2Eclipse](http://m2eclipse.sonatype.org) (Eclipse update site URL: http://m2eclipse.sonatype.org/sites/m2e)
  * Install M2Eclipse extras (Eclipse update site URL: http://m2eclipse.sonatype.org/sites/m2e-extras)
  * Change Eclipse default compiler compliance level: `Windows > Preferences > Java > Compiler > Compiler compliance level: 1.5`
  * From `myProject-batch` folder, execute the following command to create the Eclipse project: `mvn eclipse:eclipse`
  * Import the project into Eclipse: `File > Import... > General > Existing projects into Workspace`
  * Generate Eclipse configuration files: `Right click on each projects > Maven > Enable Dependency management`

# Run batch job #

During development, you have two options to run batch jobs:
  * By command line after build & deploy
  * Inside Eclipse

## Run by script ##

  * Copy `build_local.properties` to `build.properties` and update bms home
  * From Eclipse, select `deploy.xml`
  * Right click and select `Run As > Ant Build`
  * From BMS home, execute the following command:
```
  > bms myproject testbatch
```

## Run inside Eclipse ##

  * In Eclipse, select the class you want to run
  * Right click, select `Run As > Run Configurations`
![http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch1.png](http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch1.png)<br />
  * Add arguments:
    * -c ${project\_loc}/src/main/bms/myproject/config/testbatchdb.appconfig.dna
    * -env BPADev
![http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch2.png](http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch2.png)<br />
  * Add `weblogic.jar` to the classpath
![http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch3.png](http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch3.png)<br />
  * Add environment variables:
    * BMS\_APPSERVER -> com.bluemartini.thirdparty.weblogic.WebLogicAppServer
    * BMS\_HOME -> /home/yannick/apps/bm101
    * BMS\_CONFIG\_HOME -> /home/yannick/apps/bm101
    * BMS\_CONFIG\_DIR -> core/config
    * BMS\_ENV -> /home/yannick/apps/bm101/core/config/env\_wls\_dev.dna
    * BMS\_SECURITY\_DIR -> /home/yannick/apps/bm101/core/config/appcommon
    * BMS\_EAC\_SERVER -> localhost
    * BMS\_EAC\_PORT -> 7011
![http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch4.png](http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch4.png)<br />
  * Here should be the result:
![http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch5.png](http://maven-bluemartini.googlecode.com/svn/trunk/bms-archetype-ear/wiki/images/batch5.png)<br />
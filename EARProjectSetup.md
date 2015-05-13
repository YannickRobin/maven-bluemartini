# Prerequisite #

## Maven installation ##
  * Download and install `Maven 3`
  * Add `MAVEN_HOME` variable to your system
  * Add `<MAVEN_HOME>\bin` to your `PATH`

## Install _maven-bluemartini_ dependencies ##

See [InstallMavenBMDependencies](InstallMavenBMDependencies.md).

# Generate EAR project #

From Eclipse workspace, execute the following commands:
```
  > mvn archetype:generate -B -DarchetypeGroupId=com.bluemartini.archetypes -DarchetypeArtifactId=bms-archetype-ear -DarchetypeVersion=1.0.0 -DarchetypeRepository=http://maven-bluemartini.googlecode.com/svn/repository/ -DgroupId=com.mycompany.myproject -DartifactId=myProject-website -Dversion=1.0.0-SNAPSHOT
  > cd myProject-website
  > mvn install
```

At this step, Maven has created for you a ready-to-deploy EAR file!

# Eclipse project setup #

  * Install Eclipse
  * Install [M2Eclipse](http://m2eclipse.sonatype.org) (Eclipse update site URL: http://m2eclipse.sonatype.org/sites/m2e)
  * Install M2Eclipse extras (Eclipse update site URL: http://m2eclipse.sonatype.org/sites/m2e-extras)
  * Change Eclipse default compiler compliance level: `Windows > Preferences > Java > Compiler > Compiler compliance level: 1.5`
  * From `myProject-website` folder, execute the following command to create the Eclipse project: `mvn eclipse:eclipse`
  * Import the project into Eclipse: `File > Import... > Existing projects into Workspace`

# Eclipse WTP setup #

To deploy/run the application inside Eclipse using WTP, see [Eclipse WTP setup](EclipseWTPSetup.md).
# Continuous Integration FAQ #
_Documented with Maven 3.0, Eclipse Helios 3.6.1, Sonar 2.4.1 (Code quality tool), Selenium Server 1.0.3 (Web test automation platform), Hudson 1.386 (Continuous Integration System), Nexus 1.8.0.1 (Repository manager)._ <br />

Please note, this document is not specific to `maven-bluemartini` and can be used for any Maven project.<br />



## How developers can retrieve and build a Maven project without Eclipse? ##
  * Install SVN client
    * Windows: Slik Subversion from http://www.sliksvn.com/en/download
    * Ubuntu: sudo apt-get install subversion
  * Open a command line in the Eclipse workspace and execute the following commands:
    * `svn checkout https://<host>/svn/trunk/<project> <project>`
    * `cd <project>`
  * Get the latest code: `svn checkout https://<host>/svn/trunk/<project> <project>`
  * `cd <project>`
  * Generate the distribution file with the following command: `mvn assembly:assembly`

## How developers can retrieve and build a Maven project with Eclipse? ##
  * Install [M2Eclipse](http://m2eclipse.sonatype.org) (Eclipse update site URL: http://m2eclipse.sonatype.org/sites/m2e)
  * Install JavaHL libraries
    * Windows: Slik Subversion from http://www.sliksvn.com/en/download
    * Ubuntu: `sudo apt-get install libsvn-java`
  * Install SubEclipse plugin (Eclipse update site URL: http://subclipse.tigris.org/update_1.6.x)
  * In Eclipse, `File > New > Other > Maven > Checkout Maven Projects from SCM`
  * SCM URL: `scm:svn:https://maven-bluemartini.googlecode.com/svn/trunk/maven-bluemartini`
  * Generate compilation classpath: Right click on the project ` > Maven > Enable Dependency management`

## How to integrate with Eclipse WTP? ##
See [http://code.google.com/p/maven-bluemartini/wiki/EclipseWTPSetup](EclipseWTPSetup.md).

## How to generate a binary distribution? ##

  * Add the following section to your POM:
```
  <build>
    <plugins>
      <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <configuration>
          <descriptor>src/main/assembly/bin.xml</descriptor>
        </configuration>
      </plugin>
    </plugins>
  </build>
```
  * Create the file `src/main/assembly/bin.xml` and indicate the way to package your application:
```
<assembly>
  <id>bin</id>
  <formats>
    <format>zip</format>
  </formats>
  <includeBaseDirectory>false</includeBaseDirectory>  
  <fileSets>
    <fileSet>
      <directory>src/main/config</directory>
      <outputDirectory></outputDirectory>      
    </fileSet>    
    <fileSet>
      <directory>target</directory>
      <outputDirectory>core/classes</outputDirectory>
      <includes>
        <include>maven-bluemartini-${project.version}.jar</include>
      </includes>
    </fileSet>
  </fileSets>
</assembly>
```
  * Run `assembly:assembly`

## How to release from SVN? ##
  * Install SVN client
    * Windows: Slik Subversion from http://www.sliksvn.com/en/download
    * Ubuntu: `sudo apt-get install subversion`
  * Ensure `svn` command works. It must be in your PATH.
  * Ensure you have correct SCM information in your POM. Here is the format:
```
  <scm>
    <connection>scm:svn:https://maven-bluemartini.googlecode.com/svn/trunk/maven-bluemartini</connection>
    <developerConnection>scm:svn:https://maven-bluemartini.googlecode.com/svn/trunk/maven-bluemartini</developerConnection>
    <url>http://code.google.com/p/maven-bluemartini/source/browse/</url>
  </scm>
```
  * If you want to execute the assembly goal when you release, add:
```
  <plugin>
    <artifactId>maven-release-plugin</artifactId>
    <version>2.1</version>
    <configuration>
      <!--
        During release:perform, enable the "release" profile
       -->
      <releaseProfiles>release</releaseProfiles>
      <goals>deploy assembly:assembly</goals>
    </configuration>
  </plugin>
```
  * Add a repository to store release artifact
```
  <distributionManagement>
	<repository>
		<id>MyRepositoryID</id>
		<name>My Repository Name</name>
		<url>file:///d:/MyRemoteMavenRepository</url>
	</repository>
  </distributionManagement>
```
  * Commit or revert all your changes
  * Run `mvn -Dusername=[svnusername] -Dpassword=[svnpassword] release:prepare` to prepare the release. It will:
    * Update the POM for the specified release version (i.e.: 1.0.1)
    * Tag SVN for the specified release version (i.e.: maven-bluemartini-1.0.1)
    * Update the POM for the new development version (i.e.: 1.0.1-SNAPSHOT)
    * Commit the POM
  * If you want to rollback
    * `mvn release:rollback`
    * use `svn delete`, i.e.: `svn delete https://maven-bluemartini.googlecode.com/svn/tags/maven-bluemartini-1.0.0 -m "Removing obsolete tag"`
  * Run `mvn release:perform` to create the artifact related to the specified release. If the version you want to release is old, indicate explicitly the tag you want to use: `mvn release:perform -DconnectionUrl=scm:svn:https://maven-bluemartini.googlecode.com/svn/tags/maven-bluemartini-1.0.1`
  * The bin indicated generated by the assembly goal can be find here: `<project-name>/target/checkout/target`

## How to integrate with Nexus? ##

  * Install Nexus
  * Start Nexus: `<NEXUS_HOME>/bin/jsw/<OS>/nexus start`
  * Check Nexus is running: http://localhost:8081/nexus (`admin`/`admin123`)
  * Add `~.m2/settings.xml` (please note for Hudson, the Maven home is `/var/lib/hudson/.m2`):
```
<settings>
  <mirrors>
    <mirror>
      <id>nexus</id>
      <mirrorOf>*</mirrorOf>
      <url>http://localhost:8081/nexus/content/groups/public</url>
    </mirror>
  </mirrors>
  <profiles>
    <profile>
      <id>nexus</id>
      <!--Enable snapshots for the built in central repo to direct -->
      <!--all requests to nexus via the mirror -->
      <repositories>
        <repository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
  <activeProfiles>
    <!--make the profile active all the time -->
    <activeProfile>nexus</activeProfile>
  </activeProfiles>
</settings>
```

## How to generate Maven site? ##

  * Create `src/site/site.xml`, here is an example:

```
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/DECORATION/1.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/DECORATION/1.0.0 http://maven.apache.org/xsd/decoration-1.0.0.xsd">
  <body>

    <menu name="Overview">
      <item name="Introduction" href="index.html"/>
      <item name="Goals" href="plugin-info.html"/>
      <item name="Usage" href="usage.html"/>
      <item name="FAQ" href="faq.html"/>
      <item name="Migrate" href="migrate.html"/>
    </menu> 
    <menu name="Configuration">
      <item name="Internationalization" href="i18n.html"/>
    </menu>

  </body>
</project>
```

  * Create `src/site/apt/index.apt`, here is an example:
```
Hello world
```
  * Execute `mvn site` to generate the site
  * Execute `mvn site:run` to start the server
  * Go to [http://localhost:8080](http://localhost:8080)


## How to generate Maven reports? ##

  * Add and configure maven-site-plugin to the POM
```
    <build>
        <plugins>
    		<plugin>
    			<groupId>org.apache.maven.plugins</groupId>
    			<artifactId>maven-site-plugin</artifactId>
    			<version>3.0-beta-3</version>
				<configuration>
                                          <reportPlugins>
					       <!-- Add reports you want to generate here -->
                                          </reportPlugins>		  
				</configuration>
    		</plugin>	
        </plugins>
    </build>
```
  * Add reports you want to generate in the `reportPlugins` section:
    * For project info report:
```
                                                <!-- Generate project info report -->
                                                <plugin>
                                                  <groupId>org.apache.maven.plugins</groupId>
                                                  <artifactId>maven-project-info-reports-plugin</artifactId>
                                                  <version>2.2</version>
                                                  <reports>
                                                        <report>cim</report>
                                                        <report>issue-tracking</report>
                                                        <!--report>dependencies</report-->
                                                  </reports>
                                                </plugin>
```
    * For change report:
```
                                                <!-- Generate 'Changes Report' from src/changes/changes.xml -->
                                                <plugin>
                                                        <groupId>org.apache.maven.plugins</groupId>
                                                        <artifactId>maven-changes-plugin</artifactId>
                                                        <version>2.3</version>
                                                        <reportSets>
                                                                <reportSet>
                                                                        <reports>
                                                                                <report>changes-report</report>
                                                                        </reports>
                                                                </reportSet>
                                                        </reportSets>
                                                </plugin>
```
    * For JXR (Source code as HTML) report:
```
                                                <!-- JXR - Source code as HTML --> 
                                                <plugin>
                                                        <groupId>org.apache.maven.plugins</groupId>
                                                        <artifactId>maven-jxr-plugin</artifactId>
                                                        <version>2.1</version>
                                                        <configuration>
                                                                <inputEncoding>utf-8</inputEncoding>
                                                                <outputEncoding>utf-8</outputEncoding>
                                                        </configuration>
                                                </plugin>
```
    * For JavaDoc report:
```
                                                <!-- JavaDoc - API-documentation -->
                                                <plugin>
                                                  <groupId>org.apache.maven.plugins</groupId>
                                                  <artifactId>maven-javadoc-plugin</artifactId>
                                                        <version>2.6.1</version>
                                                        <configuration>
                                                                <show>public</show>
                                                                <charset>utf-8</charset>
                                                                <docencoding>utf-8</docencoding>
                                                                <encoding>utf-8</encoding>    
                                                        </configuration>
                                                </plugin>
```
    * For Surefire (JUnit) report:
```
                                                <!-- Surefire - JUnit testing-->
                                                <plugin>
                                                        <groupId>org.apache.maven.plugins</groupId>
                                                        <artifactId>maven-surefire-report-plugin</artifactId>
                                                        <version>2.4.3</version>
                                                        <configuration>
                                                                <!-- Required to properly link JXR -->
                                                                <xrefLocation>${project.reporting.outputDirectory}/../xref-test</xrefLocation>
                                                        </configuration>
                                                </plugin>
```
    * For JDepend (Package dependencies) report:
```
                                                <!-- JDepend - Package dependencies -->
                                                <plugin>
                                                        <groupId>org.codehaus.mojo</groupId>
                                                        <artifactId>jdepend-maven-plugin</artifactId>
                                                        <version>2.0-beta-2</version>
                                                </plugin>
```
    * For Cobertura (Code coverage) report:
```
                                                <!-- Cobertura - Test code coverage report. -->
                                                <plugin>
                                                        <groupId>org.codehaus.mojo</groupId>
                                                        <artifactId>cobertura-maven-plugin</artifactId>
                                                        <version>2.3</version>
                                                </plugin>
```
    * For PMD (Code analysis) report:
```
                                                <!-- PMD - Generate PMD and CPD reports using the PMD code analysis tool. -->
                                                <plugin>
                                                        <groupId>org.apache.maven.plugins</groupId>
                                                        <artifactId>maven-pmd-plugin</artifactId>
                                                        <version>2.4</version>
                                                        <configuration>
                                                                <linkXref>true</linkXref>
                                                                <!-- Required to properly link JXR -->
                                                                <xrefLocation>${project.reporting.outputDirectory}/../xref-test</xrefLocation>
                                                                <sourceEncoding>utf-8</sourceEncoding>
                                                                <aggregate>true</aggregate>
                                                                <targetJdk>1.5</targetJdk>
                                                        </configuration>
                                                </plugin>
```
    * For FindBugs (Code analysis) report:
```
                                                <!-- FindBugs - Finds potential bugs in your source code -->
                                                <plugin>
                                                        <groupId>org.codehaus.mojo</groupId>
                                                        <artifactId>findbugs-maven-plugin</artifactId>
                                                        <version>2.3.1</version>
                                                        <configuration>
                                                                <xmlOutput>true</xmlOutput>
                                                                <effort>Max</effort>
                                                        </configuration>
                                                </plugin>
```
    * For JavaNCSS (Source code metrics) report:
```
                                                <!-- JavaNCSS - Source code metrics -->
                                                <plugin>
                                                        <groupId>org.codehaus.mojo</groupId>
                                                        <artifactId>javancss-maven-plugin</artifactId>
                                                        <version>2.0</version>
                                                </plugin>
```
    * For TagList (Creates a list with TODO's) report:
```
                                                <!-- TagList - Creates a list with TODO:s etc -->
                                                <plugin>
                                                        <groupId>org.codehaus.mojo</groupId>
                                                        <artifactId>taglist-maven-plugin</artifactId>
                                                        <version>2.4</version>
                                                        <configuration>
                                                                <aggregate>true</aggregate>
                                                                <tags>
                                                                <tag>TODO</tag>
                                                                <tag>FIXME</tag>
                                                                <tag>@todo</tag>
                                                                </tags>
                                                        </configuration>    
                                                </plugin>
```


  * Edit `src/site/site.xml`, and add `<menu ref="reports"/>` in the menu section
  * Execute `mvn site` to generate the site

## How to generate Sonar reports? ##

  * Install Sonar
  * Start Sonar `<SONAR HOME>/bin/windows-x86-32/StartSonar.bat`
  * Default Sonar url is http://localhost:9000.
  * Run `mvn sonar:sonar`, if it doesn't work use `mvn org.codehaus.mojo:sonar-maven-plugin:2.0-beta-1:sonar`, see http://jira.codehaus.org/browse/SONAR-1851?page=com.atlassian.jira.plugin.system.issuetabpanels%3Aall-tabpanel#issue-tabs.

## How to run Selenium tests? ##

  * Install Selenium IDE
  * Record the test with Selenium IDE
  * Export the Selenium test `File > Export Test Case As... > Java(Junit)` to a JUnit test in `src/test/java/...`
  * In `setUp()` method, indicates your application url:
```
	public void setUp() throws Exception {
		setUp("http://localhost:8080/", "*chrome");
	}
```
  * Add the following section to your POM:
```
    <dependencies>
                ...
		<dependency>
			<groupId>org.seleniumhq.selenium</groupId>
			<artifactId>selenium</artifactId>
			<version>2.0a7</version>
			<type>jar</type>
			<scope>compile</scope>
		</dependency>
    </dependencies>
```
  * Install Selenium Server
  * Run `<SELENIUM-RC-HOME>/selenium-server-1.0.3/selenium-server.bat` to start Selenium Server
  * Run `mvn test`
  * If you generate Maven site or Sonar reports, results will appear in Surefire Report section

## How to do nightly build with Hudson/Jenkins? ##
  * Install Hudson
  * Go to http://localhost:8080/
  * Go to `Manage Hudson > Configure System`
  * Click `Add Maven`
    * Uncheck `Install automatically`
    * Name: `Maven 3`
    * MAVEN\_HOME: `your_maven_home`
  * Click `New Job`
Note `maven2 project` doesn't work with `Hudson 1.386` because of the following bug: http://issues.hudson-ci.org/browse/HUDSON-4988, please use `free-style software project`
  * For a `maven2 project`:
    * Indicate the job name
    * Select `Build a maven2 project`
    * Click Ok
    * Select `Subversion`
      * Repository URL: https://bmjmx.googlecode.com/svn/trunk/bmjmx
    * Select `Poll SCM` and add `@daily`
    * For `Goals and options`, indicate: `install`
    * Click `Save`
  * For a `free-style software project`:
    * Indicate the job name
    * Select `Free-style software project`
    * Click `Ok`
    * Select `Subversion`
      * Repository URL: https://bmjmx.googlecode.com/svn/trunk/bmjmx
    * Select `Poll SCM` and add `@daily`
    * Click `Add build step`
      * Maven Version: `Maven 3`
      * Goals: `install`
    * Click `Save`
Please note, the Hudson local repository is `/var/lib/hudson/.m2/repository`.

## How to by-pass FW? ##
  * Maven:
    * Edit `C:\Documents and Settings\<your user>\.m2\settings.xml` and add:
```
<settings>
  <proxies>
   <proxy>
      <active>true</active>
      <protocol>http</protocol>
      <host>myproxyhost</host>
      <port>myproxyport</port>
      <nonProxyHosts>www.google.com|*.somewhere.com</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```
  * Eclipse:
    * Go to `Window > Preferences > General > Network connections`
  * Hudson:
    * Go to `Manage Hudson > Plugin manager > Advanced > HTTP proxy`
  * Nexus:
    * Go to `Administration > Server > Nexus`
    * Check `Default HTTP Proxy Settings (optional)`
  * Svn:
    * Edit `~/.subversion/servers` and add:
```
[groups]
group1 = mysvnserver

[group1]
http-proxy-host = myproxyhost
http-proxy-port = myproxyport
# http-proxy-username = foo
# http-proxy-password = foo
http-timeout = 60
```
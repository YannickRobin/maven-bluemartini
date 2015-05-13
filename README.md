#Introduction

`maven-bluemartini` is Maven archetypes for Blue Martini projects:
* One for web application project: bms-archetype-ear
* One for batch job project: bms-archetype-batch


For a presentation with more details, see [maven-bluemartini on Slideshare](http://www.slideshare.net/yrob/mavenbluemartini-presentation).

#Goals

Here were the requirements for this project:
* Set up a new Blue Martini project in just 15 minutes^*^!
* Develop EAR without BM installation using Eclipse WTP
* Keep EAR build standard and as simple as possible (No BM scripts)
* Integrate BM projects with Continuous integration softwares and code quality tools
* Respect industry standards (new developer productive in Day One)

^*^ _Not including third-party software installation of course ;-)_

#Releases

* bms-archetype-ear-1.0.0: Tested with BM 10.1.1 and !WebLogic
* bms-archetype-batch-1.0.0: Tested with BM 10.1.1 and !WebLogic

#Getting started

##Web application

To create a web application project, see [EARProjectSetup EAR project setup]

##Batch job

To create a batch job project, see [BatchJobProjectSetup Batch job project setup].

##Continuous integration

After importing projects into a Software Configuration Management such as SVN, set up your Continuous Integration platform. Go to [ContinuousIntegrationFAQ Continuous Integration FAQ].

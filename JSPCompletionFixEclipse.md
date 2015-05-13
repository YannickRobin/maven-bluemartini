In Eclipse, JSP include with absolute path (i.e.: `<%@ include file="/include/inc_common.jsp" %>`) doesn't work because of the `/templates` folder.

## Installation steps ##

  * Replace `<eclipse>\plugins\org.eclipse.jst.jsp.core_1.2.110.v200809120122.jar\org\eclipse\jst\jsp\core\internal\util\FacetModuleCoreSupport.class` by the [fix](http://maven-bluemartini.googlecode.com/files/FacetModuleCoreSupport.class).
  * Restart Eclipse
This fix has been tested with Eclipse 3.4. Please note, it works for JSP compilation and auto-completion but not for browsing.
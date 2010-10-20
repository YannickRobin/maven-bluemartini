<%@ include file="include/inc_common.jspf" %>
<%
String sJSPMessage = "testJSP";
String sConfigMessage = BMMessages.getLabel("testMessage");
String sJavaMessage = com.bluemartini.wtp.Test.getMessage();
%>


<HTML>

<H1>Blue Martini 10.1 with Eclipse WTP works fine!</H1>

This is a JSP message: <B><%= sJSPMessage %></B>. <BR/>
This a configuration file message: <B><%= sConfigMessage %></B>. <BR/>
This a Java message: <B><%= sJavaMessage %></B>. <BR/>

<pre>
dnaFormData = <BR/>
<%= dnaFormData%>
</pre>
</HTML>
.. _s-netlogger:

**********************************************************************
Using Netlogger
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
========

One of the main goals for the FutureGrid performance group is to assess
the performance of the FutureGrid infrastructure. As such, both active
and passive performance measurements will be collected and analyzed.

This document describes the passive measurement collection method
using `Netlogger <http://acs.lbl.gov/NetLoggerWiki/index.php/NetLogger_Toolkit>`__.
For active measurements, please see the `Inca
document <https://wiki.futuregrid.org/index.php/Docs/Performance/IncaHowTo>`__.

Netlogger�is a tool for debugging and analyzing the performance of
complex distributed applications.�It is comprised of an API that allows
a user to instrument their application and tools for parsing existing
log files.�The overhead of using Netlogger is low and the Netlogger
website indicates you can generate up to "5000 events/second using the C
API, 500 events/second using the Java API, and 80 events/second using
the python API with negligible impact on your application. Netlogger
data is also easy to query and we provide a simple graphing interface
for FutureGrid. Netlogger has been in development since 1998 and is
used in several projects across the world. For more information, please
visit the `Netlogger
website <http://acs.lbl.gov/NetLoggerWiki/index.php/NetLogger_Toolkit>`__.

Within FutureGrid, we would like to collect coarse-grained usage and
performance data from each of the FutureGrid components.�This data will
help us determine the usage of a particular FutureGrid component and/or
help identify performance problems.�The data collected about each
component may vary from one another and each developer should decide the
relevant data to collect. Some samples are provided below

Scope
=====

This document applies to anyone developing or deploying FutureGrid
software components. We are also considering providing Netlogger as
part of a user's experiment but that is outside the scope of this
document and is tracked as Jira
task `FG-1017 <http://jira.futuregrid.org/browse/FG-1017>`__.

Deployment Information
======================

The Netlogger server is hosted at
`inca.futuregrid.org <http://inca.futuregrid.org>`__. �Both a TCP server
(provided by nl\_broker) and a AMQP server (provided by RabbitMQ v1.8.1)
are supported.�By default, we provide
`MongoDB <http://www.mongodb.org/>`__ as the default database backend
for FutureGrid components. �MongoDB is a schema-less database and will
not work well for components sending more than 1500 events at once. For
components needing a more scalable database, any relational database
backend can be setup to work with Netlogger. For example, the
`Pegasus <https://wiki.futuregrid.org/index.php/Docs/Performance/NetloggerHowTo#Pegasus>`__
use case below describes their relational database setup and schema.

Each FutureGrid component will be setup with their own MongoDB database
to avoid accidental deletes of each others data. To get setup with a
MongoDB database, send email to performance@futuregrid.org and specify a
prefix for your events (e.g., inca, pegasus, etc.) and the protocols you
want to use to publish data (AMQP, TCP).�We also have a test database
setup for those who are just getting started or want to try it out. To
use the test database, just prefix your events with "fgtest." (e.g.,
fgtest.expharness.usage). 

Using Netlogger
===============

Decide on Data to Collect
-------------------------

As mentioned above, we want to collect coarse-grained usage and
performance data from each of the FutureGrid components. For ideas of
what data to report, please see the `Performance group's architecture
document and use
cases <https://wiki.futuregrid.org/index.php/Docs/Performance/Internal>`__.

Data can be collected either by instrumenting the application itself or
writing a custom parser script to parse data from a log file. Data is
logged in the format of an event (i.e., timestamped). Each event can
contain one or more different values that you determine (e.g., number of
connections, number of errors, etc.).�E.g.,

| ts=2010-10-13T05:00:00Z event=inca.depot.usage level=INFO
numQueries=210 numConns=507 numInserts=297
|  ts=2010-10-13T06:00:00Z event=inca.depot.usage level=INFO
numQueries=250 numConns=547 numInserts=297

As mentioned above, the Netlogger website says you can generate up to
5000 events/second using the C API, 500 events/second using the Java
API, and 80 events/second using the python API with negligible impact on
your application. The other limitation is the backend database used for
archiving the events, which by default is MongoDB. MongoDB is a
schema-less database and each component by default is setup with a
single collection called "netlogger". A collection is equivalent to a
database table and is�formatted as a BSON document and stored as a
memory mapped file.�On inca.futuregrid.org, the size limit of a single
collection should be 2 GB. There is also the option to setup capped
(fixed size) collections which will automatically delete old records.
However, you cannot delete specific records from a collection once it
is capped. So, once your Netlogger data has stabilized, you can either
cap the collection yourself using the `mongo
console <https://wiki.futuregrid.org/index.php/Docs/Performance/NetloggerHowTo#MongoDB_console>`__:

::

    > use <database>
    > db.netlogger.convertToCapped( 1000000000 );

or email performance@futuregrid.org for help. The maximum size limit on
a capped collection is 1e9 bytes. Since we envision Netlogger to be
used primarily for capturing coarse-grained usage and performance data,
events should be generated on a minute, hour, or day schedule depending
on the variability of the data. If you think your data will require
more than one collection, just indicate that in your request to
performance@futuregrid.org.

Names for your events should have a common prefix (i.e., inca, nimbus,
eucalyptus) followed by a dot (.). This will help Netlogger direct
events to the correct MongoDB instance. You may want to then group
related events together. For example, Inca may group events related to
each of its components such as inca.depot.\*, inca.consumer.\*, or
inca.agent.\*. You might also want to identify the type of data you are
reporting by appending "usage" or "perf" (performance) to the event
name. If you would like to use the `default graphing
interface <https://wiki.futuregrid.org/index.php/Docs/Performance/NetloggerHowTo#mongo.jsp>`__
described below, you should ensure related values that you would like to
view on the same graph have the same timestamp either by supplying
multiple values within a single event like "inca.depot.usage" above or
by providing the same timestamp across multiple events with a single
value such as below.

ts=2010-10-13T05:00:00Z event=nimbus.usage.sierra level=INFO vms=72

ts=2010-10-13T05:00:00Z event=nimbus.usage.hotel level=INFO vms=152


Download API and Parse Tools
----------------------------

The Netlogger tools and APIs are available on inca.futuregrid.org in the
appropriate system directories or /opt/netlogger/default for Java.�If
you would like an account on this machine, send email to
performance@futuregrid.org.�Otherwise, you can download the APIs and
tools directly from the `NetLogger
website <http://acs.lbl.gov/NetLoggerWiki/index.php/Software>`__. 

APIs
are available in `C <http://inca.futuregrid.org/netlogger/c/>`__,
`Java <http://inca.futuregrid.org/netlogger/java/>`__,
`Perl <http://inca.futuregrid.org/netlogger/perl/>`__, and
`Python <http://inca.futuregrid.org/netlogger/python/>`__. We are using
the nightly build "trunk" version of Netlogger. 


Instrument and/or Parse
-----------------------

You have three options to log performance and/or usage data from your
application: 1) instrument the code directly, 2) use the nl\_parse tool
to parse specific log files, or 3) write your own parse tool. 

Instrument Code
~~~~~~~~~~~~~~~

This option is only available if you have access to the source code and
the source code is either written in C, Java, Perl, or Python.  The
advantage of this method is that once instrumented, your FutureGrid
component will be able to periodically send performance and usage data
to the FutureGrid Netlogger server directly.  The disadvantage is that
it will require more work up front to integrate the Netlogger API into
your component and will be harder to change once in deployment without
restarting the component. Note, there are both TCP and AMQP options for
Netlogger (for Java only AMQP is supported). Below shows an example of
using the RabbitMQ Java client library to send Netlogger message to the
server at inca.futuregrid.org and can optionally be downloaded as a
`tar.gz
file <http://inca.futuregrid.org/netlogger/NetloggerAmqpJava.tar.gz>`__.

::

    import com.rabbitmq.client.AMQP;
    import com.rabbitmq.client.Channel;
    import com.rabbitmq.client.Connection;
    import com.rabbitmq.client.ConnectionFactory;
    import gov.lbl.netlogger.LogMessage;
    import java.util.Calendar;

    public class NetloggerAmqpJava {
      public static void main(String[] args) {
        try {
          // Set up connection to AMQP server
          ConnectionFactory cfconn = new ConnectionFactory(); 
          cfconn.setHost("inca.futuregrid.org"); 
          Connection conn = cfconn.newConnection();
          Channel ch = conn.createChannel();

          // Create a NetLogger message
          String unique_event = "fgtest." + System.getProperty("user.name");
          int val = Calendar.getInstance().get(Calendar.SECOND);
          LogMessage nlmessage = new LogMessage(unique_event).add("val",val);
          System.out.println( nlmessage );

          // Publish it to the NetLogger Server
          ch.basicPublish("default_nl_ex", "default_nl_route", null, nlmessage.toString().getBytes());

          // Clean up
          ch.close();
          conn.close();
        } catch (Exception e) {
          System.err.println("Main thread caught exception: " + e);
          e.printStackTrace();
          System.exit(1);
        }
      }
    }

To compile, type

::

    javac -cp netlogger-java-trunk.jar:rabbitmq-client.jar NetloggerAmqpJava.java

To run, type

::

    java -cp .:netlogger-java-trunk.jar:rabbitmq-client.jar:commons-io-1.2.jar NetloggerAmqpJava

This will add one event fgtest.<userid> with val=<current secs>. For
example,

::

    ts=2010-10-18T09:32:40.820515Z event=fgtest.ssmallen val=40

Run a few more times and view the values using the graphing page below
(substitute 'ssmallen' with your username)

-  http://inca.futuregrid.org:8080/inca/jsp/mongo.jsp?event=fgtest.ssmallen&fields=val

You should see something like the following graph and can see the values
by moving the cursor over the line.

|MongoAMQP.png|

nl\_parse
~~~~~~~~~

The nl\_parse tool can be used to parse one or more log files and send
the data to the Netlogger server.�Use this option if your component
prints messages in Netlogger format (bp) or one of the other accepted
formats (see nl\_parse -l). Below shows an example that uses the Java
client library to print a Netlogger message to stdout and can optionally
be downloaded as a `tar.gz
file <http://inca.futuregrid.org/netlogger/NetloggerJava.tar.gz>`__.

::

    import gov.lbl.netlogger.LogMessage;
    import java.util.Calendar;

    public class NetloggerJava {
      public static void main(String[] args) {
        // Create a NetLogger message
        String unique_event = "fgtest." + System.getProperty("user.name");
        int val = Calendar.getInstance().get(Calendar.SECOND);
        LogMessage nlmessage = new LogMessage(unique_event).add("val",val);
        System.out.println( nlmessage );
      }
    }

To compile, type

::

    javac -cp netlogger-java-trunk.jar NetloggerJava.java

To run and redirect the output to a file called file.log, type

::

    java -cp .:netlogger-java-trunk.jar NetloggerJava >> file.log

Run a few more times waiting a few seconds in between. The file.log file
should look like something like the below.

::

    $ cat file.log 
    ts=2010-10-18T10:37:16.943691Z event=fgtest.inca val=16 
    ts=2010-10-18T10:37:19.488067Z event=fgtest.inca val=19 
    ts=2010-10-18T10:37:21.364917Z event=fgtest.inca val=21

To send the events to the Netlogger server, use the nl\_write command as
follows to send the results using the AMQP protocol.

::

    $ nl_parse -a localhost bp file.log

You can then view the values using the graphing page below (substitute
'inca' with your username)

http://inca.futuregrid.org:8080/inca/jsp/mongo.jsp?event=fgtest.inca&fields=val

The nl\_parse tool can also be run on a set of files and in tail mode so
that it runs in the background and sends changes to the log files as
they are written. To view more about nl\_parse's capabilities please
see the
`manpage <http://acs.lbl.gov/projects/netlogger/releases/doc/trunk/manual.html#man_nl_parse>`__
and
`cookbook <http://acs.lbl.gov/projects/netlogger/releases/doc/trunk/cookbook.html#_pipeline_parser_nl_parser>`__
for examples.


[`edit <https://wiki.futuregrid.org/index.php?title=Docs/Performance/NetloggerHowTo&action=edit&section=10>`__\ ] Write Your Own Parse Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your component already has log files that it generates and you would
like to parse data and process it before logging a Netlogger event, you
should write your own parse script. The advantage of this method is
that you do not need to modify your component's source code and you can
write a custom parse script fairly quickly using Perl or Python. Below
shows an example of a Perl script that parses the number and type of
connections from Inca's depot log file, sums the totals per hour, and
sends the data (numConns, numInserts, numQueries) as Netlogger events.

::

    #!/usr/bin/perl

    use strict;
    use warnings;
    use NetLogger;
    use Date::Manip;

    my $DIR = "$ENV{HOME}/fg/var";
    my $LOG = "depot.log";
    my $AGO = "yesterday";

    my $yesterday = UnixDate( ParseDate($AGO), "%Y-%m-%e" );
    my $logfile = "$DIR/$LOG.$yesterday";

    print "Parsing $logfile\n";

    my @files = glob( "$logfile*" );
    die "No log file found" if scalar(@files) < 1;

    my $cat = $files[0] =~ /gz$/ ? "zcat" : "cat";

    my $log = new NetLogger();
    #$log->open("foo.log");
    my $r = $log->open("x-netlog://localhost");
    die "Unable to connect to NetLogger broker" if undef $r;

    open( FD, "$cat $files[0]|" );
    my ($numConns, $numInserts, $numQueries) = (0,0,0);
    my $hour = 0;
    while(  ) {
      if ( /Servicing/ || /Running/ ) {
        my ($ts) = $_ =~ /^(\d\d:\d\d:\d\d)/;
        $ts =~ s/,/./; # convert the , before millis to .
        my $tsDate = ParseDate("$yesterday at $ts");
        if ( UnixDate($tsDate, "%H") != $hour ) {
          my $gmtDate = DateCalc( $tsDate, "+4hours" );
          my $nsts = UnixDate( $gmtDate, "%Y-%m-%dT%H:00:00Z" );
          $log->info( "inca.depot.usage", { ts => $nsts, 
            numConns => $numConns, numInserts => $numInserts, numQueries => $numQueries} );
          ($numConns, $numInserts, $numQueries) = (0,0,0);
          $hour = UnixDate($tsDate, "%H");
        };
        $numConns++ if /Servicing/;
        $numInserts++ if /Running/ && /Insert/;
        $numQueries++ if /Running/ && /Query/;
      }
    }
    close FD;
    $log->close();


View Data
---------

Once you have inserted data into the Netlogger server, you can view the
data in three ways: 1) use the MongoDB console, 2) use the MongoDB APIs
to fetch and visualize the data, or 3) use the mongo.jsp custom script.

�Each are described in the following subsections.

MongoDB Console
~~~~~~~~~~~~~~~

To access the MongoDB console, just type 'mongo <dbname>' on
inca.futuregrid.org or download MongoDB from the `MongoDB
website <http://www.mongodb.org/downloads>`__�and install it on your
local machine. If you do the latter, please send the IP address of your
machine to performance@futuregrid.org so that you can get thru the
firewall. Then to connect type 'mongo inca.futuregrid.org/<dbname>'.
For example to query the 'inca' database, type

::

    % mongo inca
    MongoDB shell version: 1.4.3
    url: inca
    connecting to: inca
    type "help" for help
    >

By default Netlogger data is placed in the collection 'netlogger'. To
view the number of records in your collection, type

::

    > db.netlogger.count()
    161
    > 

To view all records, type

::

    > db.netlogger.find()
    { "_id"�: ObjectId("4cb76f0ce1dab05e7500005e"), "numConns"�: "507", "level"�: "INFO", "numQueries" : 
    "210", "ts" : "Wed Oct 13 2010 01:00:00 GMT-0400 (EDT)", "numInserts" : "297", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cb76f0fe1dab05e7500005f"), "numConns" : "507", "level" : "INFO", "numQueries" : 
    "210", "ts" :  "Wed Oct 13 2010 02:00:00 GMT-0400 (EDT)", "numInserts" : "297", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cb76f13e1dab05e75000060"), "numConns" : "516", "level" : "INFO", "numQueries" : 
    "210", "ts" : "Wed Oct 13 2010 03:00:00 GMT-0400 (EDT)", "numInserts" : "306", "event" : "inca.depot.usage" }
    has more

If 'has more' is printed at the end, type 'it' to list the next set of
entries

::

    > it                                                                                                                                                                      
    { "_id" : ObjectId("4cb76f4be1dab05e75000072"), "numConns" : "512", "level" : "INFO", "numQueries" : 
    "209", "ts" : "Wed Oct 13 2010 21:00:00 GMT-0400 (EDT)", "numInserts" : "303", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cb76f4ee1dab05e75000073"), "numConns" : "512", "level" : "INFO", "numQueries" : 
    "210", "ts" : "Wed Oct 13 2010 22:00:00 GMT-0400 (EDT)", "numInserts" : "302", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cb76f52e1dab05e75000074"), "numConns" : "508", "level" : "INFO", "numQueries" : 
    "210", "ts" : "Wed Oct 13 2010 23:00:00 GMT-0400 (EDT)", "numInserts" : "298", "event" : "inca.depot.usage" }

To search for specific entries, add search criteria. For example to
search for all entries that have numQueries = 209

::

    > db.netlogger.find( { numQueries : "209" } )     
    { "_id" : ObjectId("4cb76f22e1dab05e75000065"), "numConns" : "513", "level" : "INFO", "numQueries" : 
    "209", "ts" : "Wed Oct 13 2010 08:00:00 GMT-0400 (EDT)", "numInserts" : "304", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cb76f34e1dab05e7500006b"), "numConns" : "519", "level" : "INFO", "numQueries" : 
    "209", "ts" : "Wed Oct 13 2010 14:00:00 GMT-0400 (EDT)", "numInserts" : "310", "event" : "inca.depot.usage"   }
    { "_id" : ObjectId("4cb76f4be1dab05e75000072"), "numConns" : "512", "level" : "INFO", "numQueries" : 
    "209", "ts" : "Wed Oct 13 2010 21:00:00 GMT-0400 (EDT)", "numInserts" : "303", "event" : "inca.depot.usage" }
    { "_id" : ObjectId("4cbcd261e1dab0570300000c"), "numConns" : "507", "level" : "INFO", "numQueries" : 
    "209", "ts" : "Sun Oct 17 2010 13:00:00 GMT-0400 (EDT)", "numInserts" : "298", "event" : "inca.depot.usage" } 

Other useful queries are described below:

-  Find events on a specific timestamp:

::

    >  db.netlogger.find( { ts�: new Date( 'Oct 12, 2010 02:00:00') } )         

-  Find events less than a specific timestamp:

::

    > db.netlogger.find( { ts�: { $lt: new Date( 'Oct 12, 2010 03:00:00') } } )

-  Find events greater than a value:

::

    > db.netlogger.find( { numQueries�: { $gt: "209" } }

For more help on queries, please see the MongoDB's user guide on
`Querying <http://www.mongodb.org/display/DOCS/Querying>`__.

MongoDB Query APIs
~~~~~~~~~~~~~~~~~~~

If you would like to view data from a script or web page, `query
APIs <http://api.mongodb.org/>`__ are available in C++, Java, JS, PHP,
Perl, Python, and Ruby. �If you are deploying on a machine other than
inca.futuregrid.org, please email the IP address of the machine to
performance@futuregrid.org so we can except it from the firewall. 

The
following is an example of a JSP page that queries data using
the \ `MongoDB Java API <http://api.mongodb.org/java/current/>`__ and
displays it using the `Dygraphs Javascript
API <http://danvk.org/dygraphs/>`__. �The relevant Mongo Java API parts
are highlighted in green.

::

    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    <%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
    <%@ taglib prefix="inca" tagdir="/WEB-INF/tags/inca" %>

    <%@ page import="com.mongodb.Mongo" %> 
    <%@ page import="com.mongodb.DB" %>
    <%@ page import="com.mongodb.DBCollection" %>
    <%@ page import="com.mongodb.DBObject" %>
    <%@ page import="com.mongodb.BasicDBObject" %>
    <%@ page import="com.mongodb.DBCursor" %> 
    <%@ page import="java.util.Date" %>
    <%@ page import="java.util.Calendar" %>

    <c:set var="usage">
    Description:  Graph netlogger data stored in inca.futuregrid.org.

    Usage:  mongo.jsp?database=fgtest&event=e&fields=f1,f2,...&labels=l1,l2,...&
      width=500&height=200&labelwidth=125&labelheight=200&title=Netlogger data

    where

    database = the name of the database [default: fgtest]

    event = name of a Netlogger event

    fields = comma separated list of fields to graph

    labels = comma separated list labels for the series

    width = width of the graph [default: 500]

    height = height of the graph [default: 200]

    labelwidth = width of the label area [default: 125]

    labelheight = height of the label area [default: 200]

    title = title for the graph [default: Netlogger data]
    </c:set>

    <%-- Check input parameters and redirect error if incorrect --%>
    <c:set var="error">
    ${empty param.event ?  'Missing event parameter' :  }
    ${empty param.fields ?  'Missing fields parameter' : }
    </c:set>
    <c:if test="${error != }">
    <jsp:forward page="error.jsp">
    <jsp:param name="msg" value="${error}" />
    <jsp:param name="usage" value="${usage}" />
    </jsp:forward>
    </c:if>

    <c:set var="width" value="${empty param.width ? 500 : param.width}"/>
    <c:set var="height" value="${empty param.height ? 200 : param.height}"/>
    <c:set var="labelwidth" value="${empty param.labelwidth ? 125 : param.labelwidth}"/>
    <c:set var="labelheight" value="${empty param.labelheight ? 200 : param.labelheight}"/>
    <c:set var="graphstyle">width:<c:out value="${width}"/>;height:<c:out value="${height}"/></c:set>
    <c:set var="labelstyle">width:<c:out value="${param.labelwidth}"/>;height:<c:out value="${param.labelheight}"/></c:set>
    <c:set var="title" value="${empty param.title ? 'Netlogger data' : param.title}"/>
    <c:set var="labels" value="${empty param.labels ? param.fields : param.labels }"/>
    <c:set var="database" value="${empty param.database�? 'fgtest'�: param.database }"/>

    <html>
    <head>
    <inca:getUrl var="url"/>
    <link href="${url}/css/inca.css" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="${url}/js/dygraph-combined.js"></script>
    <title>${title}</title>
    </head>
    <body>

    <%
    String[] fields = request.getParameter("fields").split(",");
    String event = request.getParameter("event");
    String labels = (String)pageContext.getAttribute("labels");
    String database = (String)pageContext.getAttribute("database");
    Mongo m = new Mongo( "localhost" );
    DB db = m.getDB( database );
    DBCollection coll = db.getCollection("netlogger");
    if ( coll.getCount() < 1 ) {
    pageContext.setAttribute( "error", "Zero records found for event " + event + " in database " + database);
    �%>
    <jsp:forward page="error.jsp">
    <jsp:param name="msg" value="${error}" />
    <jsp:param name="usage" value="${usage}" />
    </jsp:forward>
    <%
    }   
    %>

    <table border="0">
    <tr><td align="center">
    <h1><c:out value="${title}"/></h1>
    <p>x-axis = Timestamp, y-axis = <c:out value="${param.ylabel}"/></p>
    </td></tr>
    <tr>
    <td><div id="graphdiv"  style="${graphstyle}"></div></td>
    <td valign="top"><div id="labeldiv" style="${labelstyle}"></div></td>
    </tr>
    </table>
    <script type="text/javascript">
    g = new Dygraph(
    document.getElementById("graphdiv"),

    function HourlyData() {
    return "" +
    <%
    out.println( "\"Date," + labels + "\\n\"" );
    BasicDBObject query = new BasicDBObject();
    query.put( "event", event );
    DBCursor results = coll.find(query);
    while(results.hasNext()) {
    DBObject result = results.next();
    Calendar cal = Calendar.getInstance();
    cal.setTime( (Date)result.get("ts") );
    String tsString = cal.get(Calendar.YEAR) + "-" + cal.get(Calendar.MONTH) + "-" + 
          cal.get(Calendar.DAY_OF_MONTH) + " " + cal.get(Calendar.HOUR_OF_DAY) +
          ":" + cal.get(Calendar.MINUTE) + ":" + cal.get(Calendar.SECOND);; 
    out.println(" + \"" + tsString + "\"");
    for( int i = 0; i < fields.length; i++ ) {
    out.println( " + \"," + result.get(fields[i]) + "\"" );
    }
    out.println( " + \"\\n\"" );
    }
     %>
    },
    { includeZero : true,
    labelsSeparateLines : true,
    labelsDiv: document.getElementById("labeldiv") 
    }
    );
    </script>

    </body>
    </html>

 

mongo.jsp
~~~~~~~~~

If you want view a simple graph of you Netlogger collected data, you can
use the mongo.jsp interface hosted within the Inca deployment at
inca.futuregrid.org.  It uses the Dygraphs Javascript API to plot
multiple values within a single event on a time series graph as shown in
the below picture.

|image2|

A live view of that same graph can be found at `this
url <http://inca.futuregrid.org:8080/inca/jsp/netlogger.jsp>`__. 

To
view the values on the graph, simply mouse-over the lines. It also
supports zooming if you click on a location on the graph and drag a box
over an area.�To zoom out, just double-click anywhere on the graph.

To view your data, simply provide your database name and either:

-  one or more event names and one field name

or

-  one event name and one or more field names

Please see the help information below for more options.

::

     Description:  Graph netlogger data stored in inca.futuregrid.org.

      Usage:  mongo.jsp?database=fgtest&event=e&fields=f1,f2,...&labels=l1,l2,...&width=500&height=200&labelwidth=125&labelheight=200&title=Netlogger data

              or 

              mongo.jsp?database=fgtest&event=e1,e2,...&fields=f&labels=l1,l2,...&width=500&height=200&labelwidth=125&labelheight=200&title=Netlogger data

      where

      database = the name of the database [default: fgtest]

      events = one or comma separated list of Netlogger event names.  If multiple
               events specified, fields must contain a single field

      fields = one or comma separated list of fields to graph.  If multiple
               fields specified, events must contain a single event

      labels = comma separated list labels for the series

      width = width of the graph [default: 500]

      height = height of the graph [default: 200]

      labelwidth = width of the label area [default: 125]

      labelheight = height of the label area [default: 200]

      title = title for the graph [default: Netlogger data]

      ylabel = label for the y axis [default

Publishing Data
---------------

A Drupal page has been created to add Netlogger data graphs on the
portal.futuregrid.org website using IFrames.�Access this page using the
following url:

-  http://portal.futuregrid.org/performance/netlogger

Please add your graph to the page when it is ready.�Remember not to use
the "Preview" button in Drupal as it will cause the contents to be
duplicated within that page.

References
==========

-  `Netlogger Home
   Page <http://acs.lbl.gov/NetLoggerWiki/index.php/NetLogger_Toolkit>`__
-  `MongoDB Home Page <http://www.mongodb.org/>`__


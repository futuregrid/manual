**********************************************************************
Just Enough Python for the Cloud
**********************************************************************


* http://www.korokithakis.net/tutorials/python/

and here is one that you can do on a web browser in case you have not installed python on your computer

* http://www.afterhoursprogramming.com/tutorial/Python/Introduction/

Terminal
===================================================================
::

   todo

OS Specific
===================================================================

Linux
----------------------------------------------------------------------

OS X
----------------------------------------------------------------------

::

   uname -a
   Darwin pro-2013.local 12.3.0 Darwin Kernel Version 12.3.0: Sun Jan 6 22:37:10 PST 2013; root:xnu-2050.22.13~1/RELEASE_X86_64 x86_64

::

   >>> python
   Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
   [GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin


Windows
----------------------------------------------------------------------

todo

Lanaguage Features
==================================================================

Print
-----------------------------------------------------------------
.. runblock:: pycon

   >>> print "Hello Cloud"

Comments
-----------------------------------------------------------------
.. runblock:: pycon

   >>> # this is a comment

Multiline Comment
-----------------------------------------------------------------
.. runblock:: pycon

   >>> """ 
   ... this is a multiline coment 
   ... """

Multiline Comment
-----------------------------------------------------------------
.. runblock:: pycon

   >>> '''
   ... this is a multiline coment
   ... '''

Variables
-----------------------------------------------------------------
.. runblock:: pycon

   >>> flavor = "tiny"
   ... print flavor

Changing the variable Value
-----------------------------------------------------------------
.. runblock:: pycon

   >>> flavor = "large"
   ... print flavor

List
-----------------------------------------------------------------
.. runblock:: pycon

    >>> list = [1, 2, 3, 4, 5, 6]
    ... print list[0]
    ... print list[len(list)-1]
    ... print list[2:5]



For Loop
-----------------------------------------------------------------
.. runblock:: pycon

    >>> list = [1, 2, 3, 4, 5, 6]
    ... for element in list:
    ...   print element

Arithmetic Operators
-----------------------------------------------------------------
.. runblock:: pycon

    >>> list = [1, 2, 3, 4, 5, 6]
    ... print sum(list)
    ... print min(list)
    ... print max(list)
    ... print sum(list)/len(list)
    ... print sum(list)/float(len(list))

Function to do calculations
-----------------------------------------------------------------
.. runblock:: pycon

    >>> def f(x,y):
    ...   return x+y+ y*y + x*x
    ...
    ... print f(1,2)
    ... print f(4,6)


Functions for String Manipulation
-----------------------------------------------------------------
.. runblock:: pycon

    >>> def name(firstname, lastname):
    ...   return "%s %s" % (firstname, lastname)
    ...
    ... def reversename(firstname, lastname):
    ...   return "%s, %s" % (lastname, firstname)
    ...
    ... print name('Gregor', 'von Laszewski')
    ... print reversename('Gregor', 'von Laszewski')

If Condition
-----------------------------------------------------------------
.. runblock:: pycon

   >>> flavor = "tiny"
   ... if flavor -- "tiny":
   ...    print("vanilla has a tiny flavor")
   ... elif flavor -- "large":
   ...    print("chocolate has a large flavor")
   ... else:
   ...    print("other flavors I do not like")

For
------------------------------------------------------------------
.. runblock:: pycon

   ... flavors = ['tiny', 'medium', 'large']
   ... for flavor in flavors:
   ...   print flavor

Local
===================================================================
::

   $ man python

Ecosystem
===================================================================

.. todo:: mind the virtualenv

pypi
----------------------------------------------------------------------
The Python Package Index is a large repository of software for the
Python programming language containing a large number of packages
[link]. The nice think about pipy is that many packages can be
installed with the program 'pip'.

To do so you have to locate the <package_name> for example with the
serach function in pypi and say on the commandline::

    pip install <package_name>

where pagage_name is the string name of the package. an example would
be the package called fabric which you can install with::

   pip install fabric
 
If all goes well the package will be installed.

github
----------------------------------------------------------------------

todo

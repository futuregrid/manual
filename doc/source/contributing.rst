**********************************************************************
Building the Book
**********************************************************************

Make sure the is no book directory in your home

Virtualenv
----------------------------------------------------------------------
Use virtual env::

    cd
    virtualenv book
    source book/bin/activate

Theme
----------------------------------------------------------------------
To build this book make sure you install the following module::

    pip install sphinx_bootstrap_theme

Autorun
----------------------------------------------------------------------

https://bitbucket.org/birkenfeld/sphinx-contrib/src/c54749e503872d3f7a00c0561a115000dcc83565/autorun?at=default

$ hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/
$ cd sphinx-contrib/autorun
$ python setup.py install


======================
  linkedin-scraper
======================

Download user data from LinkedIn


Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on keywords defined by user, perform a LinkedIn query,
extract user information from the first results page and store it
to a CSV file.


Synopsis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``linkedin-scraper [--output FILE] keyword [keyword...]``


Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for Java Developers and store the result to ``java.csv``::

    linkedin-scraper --output java.csv java developer

Output
------

The resulting CSV file can look like this::

    First name,Last name,Position,Company,City,Country
    Alice,Carter,Python & Java Developer,Google,Mountain View,United States 
    Robert,Smith,Senior Java Developer,British Airways,London,United Kingdom
    ...

Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install the package system-wide::

    python setup.py install

or for current user only::

    python setup.py install --user

Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

Note that to perform LinkedIn queries, the tool **needs an access
token**. The token is read from the file ``.linkedin-access-token``
in your home directory. 

Author
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Martin Frodl <https://github.com/mfrodl>`_


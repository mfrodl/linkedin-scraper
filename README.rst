
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

Installation
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

Gotchas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

Some fields in the output CSV file might be empty. This indicates
that the scraper failed to extract the relevant piece of
information from the results page. One of the common causes is
the limited visibility of profiles out of your network, a LinkedIn
feature which prevents regular users from accessing certain
profile information.

Author
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Martin Frodl <https://github.com/mfrodl>`_


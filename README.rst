Twitter API Project
===========================

This is a tutorial aimed at users new to Python but looking to
dive into a real world project by querying the Twitter API_.
The project idea and some other ideas were liberally borrowed
from the `Boston Python Group`_.

.. _API: https://dev.twitter.com
.. _Boston Python Group: https://openhatch.org/wiki/Boston_Python_Workshop_5/Twitter_handout

In this project, you will adapt an existing script which queries
the Twitter API to print out the users and tweet text for a 
`Twitter search`_.

.. _Twitter search: https://dev.twitter.com/docs/using-search


Prerequisites
-------------

This example requires the Requests_ module. Please download_ the module and
install it. If you are already familiar with pip, feel free to install Requests
with it.

.. _Requests: http://python-requests.org/
.. _download: http://packages.crate-cdn.com/2/1/a/8/21a81ddf1a3c2f956524538966ae19c38cae251f5629821588cdc8246a1335f7/requests-1.1.0.tar.gz

Unzip the Requests package and install it by executing:

::

  python setup.py install

Goals
-----

* Learn about imports and modules
* Learn about loops
* Use lists and dictionaries
* Argument parsing
* Have fun searching Twitter

Try
---

Try executing the following

::

  python sample_search.py
  python sample_search.py -h
  python sample_search.py "#Python"
  python sample_search.py "@sandiegopython"


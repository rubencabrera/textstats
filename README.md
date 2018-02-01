Textstats
=========

A python exercise showing a simple web app that takes a text and returns some
statistics about it.

For the web interface, Flask microframework has been chosen, time is short and
getting up and running with Flask is very fast and easy. Growth is possible,
there's room for scaling.

Bokeh is the library chosen for the data visualization tool.

Requirements:
-------------

+ Python >= 3.5
+ pip (to install other dependencies, specified in requirements.txt)

How to run it:
--------------

**Linux and Windows**

Clone this repo and run (use of virtualenv is recommended).

    pip install -r requirements.txt
    python tst.py

Open a browser of your choice and open the next address:

    127.0.0.1:5000/form


Your browser mustn't block the port 5000. If you run this app in another
machine in the local network, make sure the firewall is not blocking this port.
If you run this app in a remote machine, make sure the port 5000 is accessible
or set a reverse proxy.


Considerations:
---------------

As an end user app, the dashboard and frontend should be taken care and made to
look as smooth as possible. The math behind and the rest of the backend are 
important, that's why the app needs to be appealing (which is far from done).

As many datasets (text samples in this app) should be used for further
development. Words with just one appearance behave like noise in the word count
graph. Characters like line breaks and spaces do the same on character count.

Bar graphs are useful, but don't keep users' attention for very long. Word
clouds seem to work way better, but take some more time to develop. 

Problems may arise from:
------------------------

+ Non standard encodings, like Windows specific charsets and line breaks.
+ Insecure or non trusted users.




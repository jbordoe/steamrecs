steamrecs
=========

A basic python reimplementation of Steam's APIs

api-client.py
-------------
A front-end demo script to show off the capabilities of the api. Not exactly amazing, but it does the job.

steamapi.py
-----------
The wrapper for Steam's APIs. Instead of manually pulling in the data ourselves, I plan to have most (all?) Steam APIs implemented in that script file.

Please note in order to get the steam key, you must stick your steam key in a text file called `steamkey` in the same directory as the script

steamapitest.py
---------------
A test class to ensure the api calls are doing the right thing. Also is a kind of neat way of documenting what the methods are doing/what to expect
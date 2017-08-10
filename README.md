# whatsapp-broadcast-crawler

Crawler made with Selenium and Python to constantly receive video/audio from target and broadcast to a list of contacts.

## Installation ##

First you must install Selenium for python.

`$ pip install selenium`

Check [official selenium documentation](http://selenium-python.readthedocs.io/index.html) if needed.

Selenium requires a driver to interact with the choosen browser. I recommend looking in this [installation guide](http://selenium-python.readthedocs.io/installation.html) in drivers section.

Make sure your setup is working before run section.

## Set Up ##

* Create your broadcast list in your whatasapp app (not web);
* Go to [this line]() in `broadcast.py` and choose your target and broadcast list;

```
#####################################
#           CONFIGURATION           #
#####################################

self._target = "person name"
self._broadcast = "broadcast list name"

#####################################
#                END                #
#####################################

* Save file and you're good to go.

```

## Run ##

`$ python broadcast.py`

Wait the loading finish and do QR CODE manually. After that, let the magic happen.
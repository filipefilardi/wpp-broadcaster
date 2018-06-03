# whatsapp-broadcast-crawler

Crawler made with Selenium and Python to constantly receive video from target and broadcast to a list of contacts. The script only works with whatsapp web.

## Install ##

Install Selenium for python.

`$ pip install selenium`

Check [official selenium documentation](http://selenium-python.readthedocs.io/index.html) if needed.

Selenium requires a driver to interact with your browser. I recommend looking in this [installation guide](http://selenium-python.readthedocs.io/installation.html) in drivers section to install the proper driver.

## Set Up ##

* Create your broadcast list in your whatasapp mobile;
* Add your target and broadcast list in [this line](https://github.com/filipefilardi/whatsapp-broadcast-crawler/blob/master/broadcast.py#L18).

```python
#####################################
#           CONFIGURATION           #
#####################################

self._target = "person name"
self._broadcast = "broadcast list name"

#####################################
#                END                #
#####################################

```

## Run ##

`$ python broadcast.py`

Wait QR CODE screen appears and do it manually. After that, python will start to broadcast received target messages.

Make sure you know what you're doing. All contributors of this repository are exempt for any of your actions.

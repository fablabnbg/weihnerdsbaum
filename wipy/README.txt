
import machine
machine.reset()

import os
os.uname().release
 -> version number.

import wipy
wipy.heartbeat(False)

from network import WLAN
wlan = WLAN() # we call the constructor without params

wlan.mode()

https://github.com/wipy/wipy/releases

ftp mcuimg.bin -> /flash/sys/mcuimg.bin
 -> passive mode!
## just does nothing...


# If you power up normally, or press the reset button, the WiPy will boot into
# standard mode; the boot.py file will be executed first, then main.py will
# run.

# You can override this boot sequence by pulling GP28 up (connect it to the 3v3
# output pin) during reset. This procedure also allows going back in time to
# old firmware versions. The WiPy can hold up to 3 different firmware versions,
# which are: the factory firmware plus 2 user updates.

## Safe Boot Pin GP28 released during:
# 1st 3 secs window: Safe boot, latest firmware is selected
# 2nd 3 secs window: Safe boot, previous user update selected
# Final 1.5 secs window: Safe boot, the factory firmware is selected


ws2812
------
# Data-Pin to GPIO16
import ws2812
chain = ws2812.WS2812(nleds=14)
chain.show([ (255, 0, 0), (0, 255, 0), (0, 0, 255), (30, 30, 30) ])


move into fablab wlan
---------------------
execfile('try_wlan.py')

172.16.21.147


reading a url
-------------

import socket
s = socket.socket()
s.connect(socket.getaddrinfo('fablink.de', 80)[0][4])


# try enter one of my networks. fallback to AP mode.
# See ~/src/github/wipy/wipy/micropython/docs/library/network.rst

import network
wlan = network.WLAN()
print(wlan.mode())

wlan = network.WLAN(mode=network.WLAN.STA)
nets = wlan.scan()

success = False

for net in nets:
  if net.ssid == 'jw samsung s4':
    print("s4 hotspot found")
    try:
      wlan.connect(net.ssid, auth=(net.sec, 'fablabnbg'), timeout=5000)
      while not wlan.isconnected():
        machine.idle()
      print('wlan connection succeeded')
      success=True
      break
    except:
      print("wlan connection failed")

  if net.ssid == 'FabLab_NBG':
    print("fablab found")
    try:
      wlan.connect(net.ssid, auth=(net.sec, 'fablabnbg'), timeout=5000)
      while not wlan.isconnected():
        machine.idle()
      print('wlan connection succeeded')
      success=True
      break
    except:
      print('wlan connection failed')

if not success:
  print('none connected. Returning to AP mode')
  wlan = network.WLAN(mode=network.WLAN.AP)


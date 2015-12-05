# try enter one of my networks. fallback to AP mode.
# See ~/src/github/wipy/wipy/micropython/docs/library/network.rst

# for debugging
import ws2812
leds=10
chain = ws2812.WS2812(nleds=leds)

import network
wlan = network.WLAN()
print(wlan.mode())
# 	         R  B  G
chain.show(10* [(255,0,0)])
wlan = network.WLAN(mode=network.WLAN.STA)
chain.show(10* [(0,255,0)])
nets = wlan.scan()
chain.show(len(nets) * [(255,255,0)])
time.sleep(2)

success = False
out = open("/flash/out.txt", "w")

for net in nets:
  print("net="+net.ssid, file=out)
  if net.ssid == 'jw samsung s4':
    print("s4 hotspot found", file=out)
    try:
      wlan.connect(net.ssid, auth=(net.sec, 'fablabnbg'), timeout=5000)
      while not wlan.isconnected():
        machine.idle()
      print('wlan connection succeeded', file=out)
      success=True
      break
    except:
      print("wlan connection failed", file=out)

  if net.ssid == 'FabLab_NBG':
    print("fablab found", file=out)
    try:
      wlan.connect(net.ssid, auth=(net.sec, 'fablabnbg'), timeout=5000)
      while not wlan.isconnected():
        machine.idle()
      print('wlan connection succeeded', file=out)
      success=True
      break
    except:
      print('wlan connection failed', file=out)

if not success:
  print('none connected. Returning to AP mode', file=out)

chain.show(10 * [(0,0,8)])
wlan = network.WLAN(mode=network.WLAN.AP)
chain.show(10 * [(12,0,0)])

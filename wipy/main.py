# main.py -- put your code here!

import os,struct,time
import ws2812
leds=20*5*2
chain = ws2812.WS2812(nleds=leds)

## bloede billig china-kette....
##        B R G
# dark = (0,4,8)
##          warm white  , yellow    ,  orange    ,  green        rosa
## bright = [ (20,200,150),(0,200,150), (0,255,140), (80,200,100), (0,200,20) ]
#       R B G
dark = (12,0,8)

bright = [ dark,(200,20,150),dark,(200,0,150), dark, dark, (255,0,140), dark,(200,80,100), dark, dark, dark, (200,0,20) ]
bright_idx = 0

data = leds*[dark]

def ru16():
  return struct.unpack("<H", os.urandom(2))[0]

def rint(top):
  return ru16() * top // 65535

for b in bright:
  data[rint(leds)] = b
  data[rint(leds)] = b
  data[rint(leds)] = b

while True:
  chain.show(data)
  time.sleep_ms(100)
  i = rint(leds)
  print(i)
  data[i] = bright[bright_idx]
  bright_idx = bright_idx + 1
  if (bright_idx >= len(bright)): 
    bright_idx = 0


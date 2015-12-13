# main.py -- put your code here!

import os,struct,time
import ws2812
import FabLabNbgAPI

space = FabLabNbgAPI.SpaceAPI()

leds=10*5*2
chain = ws2812.WS2812(nleds=leds)

## bloede billig china-kette....
##        B R G
# dark = (0,4,8)
##          warm white  , yellow    ,  orange    ,  green        rosa
## bright = [ (20,200,150),(0,200,150), (0,255,140), (80,200,100), (0,200,20) ]
#       R B G
dark = (12,0,8)

#                red     , yellow   , white     ,  white
bright = [ dark,(200,0,0),(255,0,60),(255,16,64),(200,20,150),dark, dark, dark, (255,0,60), dark, dark, dark, dark, (200,0,20) ]
bright_idx = 0

data = leds*[dark]

def ru16():
  return struct.unpack("<H", os.urandom(2))[0]

def rint(top):
  v = ru16() * top // 65535
  if v == top: v = top - 1
  return v

for b in bright:
  data[rint(leds)] = b
  data[rint(leds)] = b
  data[rint(leds)] = b

while True:
  if not space.poll(['state/open']):
    chain.show([dark])
    time.delay(100)
    break

  for loop in range(1000):
    for i in range(leds):
      n = rint(len(bright))
      data[i] = bright[n]
      chain.show(data)
    for i in reversed(range(leds)):
      n = rint(len(bright))
      data[i] = bright[n]
      chain.show(data)


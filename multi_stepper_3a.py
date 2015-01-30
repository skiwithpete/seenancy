#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

axisx = [4,17,27,22]
axisy = [10,9,11,7]
axisz = [15,18,23,24]

for pin in axisx + axisy + axisz:
   GPIO.setup(pin,GPIO.OUT)
   GPIO.output(pin,0)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

try:
  while True:
    stepsx = raw_input("How many X steps forward? ")
    stepsy = raw_input("How many Y steps forward? ")
    stepsz = raw_input("How many Z steps forward? ")
    if int(stepsx) < 0:
      seq.reverse()
      for i in range(-int(stepsx)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisx[pin], seq[halfstep][pin])
          time.sleep(0.001)
      seq.reverse()
    else:
      for i in range(int(stepsx)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisx[pin], seq[halfstep][pin])
          time.sleep(0.001)

    if int(stepsy) < 0:
      seq.reverse()
      for i in range(-int(stepsy)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisy[pin], seq[halfstep][pin])
          time.sleep(0.001)
      seq.reverse()
    else:
      for i in range(int(stepsy)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisy[pin], seq[halfstep][pin])
          time.sleep(0.001)

    if int(stepsz) < 0:
      seq.reverse()
      for i in range(-int(stepsz)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisz[pin], seq[halfstep][pin])
          time.sleep(0.001)
      seq.reverse()
    else:
      for i in range(int(stepsz)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(axisz[pin], seq[halfstep][pin])
          time.sleep(0.001)


# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"
  GPIO.cleanup()

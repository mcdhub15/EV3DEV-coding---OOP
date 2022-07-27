



from ev3dev.auto import *
from ev3dev.ev3 import *
import time
import random
from random import randint

cl = ColorSensor('in1')
cl2 = ColorSensor('in4')

rmm = MediumMotor('outD')
smm = MediumMotor('outB')
lm = LargeMotor('outA')
rm = LargeMotor('outC')

us = UltrasonicSensor('in2')
us2 = UltrasonicSensor('in3')
us.mode='US-DIST-CM'
us2.mode='US-DIST-CM'
sound = Sound()

units = us.units
units2 = us2.units
# reports 'cm' even though the sensor measures 'mm'
distance1 = us.value()/10  # convert mm to cm
distance2 = us2.value()/10
#print(str(distance) + " " + units)
if distance1 < 30 or distance2 < 30:
      sound.tone([(200, 2000, 400),(800, 1000, 3000)])


units = us.units
units2 = us2.units
# reports 'cm' even though the sensor measures 'mm'
distance1 = us.value()/10  # convert mm to cm
distance2 = us2.value()/10
#print(str(distance) + " " + units)
if distance1 < 30 or distance2 < 30:
      sound.tone([(200, 2000, 400),(800, 1000, 3000)])

while True:
    rm.run_timed(time_sp=1000, speed_sp=-1000)
    lm.run_timed(time_sp=1000, speed_sp=-1000)

    rmm.run_timed(time_sp=1000, speed_sp=600)

    if cl.reflected_light_intensity > 16:
        lm.run_timed(time_sp=500, speed_sp=500)
        rm.run_timed(time_sp=500, speed_sp=500)
        time.sleep(.75)

        smm.run_timed(time_sp=1000, speed_sp=-400)
        time.sleep(.75)

                #lm.run_timed(time_sp=500, speed_sp=-500)
                #rm.run_timed(time_sp=500, speed_sp=-500)
                #time.sleep(.75)

                #smm.run_timed(time_sp=1000, speed_sp=400)
                #time.sleep(.75)

    if cl2.reflected_light_intensity > 16:
        lm.run_timed(time_sp=500, speed_sp=500)
        rm.run_timed(time_sp=500, speed_sp=500)
        time.sleep(.75)

        smm.run_timed(time_sp=1000, speed_sp=400)
        time.sleep(.75)

  #lm.run_timed(time_sp=500, speed_sp=-500)
                #rm.run_timed(time_sp=500, speed_sp=-500)
                #time.sleep(.75)

                #smm.run_timed(time_sp=1000, speed_sp=-400)
                #time.sleep(.75)


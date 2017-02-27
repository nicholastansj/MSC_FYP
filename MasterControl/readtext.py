#!/usr/bin/env python
# Filename: readtext.py

import sys
from sys import argv
import VStarCamMotor

def readText(filename):

#if __name__ == "__main__":
    #script, filename = argv
    #filename = argv
    #script = argv[0]
    #filename = argv[1].decode('string-escape')

    motor = VStarCamMotor.VStarCamMotor(domain = "172.21.150.182")

    txt = open(filename)
    print "File opened is %r:" % filename
    
    event = txt.read()
    eventvalue = int(event)
 
    print event

    if eventvalue == 800:
        #broken window event, move camera to preset position 2
        motor.PresetCamera2()
        print "Window broken event"
        return 2
    elif eventvalue == 1000:
        #explosion event, move camera to preset position 3
        motor.PresetCamera3()
        print "Explosion event"
        return 3
    else:
        motor.PresetCamera1()
        print "nothing happened"
        return 1


#!/usr/bin/env python
# Filename: Monitor.py
import sys
import VStarCamMotor
#URI = "http://172.21.150.182:81/decoder_control.cgi?loginuse=admin&loginpas=888888&command=%d&onestep=0"

#Initialize PTZ camera to default position that is non-intrusive
print "initialize camera"

motor = VStarCamMotor.VStarCamMotor(domain = "172.21.150.182")
#motor = VStarCamMotor(sys.argv[1])
motor.PresetCamera1()
if __name__ == "__main__":    
    import pygame
    import playsound
    import readtext
    
    #from time import sleep
    #from omxplayer import OMXPlayer

    Alarmflag = 0

    #while 1:
    while not Alarmflag:
            #read frequency values from textfile
            #result = readText()
            #If (result == 2) or (result == 3):
               #play alert sound via PI mic output
               #playsound.playAlert()
            motor.testMotor()
            Alarmflag = 1

        #if user acknowledged the alarm, set the camera back to preset position
        #If UserAcknowledgeFlag == 1:
            #PresetCamera1()
            #UserAcknowledgeFlag = 0


        #Poll/Read frequencies from inputs
        #frequency = readFrequency()

        #If (frequency >= threshold) and (Alarmflag == 0):
            #determine (x,y) coordinates based on frequency inputs
            #coord = calculateXY()
            #pass (x,y) to turn the camera 
            #moveCamera(coord.x, coord.y)
            #motor.testMotor()
            #play alert sound via PI mic output
            #playsound.playAlert()

            #send notification to alert personnel
            #SendAlarm()

            #set alarm flag
            #Alarmflag = 1
        
        #if user acknowledged the alarm, set the camera back to preset position
        #If UserAcknowledgeFlag == 1:
            #PresetCamera1()
            #UserAcknowledgeFlag = 0
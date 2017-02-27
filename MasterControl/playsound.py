#!/usr/bin/env python
# Filename: playsound.py
import pygame
from time import sleep
from omxplayer import OMXPlayer

sound_path = '/home/pi/Music/DenDenMushi.mp3'

def playAlert():
    global done
    global playOnce

    done = False
    playOnce = False

    if playOnce == False:    
        #pygame.init()
        #pygame.display.set_mode([100,100])
        done = False
        #print "initialize pygame window"
        omxp = OMXPlayer(sound_path)
        omxp.play()
        print 'Playing Sound'
        omxp.pause()
        playOnce = True

    while True:
       
#        for event in pygame.event.get():
#            print "for loop getting event"
#            if event.type == pygame.QUIT:
#                done = True
#                print "pygame.QUIT event"
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_ESCAPE:
#                    done = True
#                    playOnce = False
#                    omxp.quit()
                    #pygame.display.quit()
#                    print "escape key pressed"
#                elif event.key == pygame.K_F1:
#                    if (omxp.playback_status() == "Playing"):
#                        print(omxp.playback_status())
#                    elif (omxp.playback_status() == "Paused"):
#                        print(omxp.playback_status())
#                    elif (omxp.playback_status() == "Stopped"):
#                        print(omxp.playback_status())
#                    else:
#                        print "Unknown player status, quit player"
#                        playOnce = False
#                        omxp.quit()
                        #pygame.display.quit()

        if (omxp.playback_status() == "Stopped"):
            print "alert ended"
            playOnce = False
            #done = True
            omxp.quit()
            break

        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
            #print "space pressed"

    
if __name__ == "__main__":
    import sys
    import pygame
    from time import sleep
    from omxplayer import OMXPlayer
    
    pygame.init()
    pygame.display.set_mode([100,100])
    done = False
    print "initialize pygame window"
    #if (quit == False):
       #omxp = subprocess.Popen(['omxplayer',sound_path])
    omxp = OMXPlayer(sound_path)
    omxp.play()
    print 'Playing Sound'
    #sleep(5)
    omxp.pause()

    while not done:
       
        for event in pygame.event.get():
            print "for loop getting event"
            if event.type == pygame.QUIT:
                done = True
                print "pygame.QUIT event"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    omxp.quit()
                    print "escape key pressed"
                elif event.key == pygame.K_F1:
                    if (omxp.playback_status() == "Playing"):
                        print(omxp.playback_status())
                    elif (omxp.playback_status() == "Paused"):
                        print(omxp.playback_status())
                    elif (omxp.playback_status() == "Stopped"):
                        print(omxp.playback_status())
                    else:
                        print "Unknown player status, quit player"
                        done = True
                        omxp.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print "space pressed"

        if (omxp.playback_status() == "Stopped"):
            print "alert ended"
            done = True

	
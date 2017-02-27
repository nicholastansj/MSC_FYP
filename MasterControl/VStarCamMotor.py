from base.VStarCamOutput import VStarCamOutput
import urllib2
import pygame
import sys

class VStarCamMotor(VStarCamOutput):
    
    # These are the original state commands to send to the Kaicong camera.
    CMDLIST = {
        "PTZ_UP": 			0,
        "PTZ_UP_STOP": 		1,
        "PTZ_DOWN": 		2,
        "PTZ_DOWN_STOP": 	3,
        "PTZ_LEFT": 		4,
        "PTZ_LEFT_STOP": 	5,
        "PTZ_RIGHT": 		6,
        "PTZ_RIGHT_STOP": 	7,
        "PTZ_LEFT_UP": 		90,
        "PTZ_RIGHT_UP": 	91,
        "PTZ_LEFT_DOWN": 	92,
        "PTZ_RIGHT_DOWN": 	93,
        "PTZ_STOP": 		1,
        "PTZ_CENTER": 		25,
        "PTZ_VPATROL": 		26,
        "PTZ_VPATROL_STOP": 27,
        "PTZ_HPATROL": 		28,
        "PTZ_HPATROL_STOP": 29,
        "PTZ_SET_PRESET1": 30,
        "PTZ_PREFAB_BIT_SET1": 31,    #30 to set preset, 31 to goto preset based on www.foscam.es/descarga/ipcam_cgi_sdk.pdf
        "PTZ_SET_PRESET2": 32,
        "PTZ_PREFAB_BIT_SET2": 33,
        "PTZ_SET_PRESET3": 34,
        "PTZ_PREFAB_BIT_SET3": 35,
        "IO_ON": 			94, # TODO: What does this do?
        "IO_OFF": 			95, # and this one?
    }
    
    # This table converts a vector-style direction to its command
    MOVELIST = {
        "00": "PTZ_STOP",
        
        "0+": "PTZ_UP",
        "0-": "PTZ_DOWN",
        
        "+0": "PTZ_RIGHT",
        "-0": "PTZ_LEFT",
        
        "++": "PTZ_RIGHT_UP",
        "+-": "PTZ_RIGHT_DOWN",
        "-+": "PTZ_LEFT_UP",
        "--": "PTZ_LEFT_DOWN",
    }
    #URI = "http://172.21.144.49:81/decoder_control.cgi?loginuse={1}&loginpas={2}&command=%d&onestep=0"
    URI = "http://{0}:81/decoder_control.cgi?loginuse={1}&loginpas={2}&command=%d&onestep=0"
#var url = getHttpHost("decoder_control.cgi");
#url+='&command='+command;
#url+='&onestep=0';
#url+='&' + new Date().getTime() + Math.random();
#$.getScript(url);
#function getHttpHost(cgiUrl)
#{
#	return (cgiUrl+"?loginuse="+loginuser+"&loginpas="+encodeURIComponent(loginpass));
#}
    def __init__(self, domain, user="admin", pwd="888888"):
        VStarCamOutput.__init__(
            self, 
            domain, 
            VStarCamMotor.URI, 
            user, 
            pwd
        )
        #print "domain = %s" % domain
        self.state = '00'
        
    def _to_symbol(self, v):
        if v > 0:
            return '+'
        if v < 0:
            return '-'
        else:
            return '0'
    
    def send_command(self, cmdstr): 
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST[cmdstr]))
        result = stream.read()
        assert "ok" in result
        stream.close()
        
    def move(self, xy):
        move_symbol = self._to_symbol(xy[0]) + self._to_symbol(xy[1])
        cmdstr = VStarCamMotor.MOVELIST[move_symbol]
        if cmdstr != self.state:
            self.send_command(cmdstr)
        self.state = cmdstr
        
    def PresetCamera1(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET1"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET1"]
        result = stream.read()
        assert "ok" in result
        stream.close()

    #window broke event preset position 2
    def PresetCamera2(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET2"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET2"]
        result = stream.read()
        assert "ok" in result
        stream.close()

    #explosion event preset position 3
    def PresetCamera3(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET3"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_PREFAB_BIT_SET3"]
        result = stream.read()
        assert "ok" in result
        stream.close()
    
    def SetPresetPosition1(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_SET_PRESET1"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_SET_PRESET1"]
        result = stream.read()
        assert "ok" in result
        stream.close()

    def SetPresetPosition2(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_SET_PRESET2"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_SET_PRESET2"]
        result = stream.read()
        assert "ok" in result
        stream.close()

    def SetPresetPosition3(self):
        stream = urllib2.urlopen(self.uri % (VStarCamMotor.CMDLIST["PTZ_SET_PRESET3"]))
        print (self.uri) % VStarCamMotor.CMDLIST["PTZ_SET_PRESET3"]
        result = stream.read()
        assert "ok" in result
        stream.close()

    def testMotor(self):

        import readtext
        import playsound
        playOnce = False

        pygame.init()
        screen = pygame.display.set_mode((320, 240))
    
        motor = VStarCamMotor(domain = "172.21.150.182")

        def checkKeys():
            keys = pygame.key.get_pressed()
            x = 0
            y = 0
            if keys [pygame.K_1]:
                readtext.readText("null.txt")
            if keys [pygame.K_2]:
                readtext.readText("explosion.txt")
            if keys [pygame.K_3]:
                readtext.readText("window.txt")
            if keys [pygame.K_4]:
                if playOnce == False:
                  playsound.playAlert()
            if keys [pygame.K_a]:
                x = -1
            if keys [pygame.K_s]:
                y = -1
            if keys [pygame.K_d]:
                x = 1
            if keys [pygame.K_w]:
                y = 1
            if keys [pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                sys.exit()    
            motor.move([x, y])
            
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()
            checkKeys()
            #if playOnce == False:
                #playsound.playAlert()

if __name__ == "__main__":
    import pygame
    import sys
    
    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)
    
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    
    motor = VStarCamMotor(sys.argv[1])
    
    def checkKeys():
        keys = pygame.key.get_pressed()
        x = 0
        y = 0
        if keys [pygame.K_a]:
            x = -1
        if keys [pygame.K_s]:
            y = -1
        if keys [pygame.K_d]:
            x = 1
        if keys [pygame.K_w]:
            y = 1
        if keys [pygame.K_1]:
            motor.SetPresetPosition1()
        if keys [pygame.K_2]:
            motor.SetPresetPosition2()
        if keys [pygame.K_3]:
            motor.SetPresetPosition3()
        if keys [pygame.K_b]:
            motor.PresetCamera1()
        if keys [pygame.K_n]:
            motor.PresetCamera2()
        if keys [pygame.K_m]:
            motor.PresetCamera3()
        if keys [pygame.K_ESCAPE]:
            pygame.display.quit()
            pygame.quit()
            sys.exit()    
        motor.move([x, y])
            
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
        checkKeys()
        
        

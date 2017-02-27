

class VStarCamOutput():
    
    def __init__(self, domain, uri_format, user="admin", pwd="888888"):
        """ domain:   Camera IP address or web domain 
                      
        """
        self.running = False
        self.uri = uri_format.format(domain, user, pwd)
        
        

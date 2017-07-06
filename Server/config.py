import configparser


class serverSettings():
    def __init__(self):
        self.conf = configparser.RawConfigParser()
        self.conf.read("configserver.conf")

    def address(self):
        return (self.conf.get("options", "HOST"), 
                int(self.conf.get("options", "PORT")))

    def maxConn(self):  
        return int(self.conf.get("options", "MAX_CONNECTIONS"))
        
    def adminName(self):
        return self.conf.get("users", "ADMIN")
        
    def stopList(self):
        return self.conf.get("users", "STOPLIST").split('; ')
        
    def logRoot(self):
        return self.conf.get("logging", "LOG_ROOT")
        
    def errorLog(self):
        return self.conf.get("logging", "ERROR_LOG")
        
    def transferLog(self):
        return self.conf.get("logging", "TRANSFER_LOG")
    
    def DB(self):
        return self.conf.get("database", "DATABASE")


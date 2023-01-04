import json

class Config:
    token    = ''
    admins   = []

    def __init__(self):
        self.readConfig()
        pass

    def readConfig(self):
        with open('config.json', 'r') as fd:
            config      = json.load(fd)
            self.token  = self.readToken(config)
            self.admins = self.readAdmins(config)


    def readToken(self, cfg):
        with open (cfg['tkfile'], 'r') as f:
            return f.readline().strip('\n')

    def readAdmins(self, cfg):
        return [admin for admin in cfg['bot']['admins']]

    def isAdmin(self, userId):
        return (userId in self.admins)



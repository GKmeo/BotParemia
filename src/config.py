import json

class Config:
    token    = ''
    admins   = []

    def __init__(self, cfgfn):
        self.readConfig(cfgfn)

    def readConfig(self, cfgfn):
        with open(cfgfn, 'r') as fd:
            config         = json.load(fd)
            self.token     = self.readToken(config)
            self.admins    = self.readAdmins(config)
            self.scrapurls = self.readUrls(config)

    def readToken(self, cfg):
        with open (cfg['tkfile'], 'r') as f:
            return f.readline().strip('\n')

    def readAdmins(self, cfg):
        return [admin for admin in cfg['bot']['admins']]

    def readUrls(self, cfg):
        ret  = {}
        urls = cfg['scraper']['urls']
        base = urls['base']
        ret['listado']  = base + urls['listado']
        ret['busqueda'] = base + urls['busqueda']
        return ret

    def getToken(self):
        return self.token

    def isAdmin(self, userId):
        return (userId in self.admins)



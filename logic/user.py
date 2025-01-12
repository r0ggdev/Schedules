class User:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.lastName = ''
        self.career = ''
        self.site = ''

    def setCode(self, code):
        self.code = code
    
    def setName(self, name):
        self.name = name

    def setLastName(self, lastName):
        self.lastName = lastName

    def setCareer(self, career):
        self.career = career

    def setSite(self, site):
        self.site = site

    def getUser(self):
        return {
            'code': self.code,
            'name': self.name,
            'lastName': self.lastName,
            'career': self.career,
            'site': self.site
        }
    
    def loadUser(self, data):
        self.code = data['code']
        self.name = data['name']
        self.lastName = data['lastName']
        self.career = data['career']
        self.site = data['site']
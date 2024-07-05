class User:
    
    
    def __init__(self,id,name,access):
        self.id = id
        self.name = name
        self.access = access
        self.usuarios = {}
    
    def getName(self):
        return self.name
    
    def getAccess(self):
        return self.access
    
    def register(self,(id,name),password):
        if (self.id,self.name) not in self.usuarios:
            self.usuarios[(self.id,self.name)] = password
        else:
            raise Exception("Usuário já registrado")
    
    
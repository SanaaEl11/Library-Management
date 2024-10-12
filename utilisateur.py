import pickle
class Utilisateur:
    def __init__(self,login:str,pwd:str,type: str="") -> None:
        self.setLogin(login)
        self.setPwd(pwd)
        self.setType(type)
        
    def setLogin(self,login):
        self.__login=login
    def getLogin(self):
        return self.__login
    
    def setPwd(self,pwd):
        self.__pwd=pwd
    def getPwd(self):
        return self.__pwd
    
    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type
    
    def __str__(self) -> str:
        return self.__login+'\t'+self.__pwd+'\t'+self.__type
    
    def afficherInterface(self):
        pass
    
    def authentifier(self):
        from admine import Admine
        from buyer import Buyer
        from seller import Seller
        try:

           self.chargerUsers()
           item:Utilisateur
           u:Utilisateur=None
           for item in self.users:
               if item.getLogin()==self.__login and item.getPwd()==self.__pwd:
                   if item.getType()=='admine':
                        u=Admine(item.getLogin(),item.getPwd(),item.getType())
                        u.users=self.users
                        u.afficherInterface()
                   elif item.getType()=='buyer':
                        u=Buyer(item.getLogin(),item.getPwd(),item.getType())
                        u.afficherInterface()
                   elif item.getType()=='seller':
                       u=Seller(item.getLogin(),item.getPwd(),item.getType())
                       u.afficherInterface()
        except Exception as ex:
            print(ex)
            fichier=open("users.bin","wb")
            self.users=list()
            self.users.append(Utilisateur("admine","admine","admine"))
            pickle.dump(self.users,fichier)
            fichier.close() 
            self.authentifier() 
        
        
    def chargerUsers(self):
        fichier=open("users.bin","rb")
        self.users=pickle.load(fichier)
        fichier.close()
        
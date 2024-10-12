from utilisateur import Utilisateur
from form_admine import FormAdmine
import pickle
class Admine(Utilisateur):
    def __init__(self,login:str,pwd:str,type:str)->None:
        super().__init__(login,pwd,type)
    def afficherInterface(self):
        FormAdmine(self)

    
    def ajouter(self,u:Utilisateur):
        self.users.append(u)

    def enregistrer(self):
        fichier=open("users.bin","wb")
        pickle.dump(self.users,fichier)
        fichier.close()
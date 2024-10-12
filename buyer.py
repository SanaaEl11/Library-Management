from utilisateur import Utilisateur
from form_buyer import FormBuyer
from depot import Depot
class Buyer(Utilisateur):
    def __init__(self,login:str,pwd:str,type:str)->None:
        super().__init__(login,pwd,type)
        self.depot=Depot("ista","khemisset")
    def afficherInterface(self):
        FormBuyer(self)
    def searchbyTitre(self,titre):
        return self.depot.searchbyTitre(titre)
    def searchbyPrice(self,prix):
        return self.depot.searchbyPrice(prix)

    
    
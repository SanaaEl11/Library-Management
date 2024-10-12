from utilisateur import Utilisateur
from form_seller import FormSeller
from depot import Depot
class Seller(Utilisateur):
    def __init__(self,login:str,pwd:str,type:str)->None:
        super().__init__(login,pwd,type)
        self.depot=Depot("ista","khemisset")
    def afficherInterface(self):
        FormSeller(self)
    def add(self,document):
        self.depot.add(document)
    def save(self):
        self.depot.save()
    def load(self):
        self.depot.load()
    def remove(self,document):
        self.depot.remove(document)
    def exists(self,id)->bool:
        return self.depot.exists(id)
    def searchbyId(self,id):
        return self.depot.searchbyId(id)


from document import Document
class Cd(Document):
    def __init__(self, titre: str, prix:float,capaciter:float,type:str):
        super().__init__(titre, prix)
        self.setCapaciter(capaciter)
        self.setType(type)

   

    def getCapaciter(self):
        return self.__capaciter
    
    
    def setCapaciter(self,capaciter:float):
        if capaciter>0:
            self.__capaciter=capaciter
        else:
            raise Exception("Attention le type de CD doit être strictement positif !")
        
    def getType(self):
        return self.__type
    
    def setType(self,type:str):
        if len(type)>0 :
            self.__type=type
        else:
            raise Exception("attention le champ de  capaciter ne doit pas etre vide!")
        
    def __str__(self):
        return super().__str__()+'\t'+str(self.__capaciter) +'\t'+self.__type+'\t'

    
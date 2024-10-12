from document import Document
class Livre(Document):
    def __init__(self, titre: str, prix: float,auteur:str,nombredepage:float):
        super().__init__(titre, prix)
        self.setAuteur(auteur)
        self.setNombredepage(nombredepage)

    
    def __str__(self):
        return super().__str__()+'\t'+self.__auteur +'\t'+str(self.__nombredepage)+'\t'
    
    def getAuteur(self):
        return self.__auteur          
    def setAuteur(self,auteur:str):
        if len(auteur)>0:
            self.__auteur=auteur
        else:
            raise Exception("attention le champ de  auteur ne doit pas etre vide!")
        
    def getNombredepage(self):
        return self.__nombredepage
    
    def setNombredepage(self,nombredepage:float):
        if nombredepage>0 :
            self.__nombredepage=nombredepage
        else:
            raise Exception("Attention le nombre des pages doit etre strictement positif !")
   
 

    

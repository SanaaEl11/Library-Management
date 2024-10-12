class Document:
    x=0
    def __init__(self,titre:str,prix:float):
        Document.x=Document.x+1
        self.setId(Document.x)
        self.setTitre(titre)
        self.setPrix(prix)

    def afficherVertical(self):
        print('Id='+str(self.__id))
        print('titre='+(self.__titre))
        print('prix='+str(self.__prix))



    def afficherHorizontal(self):
       print(self)

    def __str__(self) :
        return  str(self.__id)+'\t'+ self.__titre + '\t' +str(self.__prix)
    
    def getId(self):
        return self.__id 
    
    def setId(self,id):
        if id >0 and id<100:
            self.__id=id
        else:
            raise Exception("Attention l'Id doit être compris entre 1 et 99 !")

    def getTitre(self):
        return self.__titre
    
    def setTitre(self,titre:str):
        if len(titre)>0:
            self.__titre=titre 
        else:
            raise Exception("Attention la titre ne doit pas être vide !")
        
    def getPrix(self):
        return self.__prix
    
    def setPrix(self,prix:float):
        if prix>0 :
            self.__prix=prix
        else:
            raise Exception("Attention le prix doit être strictement positif !")
    
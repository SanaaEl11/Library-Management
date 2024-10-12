from document import Document
import pickle
class Depot:
    def __init__(self,nom,adresse) :
        self.__nom=nom
        self.__adresse=adresse
        self.__documents=list()
    def getNom(self):
        return self.__nom
    def getAdresse(self):
        return self.__adresse
    def getdocuments(self):
        return self.__documents

    def setNom(self,nom):
        if len(nom)>0:
            self.__nom=nom
        else:
            raise Exception("Le nom ne doit pas être vide !")

    def setAdresse(self,adresse):
        if len(adresse)>0:
            self.__adresse=adresse
        else:
            raise Exception("L'adresse ne doit pas être vide !")
    
    def __str__(self) -> str:
        return self.__nom + " à l'adresse : "+self.__adresse +'\n'

    
    def add(self,document:Document):
        if not self.exists(document.getId()):
            self.__documents.append(document)
        else:
            raise Exception("Il existe deja un document avec le meme ID dans la liste !")

    def remove(self,document:Document):
        self.__documents.remove(document)

    def save(self):
        fichier=open("document.bin","wb")
        pickle.dump(self.__documents,fichier)
        fichier.close()

    def load(self):
        fichier=open("document.bin","rb")
        self.__documents=pickle.load(fichier)
        fichier.close()
        Document.x=self.getMaxId()
        print()
        
    def show(self):
        print(self)    
        for item in self.__documents :
            item.afficherHorizontal()
            
    def exists(self,id)->bool:
        for document in self.__documents:
            if document.getId()==id:
                return True                
        return False        

    def searchbyId(self,id)->Document:
        for document in self.__documents:
            if document.getId()==id:
                return document
            
    def searchbyTitre(self,titre:str)->list:
        l=list()
        lnom=titre.lower()
        for document in self.__documents:
            s:str=document.getTitre().lower()
            if s.startswith(lnom):
                l.append(document)
        return l
            
    def searchbyPrice(self,prix:float)->list:
        l=list()
        for document in self.__documents:
            x:float=document.getPrix()==prix
            if x:
                l.append(document)
        return l  
    
    def getMaxId(self)->int:
        m=self.__documents[0].getId()
        for i in range(1,len(self.__documents)):
            if self.__documents[i].getId()>m:
                m=self.__documents[i].getId()
        return m
    
    
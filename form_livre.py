import tkinter as tk
from depot import Depot
from tkinter import messagebox as msg
from livre import Livre
from document  import Document
from tkinter import tix
class FormLivre:
    def __init__(self,seller) -> None:
        self.seller=seller
        try:
            self.seller.load()
        except Exception as ex:
            msg.showwarning("Warning",ex)
        self.depot=self.seller.depot
        self.currentLivre:Livre=None
        self.root=tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("info Livre")
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg='blue')
        self.lblBienvenu=tk.Label(self.root,text=" Gestion des  'Livre'",
        font="Arial 16 bold",fg="black",bg='blue')
        self.lblBienvenu.pack()
        self.frameInfoLivre=tk.LabelFrame(self.root,text="Info Livre: ",font=("Arial","16","bold","italic"),padx=20,
                                          pady=10,relief='solid',bg="orange",bd=10)
        self.frameInfoLivre.pack(expand=1)

        self.lblTitre=tk.Label(self.frameInfoLivre,text="Titre: ",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblTitre.grid(row=0,column=0,sticky=tk.W)
        self.entryTitre=tk.Entry(self.frameInfoLivre,foreground="black",font="Arial 16 bold")
        self.entryTitre.grid(row=0,column=1)

        self.lblPrix=tk.Label(self.frameInfoLivre,text="Prix: ",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblPrix.grid(row=1,column=0,sticky=tk.W)        
        self.entryPrix=tk.Entry(self.frameInfoLivre,foreground="black",font="Arial 16 bold")
        self.entryPrix.grid(row=1,column=1)

        self.lblAuteur=tk.Label(self.frameInfoLivre,text="Auteur: ",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblAuteur.grid(row=2,column=0,sticky=tk.W)        
        self.entryAuteur=tk.Entry(self.frameInfoLivre,fg="black",font="Arial 16 bold")
        self.entryAuteur.grid(row=2,column=1)

        self.lblNombrepage=tk.Label(self.frameInfoLivre,text="Nombre de page: ",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblNombrepage.grid(row=3,column=0,sticky=tk.W)        
        self.entryNombrepage=tk.Entry(self.frameInfoLivre,foreground="black",font="Arial 16 bold")
        self.entryNombrepage.grid(row=3,column=1)
        
        #les buttons:
        self.frameButton= tk.LabelFrame(self.root,text="Action: ",
        font="Arial 14 bold italic",padx=10,pady=10,relief="flat",bd=10,bg='blue' )
        self.frameButton.pack()

        self.btnAdd=tk.Button(self.frameButton,text="Ajouter",font="Arial 15 bold",bd=10,
                              bg="black",fg="white",command=self.add)
        self.btnAdd.pack(side=tk.LEFT)
        
        self.btnShow=tk.Button(self.frameButton,text="Afficher",font="Arial 15 bold",bd=10,bg="black",
                               fg="white",command=self.show)
        self.btnShow.pack(side=tk.LEFT)
        
        self.btnLoad=tk.Button(self.frameButton,text="Charger",font="Arial 15 bold",bd=10,bg="black",fg="white"
                               ,command=self.load)
        self.btnLoad.pack(side=tk.LEFT)

        self.btnSave=tk.Button(self.frameButton,text="Enregistrer",font="Arial 15 bold",bd=10,bg="black",
                               fg="white",command=self.save)
        self.btnSave.pack(side=tk.LEFT)

        self.btnDelete=tk.Button(self.frameButton,text="Supprimer",font="Arial 15 bold",bd=10,bg="black",
                                 fg="white",command=self.delete)
        self.btnDelete.pack(side=tk.LEFT)

        self.btnSearch=tk.Button(self.frameButton,text="Chercher",font="Arial 15 bold",bd=10,bg="black"
                                 ,fg="white",command=self.search)
        self.btnSearch.pack(side=tk.LEFT)
        
        self.btnModifier=tk.Button(self.frameButton,text="Modifier",bg="black",bd=10,font="Arial 16 bold italic" ,
                                   fg="white",command=self.modify)
        self.btnModifier.pack(side=tk.LEFT)


        self.btnEffacer=tk.Button(self.frameButton,text="Effacer",
        bg="black",bd=10,font="Arial 16 bold italic" ,fg="white",command=self.deleteEntry)
        self.btnEffacer.pack(side=tk.LEFT)

        
        #pour chercher par id
        self.frameSearch=tk.LabelFrame(self.root,text="Recherche",
         font="Arial 16 bold italic",bd=3, relief="solid",padx=20,pady=20)
        
        self.lblIdSearch=tk.Label(self.frameSearch,text="Id")
        self.lblIdSearch.grid(row=0,column=0)
        
        self.entryIdSearch=tk.Entry(self.frameSearch,width=50)
        self.entryIdSearch.grid(row=0,column=1)

        self.btnOkSearch=tk.Button(self.frameSearch,text="Ok",fg="white",
            width=10,bg="black",bd=2 ,font="calibri 13 bold",command=self.okSearch)
        self.btnOkSearch.grid(row=1,column=0)
        self.btnAnnulerSearch=tk.Button(self.frameSearch,text="Annuler",width=10,bg="black",
        bd=2 ,font="calibri 13 bold",fg="white",command=self.cancelSearch)
        self.btnAnnulerSearch.grid(row=1,column=1)

        self.btnFermer=tk.Button(self.root,text="Fermer",bg="orange",
        bd=10,font="Arial 15 bold italic",fg="white",command=self.root.destroy)
        self.btnFermer.pack(side=tk.BOTTOM)


        self.root.mainloop()
    def add(self):
        try:
            self.seller.add(Livre(self.entryTitre.get(),
            float(self.entryPrix.get()),self.entryAuteur.get(),float(self.entryNombrepage.get())))
            self.deleteEntry()
            self.entryTitre.focus()
        except Exception as ex:
            msg.showwarning("Attention",ex)
    def deleteEntry(self):
        self.entryTitre.delete(0,tk.END)
        self.entryPrix.delete(0,tk.END)
        self.entryAuteur.delete(0,tk.END)
        self.entryNombrepage.delete(0,tk.END)

    
    def show(self):
        fenetre=tix.Tk()
        fenetre.geometry("680x200")
        fenetre.title("Liste des livres")
        sw=tix.ScrolledWindow(fenetre)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        livre:Livre=None
        for item in self.seller.depot.getdocuments():
            if isinstance(item,Livre):
                livre=item
                entryId=tk.Entry(sw.window,font="Arial 12 bold", fg="black",width=4)
                entryId.insert(0,livre.getId())
                entryId.grid(row=i,column=0)

                entryTitre=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryTitre.insert(0,livre.getTitre())
                entryTitre.grid(row=i,column=1)

                entryPrix=tk.Entry(sw.window,font="Arial 12 bold", fg="black",width=6)
                entryPrix.insert(0,livre.getPrix())
                entryPrix.grid(row=i,column=2)

                entryColor=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryColor.insert(0,livre.getAuteur())
                entryColor.grid(row=i,column=3)

                entryNombrepage=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryNombrepage.insert(0,livre.getNombredepage())
                entryNombrepage.grid(row=i,column=4)
                i+=1

        fenetre.mainloop()
    def load(self):
        self.seller.load()
    def save(self):
        self.seller.save()
    
    def delete(self):
        if msg.askyesno("confirmation","etes vous sur de vouloir suprimer?"):
            self.depot.remove(self.currentLivre)
            self.deleteEntry()

    def modify(self):
        if msg.askyesno("Confirmation","Etes vous sûr de vouloir Modifier ? "):
            try:
                self.currentLivre.setTitre(self.entryTitre.get())
                self.currentLivre.setPrix(float(self.entryPrix.get()))
                self.currentLivre.setAuteur(self.entryAuteur.get())
                self.currentLivre.setNombredepage(float(self.entryNombrepage.get()))
            except Exception as ex:
                msg.showwarning("Attention",ex)

    def search(self):
        self.frameSearch.pack()


    def cancelSearch(self):
        self.frameSearch.pack_forget()

    def okSearch(self):
        self.deleteEntry()
        try:

            if self.depot.exists(int(self.entryIdSearch.get())):
                self.currentLivre=self.depot.searchbyId(int(self.entryIdSearch.get()))
                self.entryTitre.insert(0,self.currentLivre.getTitre())
                self.entryPrix.insert(0,self.currentLivre.getPrix())
                self.entryAuteur.insert(0,self.currentLivre.getAuteur())
                self.entryNombrepage.insert(0,self.currentLivre.getNombredepage())

            else:
                msg.showinfo("Message","livre n'existe pas")
        except Exception as ex:
            msg.showwarning("Error",ex)
        self.frameSearch.pack_forget()


    

    

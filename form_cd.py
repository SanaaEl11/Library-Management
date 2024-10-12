import tkinter as tk
from depot import Depot
from tkinter import messagebox as msg
from tkinter import tix
from document import Document
from cd import Cd
class FormCd:
    def __init__(self,seller) -> None:
        self.seller=seller
        try:
            self.seller.load()
        except Exception as ex:
            msg.showwarning("Warning",ex)
        self.depot=self.seller.depot
        #self.depot=Depot("ista","khemisset")
        self.currentCd:Cd=None
        self.root=tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Info CD")
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg='blue')
        self.lblBienvenu=tk.Label(self.root,text="Gestion des CD",font="Arial 16 bold",fg="black",bg='blue')
        self.lblBienvenu.pack()

        self.frameinfoCd=tk.LabelFrame(self.root,text="Info CD:",font=("Arial","16","bold","italic"),padx=20,
                                          pady=10,relief='solid',bg="orange",bd=10)
        self.frameinfoCd.pack(expand=1)

        self.lblTitre=tk.Label(self.frameinfoCd,text="titre: ",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblTitre.grid(row=0,column=0,sticky=tk.W)

        self.entryTitre=tk.Entry(self.frameinfoCd,fg="black",font="Arial 15 bold")
        self.entryTitre.grid(row=0,column=1)

        self.lblPrix=tk.Label(self.frameinfoCd,text="Prix:",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblPrix.grid(row=1,column=0 ,sticky=tk.W)

        self.entryPrix=tk.Entry(self.frameinfoCd,fg="black",font="Arial 15 bold")
        self.entryPrix.grid(row=1,column=1)

        self.lblCapaciter=tk.Label(self.frameinfoCd,text="Capaciter:",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblCapaciter.grid(row=2,column=0 ,sticky=tk.W)

        self.entryCapaciter=tk.Entry(self.frameinfoCd,fg="black",font="Arial 15 bold")
        self.entryCapaciter.grid(row=2,column=1)

        self.lblType=tk.Label(self.frameinfoCd,text="Type:",foreground="black",font="Arial 16 bold",bg="orange")
        self.lblType.grid(row=3,column=0 ,sticky=tk.W)

        self.entryType=tk.Entry(self.frameinfoCd,fg="black",font="Arial 15 bold")
        self.entryType.grid(row=3,column=1)


       

        #les buttons:
        self.frameButton=tk.LabelFrame(self.root,text="Action",
            font="Arial 14 bold italic",padx=10,pady=10,relief="flat",bd=10,bg='blue' )
        self.frameButton.pack(expand=1)

        self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",font="Arial 15 bold",bd=10,
                              bg="black",fg="white",command=self.add)
        self.btnAjouter.pack(side=tk.LEFT)
        
        self.btnAfficher=tk.Button(self.frameButton,text="Afficher",
        bg="black",bd=10,font="Arial 15 bold italic",fg="white",
        command=self.show)
        self.btnAfficher.pack(side=tk.LEFT)

        self.btnEnregistrer=tk.Button(self.frameButton,text="Enregistrer",
        bg="black",bd=10,font="Arial 15 bold italic" ,
        fg="white",command=self.save)
        self.btnEnregistrer.pack(side=tk.LEFT)

        self.btnChercher=tk.Button(self.frameButton,text="chercher",
        bg="black",bd=10,font="Arial 15  bold italic",fg="white",
        command=self.search)
        self.btnChercher.pack(side=tk.LEFT)

        self.btnModifier=tk.Button(self.frameButton,text="Modifier",
        bg="black",bd=10,font="Arial 15 bold italic" ,
        fg="white",command=self.modify)
        self.btnModifier.pack(side=tk.LEFT)

        self.btnCharger=tk.Button(self.frameButton,text="Charger",
        bg="black",bd=10,font="Arial 15 bold italic" ,fg="white",command=self.load)
        self.btnCharger.pack(side=tk.LEFT)

        self.btnEffacer=tk.Button(self.frameButton,text="Effacer",
        bg="black",bd=10,font="Arial 15 bold italic" ,fg="white",
        command=self.deleteEntry)
        self.btnEffacer.pack(side=tk.LEFT)

        self.btnSuprimer=tk.Button(self.frameButton,text="Suprimer",
        bg="black",bd=10,font="Arial 16 bold italic" ,
        fg="white",command=self.delete)
        self.btnSuprimer.pack(side=tk.LEFT)

        #fenetre pour chercher un produit
        self.frameSearch=tk.LabelFrame(self.root,text="Rechercher",
        font="Arial 16 bold italic",bd=3, relief="solid",padx=20,pady=20)
        

        self.lblIdPeSearch=tk.Label(self.frameSearch,text="Id Cd: ")
        self.lblIdPeSearch.grid(row=0,column=0)

        self.entryIdSearch=tk.Entry(self.frameSearch,width=50)
        self.entryIdSearch.grid(row=0,column=0)

        self.btnOkSearch=tk.Button(self.frameSearch,text="ok",fg="white",
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
            self.seller.add(Cd(self.entryTitre.get(),
            float(self.entryPrix.get()),float(self.entryCapaciter.get()),self.entryType.get()))
            self.deleteEntry()
            self.entryTitre.focus()
        except Exception as ex:
            msg.showwarning("Attention ",ex)

    def deleteEntry(self):
        self.entryTitre.delete(0,tk.END)
        self.entryPrix.delete(0,tk.END)
        self.entryCapaciter.delete(0,tk.END)
        self.entryType.delete(0,tk.END)
        
        

    def show(self):
        fenetre=tix.Tk()
        fenetre.geometry("680x200")
        fenetre.title("Liste des Cd")
        sw=tix.ScrolledWindow(fenetre)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        cd:Cd=None
        for item in self.depot.getdocuments():
            if isinstance(item,Cd):
                cd=item
                entryId=tk.Entry(sw.window,font="Arial 12 bold", fg="black",width=4)
                entryId.insert(0,cd.getId())
                entryId.grid(row=i,column=0)

                entryTitre=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryTitre.insert(0,cd.getTitre())
                entryTitre.grid(row=i,column=1)

                entryPrix=tk.Entry(sw.window,font="Arial 12 bold", fg="black",width=6)
                entryPrix.insert(0,cd.getPrix())
                entryPrix.grid(row=i,column=2)

                entryCapaciter=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryCapaciter.insert(0,cd.getCapaciter())
                entryCapaciter.grid(row=i,column=3)

                entryType=tk.Entry(sw.window,font="Arial 12 bold", fg="black")
                entryType.insert(0,cd.getType())
                entryType.grid(row=i,column=4)
                i+=1

        fenetre.mainloop()
    def save(self):
        self.seller.save()

    def load(self):
        self.seller.load()

    def delete(self):
        if msg.askyesno("confirmation","etes vous sur de vouloir suprimer?"):
            self.depot.remove(self.currentCd)
            self.deleteEntry()

    def modify(self):
        if msg.askyesno("confirmation","etes vous sur de vouloir modifier?"):
            try:
                self.currentCd.setTitre(self.entryTitre.get())
                self.currentCd.setPrix(float(self.entryPrix.get()))
                self.currentCd.setCapaciter(float(self.entryCapaciter.get()))
                self.currentCd.setType(self.entryType.get())
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
                self.currentCd=self.depot.searchbyId(int(self.entryIdSearch.get()))
                self.entryTitre.insert(0,self.currentCd.getTitre())
                self.entryPrix.insert(0,self.currentCd.getPrix())
                self.entryCapaciter.insert(0,self.currentCd.getCapaciter())
                self.entryType.insert(0,self.currentCd.getType())
            else:
                msg.showinfo("Message","cd n'existe pas")
        except Exception as ex:
            msg.showwarning("Error",ex)
        self.frameSearch.pack_forget()




    
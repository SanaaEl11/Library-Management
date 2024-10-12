import tkinter as tk
from tkinter import tix
from livre import Livre
class FormNom:
    def __init__(self,buyer) -> None:
        from buyer import Buyer
        self.buyer:Buyer=buyer
        self.depot=self.buyer.depot
        self.depot.load()
        # self.depot=Depot("ista","khemisset")
        self.root=tk.Tk()
        self.root.geometry("800x500")
        self.root.title(" form buyer : chercher des documents")
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg='blue')
        self.lblBienvenu=tk.Label(self.root,text="cherchers des documment Livre",
        font="Arial 16 bold",pady=10,bg='blue')
        self.lblBienvenu.pack()

        self.frameSearchT=tk.LabelFrame(self.root,text="Recherche",
        font="Arial 16 bold",bd=10,padx=25,pady=25,bg="orange",relief='solid',border=3)
        self.frameSearchT.pack(expand=1)
        self.lblSearchT=tk.Label(self.frameSearchT,text="Titre:",font="Arial 17 bold",fg="black")
        self.lblSearchT.grid(row=0,column=0)
        
        self.entrySearchT=tk.Entry(self.frameSearchT,font="Arial 16 bold",width=20,relief='solid',border=3)
        self.entrySearchT.grid(row=0,column=1)

        self.btnOkSearchT=tk.Button(self.frameSearchT,text="Ok",font="Arial 16 bold",width=10,fg="white",bg="black",command=self.searchbyTitre)
        self.btnOkSearchT.grid(row=1,column=1)
        

        self.btnFermer=tk.Button(self.root,text="Fermer",font="Arial 16 bold",bd=10,bg="orange",fg="black",command=self.root.destroy)
        self.btnFermer.pack(side=tk.BOTTOM)
        
        self.root.mainloop()

    
    def searchbyTitre(self):
        fenetre=tix.Tk()
        fenetre.geometry("680x200")
        fenetre.title("Liste des livres")
        sw=tix.ScrolledWindow(fenetre)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        for document in self.buyer.searchbyTitre(self.entrySearchT.get()):
            if isinstance(document,Livre):
                livre=document
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

import tkinter as tk
from tkinter import tix
from depot import Depot
from cd import Cd
class FormPrix:
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

        self.frameSearchP=tk.LabelFrame(self.root,text="Recherche",
        font="Arial 16 bold",bd=10,padx=25,pady=25,bg="orange",relief='solid',border=3)
        self.frameSearchP.pack(expand=1)
        self.lblSearchP=tk.Label(self.frameSearchP,text="Prix:",font="Arial 16 bold",bg="orange",fg="black")
        self.lblSearchP.grid(row=0,column=0)
        
        self.entrySearchP=tk.Entry(self.frameSearchP,font="Arial 16 bold",width=20,relief='solid',border=3)
        self.entrySearchP.grid(row=0,column=1)

        self.btnOkSearchP=tk.Button(self.frameSearchP,text="Ok",font="Arial 16 bold",width=20,fg="white",bg="black",command=self.searchbyPrice)
        self.btnOkSearchP.grid(row=1,column=1)
        

        self.btnFermer=tk.Button(self.root,text="Fermer",font="Arial 16 bold"
                    ,bd=10,bg="orange",fg="black",command=self.root.destroy)
        self.btnFermer.pack(side=tk.BOTTOM)
        
        self.root.mainloop()
        

    def searchbyPrice(self,prix):
        fenetre=tix.Tk()
        fenetre.geometry("680x200")
        fenetre.title("Liste des livres")
        sw=tix.ScrolledWindow(fenetre)
        sw.pack(expand=1,fill=tk.BOTH)
        i=0
        for document in self.buyer.searchbyPrice(self.entrySearchP.get()):
            if isinstance(document,Cd):
                cd=document
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

   
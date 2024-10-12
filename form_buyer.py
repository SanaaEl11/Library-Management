import tkinter as tk
from form_prix import FormPrix
from form_nom import FormNom
from utilisateur import Utilisateur
class FormBuyer:
    def __init__(self,buyer:Utilisateur) -> None:
        self.buyer=buyer
        # self.depot=self.buyer
        self.root=tk.Tk()
        self.root.geometry("800x500")
        self.root.title("first form : Gestion des documents")
        self.root.configure(bg='blue') 
        self.root.iconbitmap("icon.ico")
        self.lblBienvenu=tk.Label(self.root,text="chercher des documents:",font="Arial 16 bold",pady=10,bg='blue')
        self.lblBienvenu.pack()

        self.frameButton=tk.Frame(self.root,bg="white",padx=10,pady=10)
        self.frameButton.pack(expand=1)
        #self.btnSearchTitre.bind("<<Enter>>",nom de btn,"<comboboxSelected>>")
        self.btnSearchTitre=tk.Button(self.frameButton,text="Chercher par titre",font="Arial 14 bold",bg="orange",
                             fg="black",bd=10,width=25,command=self.openforTitre)
        self.btnSearchTitre.pack(side="left")
        self.btnSearchPrix=tk.Button(self.frameButton,text="Chercher par prix",font="Arial 14 bold",bg="orange",
                             fg="black",bd=10,width=25,command=self.openforPrix)
        self.btnSearchPrix.pack(side="left")


        self.btnQuitter=tk.Button(self.root,text="Quitter",
        font="Arial 14 bold",bg="black",fg="white",bd=10,command=self.root.destroy)
        self.btnQuitter.pack(side=tk.BOTTOM)
        self.root.mainloop()

      
    def openforTitre(self):
        FormNom(self.buyer)
    def openforPrix(self):
        FormPrix(self.buyer)
    
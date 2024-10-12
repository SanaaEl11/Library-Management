import tkinter as tk
from form_livre import FormLivre
from form_cd import FormCd
class FormSeller:
    def __init__(self,seller) -> None:
        self.seller=seller
        self.root=tk.Tk()
        self.root.geometry("800x500")
        self.root.title("first form : Gestion des documents")
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg='blue')
        self.lblBienvenu=tk.Label(self.root,text="Bienvenu dans l'application Gestion des documment",
        font="Arial 16 bold",pady=10,bg='blue')
        self.lblBienvenu.pack()

        self.frameButton=tk.Frame(self.root,bg="white",padx=10,pady=10)
        self.frameButton.pack(expand=1)

        self.btnLivre=tk.Button(self.frameButton,text="Gestion des livres",font="Arial 14 bold",bg="orange",
                                fg="black",bd=10,width=25,command=self.openFormLivre)
        self.btnLivre.pack(side="left")

        self.btnCd=tk.Button(self.frameButton,text="Gestion des CD",font="Arial 14 bold",bg="orange",
                             fg="black",bd=10,width=25,command=self.openFormCd)
        self.btnCd.pack(side="left")

        self.btnQuitter=tk.Button(self.root,text="Quitter",
        font="Arial 14 bold",bg="black",fg="white",bd=10,command=self.root.destroy)
        self.btnQuitter.pack(side=tk.BOTTOM)
        self.root.mainloop()
    
    
    def openFormLivre(self):
        FormLivre(self.seller)
    
    def openFormCd(self):
        FormCd(self.seller)
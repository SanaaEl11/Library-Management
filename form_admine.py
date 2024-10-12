import tkinter as tk
from utilisateur import Utilisateur
from tkinter import messagebox as msg
class FormAdmine:
    def __init__(self,admine:Utilisateur) -> None:
      self.admine=admine
      self.root= tk.Tk()
      self.root.geometry('600x400')
      self.root.title("Formulaire Gestion des Utilisateurs")
      self.root.configure(bg='blue') 
      self.frameAuth=tk.LabelFrame(self.root,text="info utilisateur",padx=30,pady=30,fg="black",font="Arial 16 bold",bg='white',relief="solid",bd=2)
      self.frameAuth.pack(expand=1)

      self.lblLogin=tk.Label(self.frameAuth,text="Login",fg="black",font="Arial 12 bold",bg='white')
      self.lblLogin.grid(row=0,column=0,sticky=tk.NW)

      self.entryLogin=tk.Entry(self.frameAuth,relief="solid",bd=2)
      self.entryLogin.grid(row=0,column=1)

      self.lblPwd=tk.Label(self.frameAuth,text="Password",fg="black",font="Arial 12 bold",bg='white')
      self.lblPwd.grid(row=1,column=0,sticky=tk.NW)

      self.entryPwd=tk.Entry(self.frameAuth,relief="solid",bd=2)
      self.entryPwd.grid(row=1,column=1)

      self.lblType=tk.Label(self.frameAuth,text="Type",fg="black",font="Arial 12 bold",bg='white')
      self.lblType.grid(row=2,column=0,sticky=tk.NW)

      self.entryType=tk.Entry(self.frameAuth,relief="solid",bd=2)
      self.entryType.grid(row=2,column=1)

      self.frameButton=tk.Frame(self.root)
      self.frameButton.pack()
      self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",fg="white",bg="black",font="Arial 15 bold",command=self.ajouter)
      self.btnAjouter.pack(side=tk.LEFT)
      self.btnEnregistrer=tk.Button(self.frameButton,text="Enregistrer",fg="white",bg="black",font="Arial 15 bold",command=self.enregistrer)
      self.btnEnregistrer.pack(side=tk.LEFT)
      

      self.root.mainloop()

    def ajouter(self):
        self.admine.ajouter(Utilisateur(self.entryLogin.get(),self.entryPwd.get(),self.entryType.get()))

    def enregistrer(self):
        self.admine.enregistrer()
        msg.showinfo("enregistrer:","enregistrement reussi")
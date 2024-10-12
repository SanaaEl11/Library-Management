import tkinter as tk
from utilisateur import Utilisateur
class FormLog:
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Formulaire de Login")
        self.root.configure(bg='blue') 
        self.frameAuthe=tk.LabelFrame(self.root,text="authentification ",padx=30,pady=40,fg="black",font="Arial 16 bold",bg='white',relief="solid",bd=2)
        self.frameAuthe.pack(expand=1)

        self.lblLogin=tk.Label(self.frameAuthe,text="Login",fg="black",font="Arial 12 bold",bg='white')
        self.lblLogin.grid(row=0,column=0,sticky=tk.NW)

        self.entryLogin=tk.Entry(self.frameAuthe,relief="solid",bd=2)
        self.entryLogin.grid(row=0,column=1)

        self.lblPwd=tk.Label(self.frameAuthe,text="Password",fg="black",font="Arial 12 bold",bg='white')
        self.lblPwd.grid(row=1,column=0,sticky=tk.NW)

        self.entryPwd=tk.Entry(self.frameAuthe,show="*",relief="solid",bd=2)
        self.entryPwd.grid(row=1,column=1)


        self.btnOk=tk.Button(self.frameAuthe,text="ok",fg="white",bg="blue",font="Arial 12 bold",padx=20,command=self.ok)
        self.btnOk.grid(row=2,column=0,columnspan=2,sticky=tk.NSEW)
        self.root.mainloop()

    def ok(self):
        utilisateur=Utilisateur(self.entryLogin.get(),self.entryPwd.get())
        utilisateur.authentifier()
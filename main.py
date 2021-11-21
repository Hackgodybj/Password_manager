try:
    import pbkdf2,pymysql,secrets,pyaes,PIL,pyperclip
    from tkinter import *
    import os.path
    import Signup_system
    import pymysql
    from tkinter import messagebox
    from PIL import ImageTk, Image
except :
    import install_dependencies
    from tkinter import *
    import os.path
    import Signup_system
    import pymysql
    from tkinter import messagebox
    from PIL import ImageTk,Image
def main():

    mysql_login=MYSQL_LOGIN()

class MYSQL_LOGIN:
    def __init__(self):
        self.check_file=os.path.join(os.path.abspath(os.path.dirname(__file__)),"mysqlcredentials.txt")
        self.check_in_file()

    def check_in_file(self):
        if not os.path.exists(self.check_file):
           self.mysql_login()
        else:
            with open(self.check_file,"r") as f:
                output=[word.strip("\n") for word in f.readlines()]
                Signup_system.main()


    def mysql_login(self):
        self.root=Tk()
        self.root.title("MySQL Credentials")
        self.root.geometry("300x300+500+100")
        a = ImageTk.PhotoImage(file="pictures_1/mysql_hosting.png")
        self.root.iconphoto(False, a)

        credential_title=Label(self.root,text="MYSQL CREDENTIALS",fg="black",bg="cyan",relief=GROOVE,font=("times new roman",17,"bold")).pack(side=TOP,fill=X)
        host_l = Label(self.root, text="Enter hostname:" ,bg="Lightcyan2").place(x=5,y=40)
        port_l = Label(self.root, text="Enter port_number:",bg="Lightcyan2").place(x=5,y=70)
        user_l = Label(self.root, text="Enter username:",bg="Lightcyan2").place(x=5,y=100)
        pass_l = Label(self.root, text="Enter password: ",bg="Lightcyan2").place(x=5,y=130)

        self.host_e=Entry(self.root,width=20,bg="white")
        self.host_e.insert(0,"localhost")
        self.port_e=Entry(self.root,width=20,bg="white")
        self.port_e.insert(0,"3306")
        self.user_e=Entry(self.root,width=20,bg="white")
        self.user_e.insert(0,"root")
        self.pass_e=Entry(self.root,width=20,bg="white",show="*")
        self.pass_e.insert(0,"")
        self.host_e.place(x=120,y=40)
        self.port_e.place(x=120,y=70)
        self.user_e.place(x=120,y=100)
        self.pass_e.place(x=120,y=130)
       
        exit_btn=Button(self.root,text="Exit",bg="red",fg="black",font=("times new roman",12,"bold"),relief=GROOVE,command=self.root.destroy).place(x=250,y=255)
        check_btn=Button(self.root,text="Check",bg="dodger blue",fg="black",font=("times new roman",15,"bold"),relief=RAISED,command=self.write_details).place(x=110,y=180)

        self.root.mainloop()
    def check_connection(self):
        try:
            con=pymysql.connect(host=self.host_e.get(),port=int(self.port_e.get()),user=self.user_e.get(),passwd=self.pass_e.get())

            return True
        except Exception as es:
            return False
    def write_details(self):
        if not self.check_connection():
            messagebox.showerror("Error","Invalid Details Given!",parent=self.root)
        else:
            with open(self.check_file,"w") as f:
                f.write(self.host_e.get()+"\n"+self.port_e.get()+"\n"+self.user_e.get()+"\n"+self.pass_e.get()+"\n")
                f.close()
                messagebox.showinfo("Congrats","Correct details given!",parent=self.root)
                self.root.destroy()
                Signup_system.main()




if __name__ == '__main__':
    main()

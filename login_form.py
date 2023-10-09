from tkinter import *
from tkinter import messagebox
t=Tk()
t.geometry("500x500")


def main():
    f0=Frame(bg="gray")
    f0.place(x=0,y=0,width=500,height=500)
    
    l0=Label(f0, text="Welcome to Home page",font="Algerian", bg="gray")
    l0.place(x=120,y=90)
    
    b0=Button(f0, text="Sign-Up", command=signup,  font="Roboto" )
    b0.place(x=140,y=140 )
    
    b1=Button(f0, text="Sign-in", command=signin,font="Roboto")
    b1.place(x=240,y=140)

def signin():
    f2=Frame(bg="gray")
    f2.place(x=0,y=0,width=500,height=500)
    
    l1=Label(f2, text="Welcome to Sign-in")
    l1.place(x=200,y=20)
    
    e0=Entry(f2)
    
    e0.place(x=240,y=50)
    u0=Label(f2,text="Enter your name", fg="black",bg="gray")
    u0.place(x=80,y=50, width=130)
    
    e1=Entry(f2)
    e1.place(x=240,y=70)
    u1=Label(f2,text="Email", fg="black",bg="gray")
    u1.place(x=80,y=70, width=130)
     
    e3=Entry(f2,show="*")
    e3.place(x=240,y=90)
    u3=Label(f2,text="Password", fg="black",bg="gray")
    u3.place(x=80,y=90, width=130)
    
    c0=Checkbutton(f2,u3,text="Password" , command="check")
    c0.place(x=120,y=110)

    b1=Button(f2, text="Sign-in", command=lambda: get_value(e0.get(),e1.get(),e3.get()) ) #command=lambda: value(e0.get(),e1.get(),e3.get())
    b1.place(x=200,y=130)
    
    # print(e0.get(), e1.get(), e3.get())
    b1=Button(f2, text="Home",command=main)
    b1.place(x=0,y=0)
    
def get_value(name,email,password):
    f=open("details.txt","r")
    for line in f.readlines():
        x=line.split("|")
        print(x)
        if email in x:
            if password == x[1]:
                print("Success")
                messagebox.showinfo("error", "login successful")
                main()   
            else:
                print("Failed") 
                messagebox.showerror("error", "wrong password") 
        else:
            messagebox.showerror("error", "User does not exist")
 
def add_data(name, email, age, password1, password2):
    if password1 == password2:
        f = open("details.txt", 'a')
        f.write(f"{email}|{password1}|{name}|{age}|\n")
        f.close()
        main()
    else:
        messagebox.showerror("error", "In_correcet_password")
    

def signup():
    f1=Frame(bg="gray")
    f1.place(x=0,y=0,width=500,height=500)
    
    l1=Label(f1, text="Welcome to Sign-up")
    l1.place(x=200,y=20)
    
    e0=Entry(f1)
    e0.place(x=240,y=50)
    u0=Label(f1,text="Enter your name", fg="black",bg="gray")
    u0.place(x=80,y=50, width=130)
    
    e1=Entry(f1)
    e1.place(x=240,y=70)
    u1=Label(f1,text="Email", fg="black",bg="gray")
    u1.place(x=80,y=70, width=130)
    
    e2=Entry(f1)
    e2.place(x=240,y=90)
    u2=Label(f1,text="Age", fg="black",bg="gray")
    u2.place(x=80,y=90, width=130)
     
    e3=Entry(f1, show="*")
    e3.place(x=240,y=110)
    u3=Label(f1,text="Create a Password",fg="black",bg="gray")
    u3.place(x=80,y=110, width=130)
   
    e4=Entry(f1, show="*")
    e4.place(x=240,y=130)
    u4=Label(f1,text="Confrim_Password", fg="black",bg="gray")
    u4.place(x=80,y=130, width=130)
    
    b1=Button(f1, text="Home",command=main)
    b1.place(x=0,y=0)
    
    b1=Button(f1, text="Sign-up", command= lambda: add_data(e0.get(), e1.get(), e2.get(), e3.get(), e4.get()))
    b1.place(x=200,y=150)
    
main()

t.mainloop()


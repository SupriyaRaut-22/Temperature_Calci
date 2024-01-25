#Calculator Application
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk

#the root window configuration
root=tk.Tk()
root.title("Temperature Convertor")
root.geometry("600x600+100+100")
root.configure(bg="#09A3BA")
f=("Arial",30,"bold")

#global variable
tempVal="Celsius"

#getting dropdwon value
def store_temp(set_temp):
    global tempVal
    tempVal=set_temp

#the Conversion
def convert():
    con=None
    try:
        tem=ent.get()
        if len(tem)==0:
            raise Exception("Temperature cannot be Empty") 
       
        if tem.isspace():
           raise Exception("Temperature cannot be only spaces")
         
        if tem.isalpha():
            raise Exception("Temperature cannot contain Alphabets")
        
        temp=float(tem)
        if temp<0:
            raise Exception("Temperature cannot be negative")
        
        if tempVal=='Celsius':
            f=float((float(tem)*9/5)+32)
            k=float((float(tem)+273.15))
            ans1.configure(text="%.2f Fahrenheit" % f)
            ans2.configure(text="%.2f Kelvin" % k)
      
        if tempVal=='Fahrenheit':
            c=float((float(tem)-32)*5/9)
            k=c+273
            ans1.configure(text="%.2f Celsius" % c)
            ans2.configure(text="%.2f Kelvin" % k)
        
    except Exception as e:
        showerror("Issue",e)

    finally:
        if con is not None:
            con.close() 
        
def remove():
    ent.delete(0,END)
    ans1.config(text="")
    ans2.config(text="")
    ent.focus()


var=tk.StringVar()

#dropdown list
droplist=["Celsius","Fahrenheit"]
dropdown=tk.OptionMenu(root,var,*droplist,command=store_temp)
dropdown.configure(font=f)
dropdown["menu"].config(font=("Arial",20),background='lightgrey', foreground="black")
var.set(droplist[0])
dropdown.pack(pady=5)


lab=Label(root,text="Enter Temperature",font=f,background="#09A3BA")
ent=Entry(root,font=f)
btn=Button(root,text="Convert",font=f,background="black",foreground="white",command=convert)
ans1=Label(root,font=f,background="#09A3BA")
ans2=Label(root,font=f,background="#09A3BA")
btn1=Button(root,text="Reset",font=f,background="lightgray",foreground="black",command=remove)
lab.pack(pady=5)
ent.pack(pady=5)
btn.pack(pady=10)
ans1.pack(pady=10)
ans2.pack(pady=10)
btn1.pack(pady=15)

root.mainloop()

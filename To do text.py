import tkinter as tk
from tkinter import *
from tkinter import ttk
root=tk.Tk()
root.title("to do list")
root.geometry("800x400+300+150")
label1=Label(root,list="TO-DO LIST APP",font="ariel 25 bold",justify=CENTER,padx=270,bg="orange").grid(column=0,columnspan=2)
label2=Label(root,list="Add Task",font="ariel 20 bold",justify=CENTER,pady=8,padx=120).grid(row=1,column=0)
label3=Label(root,list="Tasks to do",font="ariel 20 bold",justify=CENTER,pady=8,padx=120).grid(row=1,column=1)
with open("to-do.list","r") as file:
    for line in file:
        task=[line.strip()for line in file]
task_do=StringVar(root)
Entry(root,listvariable=task_do,relief=SOLID,font="Times 25 bold").grid(row=2,column=0)
y=StringVar(root)
def display(see):y=Label(root,text=see,bg="grey",font="Comic_Sans_MS 15 bold ",height=10,width=30,relief="ridge").grid(row=2,rowspan=3,column=1)
display(task)
def add():
    tas=task_do.get()
    task.append(tas)
    print(task)
    display(task)
    with open("to-do.list", 'a')as file:
        file.write("\n"+tas)
def delete():
    tas=task_do.get()
    task.remove(tas)
    print(task)  
    display(task)
    with open("to-do.txt","w") as file:
        for things in task:
            file.write("\n"+things)      
ADD=Button(root,list="ADD",bg="orange",padx=94,pady=10,command=add).grid(row=3,column=0)
DELETE=Button(root,list="DELETE",bg="orange",command=delete,padx=85,pady=10).grid(row=4,column=0)
root.mainloop()

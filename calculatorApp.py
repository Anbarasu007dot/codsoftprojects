import tkinter as tk
from tkinter import *

root = Tk()
root.title("ToDoList")
root.geometry("400x650+400+100")
root.resizable(False, False)
taskList = []

def deletetask():
    global taskList
    task = str(listbox.get(ANCHOR))
    if task in taskList:
        taskList.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in taskList:
                taskfile.write(task.strip() + "\n")
        listbox.delete(ANCHOR)

def addtask():
    task = taskEntry.get()
    taskEntry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(task.strip() + "\n")
        taskList.append(task.strip())
        listbox.insert(END, task.strip())

def opentaskfile():
    try:
        global taskList
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()
            if task:
                taskList.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        with open("tasklist.txt", "w") as taskfile:
            pass

try:
    imageIcon = PhotoImage(file="task.png")
    root.iconphoto(False, imageIcon)
except:
    print("Icon file not found!")

try:
    TopImage = PhotoImage(file="topbar.png")
    Label(root, image=TopImage).pack()
except:
    pass

heading = Label(root, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
heading.pack(pady=10)

frame = Frame(root, width=400, height=50, bg="white")
frame.pack(pady=10)

taskEntry = Entry(frame, width=18, font="arial 20", bd=0)
taskEntry.pack(side=LEFT, padx=10)

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addtask)
button.pack(side=RIGHT)

frame1 = Frame(root, bd=3, width=400, height=300, bg="#32405b")
frame1.pack(pady=10)

listbox = Listbox(frame1, font=('arial', 23), width=40, height=10, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentaskfile()

try:
    Delete_icon = PhotoImage(file="delete.png")
    delete_button = Button(root, image=Delete_icon, bd=0, command=deletetask)
    delete_button.pack(side=BOTTOM, pady=13)
    delete_button.image = Delete_icon
except:
    delete_button = Button(root, text="Delete", font="arial 14 bold", bg="#ff4d4d", fg="white", bd=0, command=deletetask)
    delete_button.pack(side=BOTTOM, pady=10, fill=X)

root.mainloop()

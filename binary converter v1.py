from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
def Ascii():
    entry3.delete(0,END)
    x=str(entry1.get())
    binary =' '.join(format(ord(y), 'b') for y in x)
    entry3.insert(10,binary)
    entry1.delete(0,END)

def binary():
    entry3.delete(0,END)
    x=str(entry2.get())
    string="".join([chr(int(binary, 2)) for binary in x.split (" ")])
    entry3.insert(10,string)
    entry2.delete(0,END)
mywindow=Tk()
mywindow.title("binary converter")

Label(mywindow, text="Ascii").grid(row=0)
Label(mywindow, text="binary").grid(row=1)
Label(mywindow, text="output").grid(row=2)

entry1=Entry(mywindow)
entry2=Entry(mywindow)
entry3=Entry(mywindow)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

Button(mywindow,text="Quit",command=mywindow.quit).grid(row=3,column=0,sticky=W,padx=5,pady=5)
Button(mywindow,text="convert to binary",command=Ascii).grid(row=3,column=1,sticky=W,padx=5,pady=5)
Button(mywindow,text="convert to Ascii",command=binary).grid(row=3,column=2,sticky=W,padx=5,pady=5)
mywindow.mainloop()
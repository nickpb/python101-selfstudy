from tkinter import *
from tkinter import ttk # theme of tkinter
from tkinter import messagebox

GUI = Tk()
GUI.title('Daily Activities logs')
GUI.geometry('500x300')

#declare function Button1
def Button1():
    text = 'KKananan'
    messagebox.showinfo('เคุณชื่ออะไร', text)

#LabelFrame Button1
FB1 = LabelFrame(GUI,text='Personal Profile') # container
FB1.place(x=10,y=50)

#create button1
B1 = ttk.Button(FB1,text='คุณชื่ออะไร?',command=Button1)
B1.pack(ipadx=10,ipady=10,padx=20,pady=20)


#declare function Button2
def Button2():
    text = 'available balance is 300 THB'
    messagebox.showwarning('เงินในบัญชี', text)
    
#create button2    
B2 = ttk.Button(FB1,text='Available Balance',command=Button2)
B2.pack(ipadx=10,ipady=10,padx=10,pady=10)

#declare function Button3
def Button3():
    text = 'Thailand'
    messagebox.showwarning('Locationี', text)
    
#create button3
B3 = ttk.Button(FB1,text='Location3',command=Button3)
B3.pack(ipadx=10,ipady=10,padx=10,pady=10)



GUI.mainloop()

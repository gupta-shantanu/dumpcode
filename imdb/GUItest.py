from tkinter import *
from scrapIMDB import *

app=0

class App:
    def __init__(self):
        self.master = Tk()
        
        self.master.title("MineSweeper  shantanu@programmer.net")
        frame=Frame(self.master)
        frame.pack()
        
        self.L1 = Label(frame, text="Enter the Text")
        self.L1.pack()
        
        self.E1 = Entry(frame, bd=1, width=30)
        self.E1.pack()
        
        self.button = Button(frame,width=30,
                             text="GO", fg="darkred",
                             command=self.button1)
        self.button.pack()
        

        
       
        
        self.L1 = Label(frame, text="Width")
        self.L1.pack()
        
        self.E1.insert(100, 11)
        self.master.mainloop()
        
    def button1(self):
        print(self.E1.get())


app = App()


            
            
        


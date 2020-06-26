from tkinter import *
def reset():
    pass
class NumSty:
    def __init__(self,obj):
        self.no = ""
        self.win = obj
    def setRes(self):
        self.no = int( self.win.entry.get())
        self.win.hex_res.configure(text=hex(self.no),font="{ARIAL BOLD 15}")
        self.win.bin_res.configure(text=bin(self.no),font="{ARIAL BOLD 15}")
        self.win.oct_res.configure(text=oct(self.no),font="{ARIAL BOLD 15}")

class MainWindow(NumSty):
         def __init__(self):
             super().__init__(self)
             self.no = StringVar
             self.rootWin = Tk()
             self.entry = Entry(textvariable=self.no)
             self.hex_res = Label()
             self.bin_res = Label()
             self.oct_res = Label()
             self.setProperty()
             self.rootWin.mainloop()


         def setProperty(self):
             self.rootWin.geometry("500x500")
             self.rootWin.title("NUMBER SYSTEM")
             self.rootWin.configure(background="white")
             self.rootWin.minsize(500,500)
             self.rootWin.maxsize(500,500)
             self.lable = Label(text="Enter the number :")
             self.lable.configure(background="white",font="{ARIAL BOLD 16}")
             self.lable.place(x=50,y=50,height=40)
             self.entry.place(x=210,y=50,height=40)
             self.resBtn = Button(text="CONVERT",command=super().setRes)
             self.resBtn.configure(bg="green")
             self.resBtn.place(x=150,y=120)
             self.resetBtn = Button(text="RESET",command=self.reset)
             self.resetBtn.configure(bg="red")
             self.resetBtn.place(x=260,y=120,width=100)

             self.hex_lable = Label(text="HEXADECIMAL :")
             self.hex_lable.configure(bg="white")
             self.hex_lable.place(x=50,y=200)
             self.hex_res.configure(bg="white")
             self.hex_res.place(x=200,y=200)

             self.oct_lable = Label(text="OCTEL :")
             self.oct_lable.configure(bg="white")
             self.oct_lable.place(x=50, y=250)
             self.oct_res.configure(bg="white")
             self.oct_res.place(x=200, y=250)

             self.bin_lable = Label(text="BINARY :")
             self.bin_lable.configure(bg="white")
             self.bin_lable.place(x=50, y=300)
             self.bin_res.configure(bg="white")
             self.bin_res.place(x=200, y=300)

         def reset(self):
             self.entry.configure(text=" ")
             self.hex_res.configure(text=" ")
             self.bin_res.configure(text=" ")
             self.oct_res.configure(text=" ")


def main():
    win = MainWindow()

if __name__ == '__main__':
    main()


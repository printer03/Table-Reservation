from Tkinter import *
class Check_in(object):
    root = Tk()
    box = Entry(root, width = 30)
    def __init__(self):
        head = Label(self.root, text="Name")
        head.pack()
        self.box.pack()
        self.b = Button(self.root, text="Reserve", width=10, command=self.callback)
        self.b.pack()
        self.root.mainloop()
        
    def callback(self):
        self.name = self.box.get()
        print self.name
        
##class monitor(object):
##    root = Tk()
##    box = Entry(root, width = 30)
##    def __init__(self):
        
    
Check_in()

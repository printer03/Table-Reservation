from Tkinter import *
class Check_in(object):
    root = Tk()
    box = Entry(root, width = 30)
    root1 = Tk()
    
    def __init__(self, count = 0):
        head = Label(self.root, text="Name")
        head.pack()
        self.box.pack()
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor)
        self.b.pack()
        self.root.mainloop()

    def monitor(self):
        self.name = self.box.get()
        head1 = Label(self.root1, text=self.name)
        head1.pack()
        self.b = Button(self.root1, text="Order", width=10\
                        , command=self.order_food)
        self.b.pack()
        print self.name
        
    def order_food(self):
        root2 = Tk()
        self.b = Button(root2, text="Noodle", width=10\
                        , command=self.monitor)
        self.b.pack()
        self.b = Button(root2, text="Fried chicken", width=10\
                        , command=self.monitor)
        self.b.pack()
        self.b = Button(root2, text="Rice", width=10\
                        , command=self.monitor)
        self.b.pack()

Check_in()


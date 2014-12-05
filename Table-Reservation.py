from Tkinter import *

class Check_in(object):
    root = Tk()
    root.title("Table-Reservation")
    root.geometry('800x1000')
    box = Entry(root, width = 50)
    listm = []
    dict1 = dict()
    count = 150
    data1, data2, data3, data4, data5 = [], [], [], [], []
    total1, total2, total3, total4, total5 = [], [], [], [], []
    
    def __init__(self):
        price = []
        head = Label(self.root, text="Welcome to 5 Tables Restaurant")
        head.pack()
        head1 = Label(self.root, text="Name")
        head1.pack()
        self.box.pack()
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor)
        self.b.pack()
        self.root.mainloop()

    def monitor(self):
        if self.count >= 300:
            root1 = Tk()
            caution = Label(root1, text="Table are full reserved now, please checking again in 10 minutes")
            caution.pack()
            exits = Button(root1, text='OK', command = root1.destroy)
            exits.pack()

        else:
            for i in xrange(150, 271, 30):
                if i not in self.listm:
                    list1 = ['Fried chicken $6', 'Rice $1', 'Noodle $8', 'Salad $5']
                    self.name = self.box.get()
                    head1 = Label(self.root, text=self.name)
                    head1.place(x=50, y=self.count)

                    self.spindle = StringVar(self.root)
                    self.spindle.set('Ordered here') #default value
                    s = OptionMenu(self.root, self.spindle, *list1)
                    s.place(x=200, y=self.count)

                    button = Button(self.root, text="Submit", command=self.submit)
                    button.place(x=350, y=self.count)

                    menu_list = Button(self.root, text="Your Ordered", command=self.menu_list)
                    menu_list.place(x=500, y=self.count)
                    
                    #check_bill = 'check_bill'+str(self.upper)
                    if self.count == 150:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill1)
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 180:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill2)
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 210:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill3)
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 240:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill4)
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 270:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill5)
                        bill_button.place(x=650, y=self.count)

                    self.listm.append(i)
                    self.count += 30
                    print self.name
                    break

    def submit(self):
        print self.spindle.get()
        ##add price to data##
        if self.count == 180:
            self.data1.append(self.spindle.get())
            self.total1.append(int(self.spindle.get()[-1]))
        elif self.count == 210:
            self.data2.append(self.spindle.get())
            self.total2.append(int(self.spindle.get()[-1]))
        elif self.count == 240:
            self.data3.append(self.spindle.get())
            self.total3.append(int(self.spindle.get()[-1]))
        elif self.count == 270:
            self.data4.append(self.spindle.get())
            self.total4.append(int(self.spindle.get()[-1]))
        elif self.count == 300:
            self.data5.append(self.spindle.get())
            self.total5.append(int(self.spindle.get()[-1]))
        
    def menu_list(self):
        rootm = Tk()
        if self.count == 180:
            for i in self.data1:
                Label(rootm, text=i).pack()
        elif self.count == 210:
            for i in self.data2:
                Label(rootm, text=i).pack()
        elif self.count == 240:
            for i in self.data3:
                Label(rootm, text=i).pack()
        elif self.count == 270:
            for i in self.data4:
                Label(rootm, text=i).pack()
        elif self.count == 300:
            for i in self.data5:
                Label(rootm, text=i).pack()
        exits = Button(rootm, text='OK', command = rootm.destroy)
        exits.pack()

    ####################################apart all button check bill for 5 customers####################################
    def check_bill1(self):
        rootb = Tk()
        for i in self.data1:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total1))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy)
        exits.pack()
        a = Label(self.root, text='                '*100)
        a.place(y=150)
        a = Label(self.root, text='                '*100)
        a.place(y=158)
        self.listm.remove(150)
        self.count -= 30
        self.data1, self.total1 = [], []
        print sum(self.total1)

    def check_bill2(self):
        rootb = Tk()
        for i in self.data2:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total2))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy)
        exits.pack()
        a = Label(self.root, text='                '*100)
        a.place(y=180)
        a = Label(self.root, text='                '*100)
        a.place(y=188)
        self.listm.remove(180)
        self.count -= 30
        self.data2, self.total2 = [], []
        print sum(self.total2)

    def check_bill3(self):
        rootb = Tk()
        for i in self.data3:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total3))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy)
        exits.pack()
        a = Label(self.root, text='                '*100)
        a.place(y=210)
        a = Label(self.root, text='                '*100)
        a.place(y=218)
        self.listm.remove(210)
        self.count -= 30
        self.data3, self.total3 = [], []
        print sum(self.total3)

    def check_bill4(self):
        rootb = Tk()
        for i in self.data4:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total4))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy)
        exits.pack()
        a = Label(self.root, text='                '*100)
        a.place(y=240)
        a = Label(self.root, text='                '*100)
        a.place(y=248)
        self.listm.remove(240)
        self.count -= 30
        self.data4, self.total4 = [], []
        print sum(self.total4)

    def check_bill5(self):
        rootb = Tk()
        for i in self.data5:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total5))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy)
        exits.pack()
        a = Label(self.root, text='                '*100)
        a.place(y=270)
        a = Label(self.root, text='                '*100)
        a.place(y=278)
        self.listm.remove(270)
        self.count -= 30
        self.data5, self.total5 = [], []
        print sum(self.total5)
        
Check_in()

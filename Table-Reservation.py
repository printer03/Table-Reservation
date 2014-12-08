from Tkinter import *
import base64
import urllib
class Check_in(object):
    root = Tk()
    root.title("Table-Reservation")
    URL = "http://www.septicsuppliesinc.com/skin/2-columns/images/2column/bg_body_page_red.gif"
    link = urllib.urlopen(URL)
    raw_data = link.read()
    link.close()
    next = base64.encodestring(raw_data)
    image = PhotoImage(data=next)
    label = Label(image=image)
    label.pack()
    root.geometry('800x700')
    box = Entry(root, width = 50, bg = '#FFFFC2')
    listm = []
    count = 300
    data1, data2, data3, data4, data5 = [], [], [], [], []
    total1, total2, total3, total4, total5 = [], [], [], [], []
    
    def __init__(self):
        price = []
        head = Label(self.root, text="Welcome to 5 Tables Restaurant", bg='#9F000F')
        head.place(x=320, y=20)
        head1 = Label(self.root, text="Name", bg='#9F000F')
        head1.place(x=385, y=50)
        self.box.place(x=250, y=100)
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor, bg = '#FDD017')
        self.b.place(x=360, y=140)
        self.root.mainloop()

    def monitor(self):
        if self.count >= 500:
            root1 = Tk()
            caution = Label(root1, text="Table are full reserved now, please checking again in 10 minutes")
            caution.pack()
            exits = Button(root1, text='OK', command = root1.destroy, bg = '#92C7C7')
            exits.pack()

        else:
            position = 0
            for i in xrange(300, 461, 40):
                position += 1
                if i not in self.listm:
                    self.count = i
                    self.listm.append(i)
                    print position
                    list1 = ['Fried chicken $6', 'Rice $1', 'Noodle $7', 'Salad $5', 'Pizza $9', 'Pasta $7', 'Juice $1', \
                             'Steak $9', 'Fried rice $2', 'Lasagna $9']
                    self.name = self.box.get()
                    head1 = Label(self.root, text='Table ' + str(position) + '   ' + self.name, bg='#9F000F')
                    head1.place(x=50, y=self.count)

                    self.spindle = StringVar(self.root)
                    self.spindle.set('Pre-Order') #default value
                    s = OptionMenu(self.root, self.spindle, *list1)
                    s.place(x=250, y=self.count)

                    button = Button(self.root, text="Submit", command=self.submit, bg = '#FFDB58')
                    button.place(x=400, y=self.count)

                    menu_list = Button(self.root, text="Your Ordered", command=self.menu_list, bg = '#FFD801')
                    menu_list.place(x=550, y=self.count)
                    
                    #check_bill = 'check_bill'+str(self.upper)
                    if self.count == 300:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill1, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 340:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill2, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 380:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill3, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 420:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill4, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                    elif self.count == 460:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill5, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)

                    self.count += 40
                    print self.name
                    break

    def submit(self):
        print self.spindle.get()
        ##add price to data##
        if self.count == 340:
            self.data1.append(self.spindle.get())
            self.total1.append(int(self.spindle.get()[-1]))
        elif self.count == 380:
            self.data2.append(self.spindle.get())
            self.total2.append(int(self.spindle.get()[-1]))
        elif self.count == 420:
            self.data3.append(self.spindle.get())
            self.total3.append(int(self.spindle.get()[-1]))
        elif self.count == 460:
            self.data4.append(self.spindle.get())
            self.total4.append(int(self.spindle.get()[-1]))
        elif self.count == 500:
            self.data5.append(self.spindle.get())
            self.total5.append(int(self.spindle.get()[-1]))
        
    def menu_list(self):
        rootm = Tk()
        if self.count == 340:
            for i in self.data1:
                Label(rootm, text=i).pack()
        elif self.count == 380:
            for i in self.data2:
                Label(rootm, text=i).pack()
        elif self.count == 420:
            for i in self.data3:
                Label(rootm, text=i).pack()
        elif self.count == 460:
            for i in self.data4:
                Label(rootm, text=i).pack()
        elif self.count == 500:
            for i in self.data5:
                Label(rootm, text=i).pack()
        exits = Button(rootm, text='OK', command = rootm.destroy, bg = '#FDD017')
        exits.pack()

    ####################################apart all button check bill for 5 customers####################################
    def check_bill1(self):
        rootb = Tk()
        for i in self.data1:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total1))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.pack()
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=300)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=310)
        self.listm.remove(300)
        self.count -= 40
        self.data1, self.total1 = [], []
        print sum(self.total1)
        print self.listm

    def check_bill2(self):
        rootb = Tk()
        for i in self.data2:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total2))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.pack()
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=340)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=350)
        self.listm.remove(340)
        self.count -= 40
        self.data2, self.total2 = [], []
        print sum(self.total2)
        print self.listm

    def check_bill3(self):
        rootb = Tk()
        for i in self.data3:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total3))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.pack()
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=380)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=390)
        self.listm.remove(380)
        self.count -= 40
        self.data3, self.total3 = [], []
        print sum(self.total3)
        print self.listm

    def check_bill4(self):
        rootb = Tk()
        for i in self.data4:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total4))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.pack()
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=420)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=430)
        self.listm.remove(420)
        self.count -= 40
        self.data4, self.total4 = [], []
        print sum(self.total4)
        print self.listm

    def check_bill5(self):
        rootb = Tk()
        for i in self.data5:
            Label(rootb, text=i).pack()
        Label(rootb, text='Price = $' + str(sum(self.total5))).pack()
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.pack()
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=460)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=470)
        self.listm.remove(460)
        self.count -= 40
        self.data5, self.total5 = [], []
        print sum(self.total5)
        print self.listm
        
Check_in()

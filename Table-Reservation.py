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
    order_amount = dict()
    
    def __init__(self):
        price = []
        about = Button(self.root, width = 115, text="About this program", command=self.detail)
        about.place(x=0, y=0)
        head = Label(self.root, text="Welcome to 5 Tables Restaurant", bg='#9F000F')
        head.place(x=320, y=40)
        head1 = Label(self.root, text="Enter your name here", bg='#9F000F')
        head1.place(x=340, y=70)
        self.box.place(x=250, y=100)
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor, bg = '#FDD017')
        self.b.place(x=360, y=140)
        self.root.mainloop()

    def monitor(self):
        '''This function is use to link all button and another option'''
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

                    button_submit = Button(self.root, text="Submit", command=self.submit, bg = '#FFDB58')
                    button_submit.place(x=400, y=self.count)

                    button_calcel = Button(self.root, text="Cancel", command=self.cancel, bg = '#FFDB58')
                    button_calcel.place(x=450, y=self.count)

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
        '''This function is use to command to save list of menu that customer ordered to this restaurant'''
        print self.spindle.get()
        ##add price to data##
        if self.spindle.get() not in self.order_amount:
            self.order_amount[self.spindle.get()] = 1
        else:
            self.order_amount[self.spindle.get()] += 1
        if self.spindle.get() != 'Pre-Order':
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

    def cancel(self):
        '''This function is use to cancel things that customer change there mind'''
        print self.spindle.get()
        if self.count == 340:
            self.order_amount[self.spindle.get()] -= 1
            if self.order_amount[self.spindle.get()] == 0:
                self.data1.remove(self.spindle.get())
            self.total1.remove(int(self.spindle.get()[-1])) ##remove price in total1
        elif self.count == 380:
            self.order_amount[self.spindle.get()] -= 1
            if self.order_amount[self.spindle.get()] < 0:
                self.data2.remove(self.spindle.get())
                self.total2.remove(int(self.spindle.get()[-1]))
            self.total1.remove(int(self.spindle.get()[-1])) ##remove price in total2
        elif self.count == 420:
            self.order_amount[self.spindle.get()] -= 1
            if self.order_amount[self.spindle.get()] <= 0:
                self.data3.remove(self.spindle.get())
            self.total3.remove(int(self.spindle.get()[-1])) ##remove price in total3
        elif self.count == 460:
            self.order_amount[self.spindle.get()] -= 1
            if self.order_amount[self.spindle.get()] <= 0:
                self.data4.remove(self.spindle.get())
            self.total4.remove(int(self.spindle.get()[-1])) ##remove price in total4
        elif self.count == 500:
            self.order_amount[self.spindle.get()] -= 1
            if self.order_amount[self.spindle.get()] <= 0:
                self.data5.remove(self.spindle.get())
            self.total5.remove(int(self.spindle.get()[-1])) ##remove price in total5
        
    def menu_list(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk()
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data1 = list(set(self.data1))
        self.data2 = list(set(self.data2))
        self.data3 = list(set(self.data3))
        self.data4 = list(set(self.data4))
        self.data5 = list(set(self.data5))
        if self.count == 340:
            for i in self.data1:
                line += 30
                Label(rootm, text=i).place(x=10, y=line)
                Label(rootm, text=self.order_amount[i]).place(x=250, y=line)
        elif self.count == 380:
            for i in self.data2:
                Label(rootm, text=i).pack()
                line += 30
                Label(rootm, text=i).place(x=10, y=line)
                Label(rootm, text=self.order_amount[i]).place(x=250, y=line)
        elif self.count == 420:
            for i in self.data3:
                Label(rootm, text=i).pack()
                line += 30
                Label(rootm, text=i).place(x=10, y=line)
                Label(rootm, text=self.order_amount[i]).place(x=250, y=line)
        elif self.count == 460:
            for i in self.data4:
                Label(rootm, text=i).pack()
                line += 30
                Label(rootm, text=i).place(x=10, y=line)
                Label(rootm, text=self.order_amount[i]).place(x=250, y=line)
        elif self.count == 500:
            for i in self.data5:
                Label(rootm, text=i).pack()
                line += 30
                Label(rootm, text=i).place(x=10, y=line)
                Label(rootm, text=self.order_amount[i]).place(x=250, y=line)
        rootm.geometry(str(300)+'x'+str(line+60))
        exits = Button(rootm, text='OK', command = rootm.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+30)

    ####################################apart all button check bill for 5 customers####################################
    def check_bill1(self):
        '''Keep database of Table1 and ready to calculate all the time'''
        rootb = Tk()
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data1 = list(set(self.data1))
        for i in self.data1:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total1))).place(x=200, y=line+30)
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=300)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=310)
        self.listm.remove(300)
        self.count -= 40
        print self.total1
        self.data1, self.total1 = [], []
        self.order_amount = dict()
        print sum(self.total1)
        print self.listm

    def check_bill2(self):
        '''Keep database of Table2 and ready to calculate all the time'''
        rootb = Tk()
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data2 = list(set(self.data2))
        for i in self.data2:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total2))).place(x=10, y=line+30)
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=340)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=350)
        self.listm.remove(340)
        self.count -= 40
        self.data2, self.total2 = [], []
        self.order_amount = dict()
        print sum(self.total2)
        print self.listm

    def check_bill3(self):
        '''Keep database of Table3 and ready to calculate all the time'''
        rootb = Tk()
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data3 = list(set(self.data3))
        for i in self.data3:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total3))).place(x=10, y=line+30)
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=380)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=390)
        self.listm.remove(380)
        self.count -= 40
        self.data3, self.total3 = [], []
        self.order_amount = dict()
        print sum(self.total3)
        print self.listm

    def check_bill4(self):
        '''Keep database of Table4 and ready to calculate all the time'''
        rootb = Tk()
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data4 = list(set(self.data4))
        for i in self.data4:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total4))).place(x=10, y=line+30)
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=420)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=430)
        self.listm.remove(420)
        self.count -= 40
        self.data4, self.total4 = [], []
        self.order_amount = dict()
        print sum(self.total4)
        print self.listm

    def check_bill5(self):
        '''Keep database of Table4 and ready to calculate all the time'''
        rootb = Tk()
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data5 = list(set(self.data5))
        for i in self.data5:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total5))).place(x=10, y=line+30)
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=460)
        a = Label(self.root, text='                '*100, bg='#9F000F')
        a.place(y=470)
        self.listm.remove(460)
        self.count -= 40
        self.data5, self.total5 = [], []
        self.order_amount = dict()
        print sum(self.total5)
        print self.listm

    def detail(self):
        rootd = Tk()
        scrollb = Scrollbar(rootd)
        texture = Text(rootd, height=4, width=57)
        scrollb.pack(side=RIGHT, fill=Y)
        texture.pack(side=LEFT, fill=Y)
        scrollb.config(command=texture.yview)
        texture.config(yscrollcommand=scrollb.set)
        quote = """This program is use to reserve a table from another place. \
You can pre-order for more rapid and comfort in your dialy life. \
This program is help you that you haven't wait for food anymore \
if you pre-order to there restaurant, all foods that will come \
to your table in 5 minutes because we had cooked for you and boil \
all the time. When you ate already you can click check bill button. \
This program will calculate all price for you to pay"""
        texture.insert(END, quote)
        
        
Check_in()

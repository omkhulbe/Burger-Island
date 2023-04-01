from tkinter import *
from time import strftime
from sqlite3 import *
import random
import os
from tkinter import messagebox
from cryptography.fernet import Fernet
import customtkinter


class Burger:
    cartlist = []
    amount = 0

    # --  page 1------
    # ------ page 2------
    def Login(sf):
        try:
            sf.scr.destroy()
            sf.scr = Tk()
        except:
            try:
                sf.scr = Tk()
            except:
                pass
        sf.cartlist = []
        sf.amount = 0
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.loginf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.loginf1, image=sf.logo, height=150).place(x=-2, y=0)

        # sf.abt = Button(sf.loginf1, text="ABOUT US", bg="#0b1335", cursor="hand2", bd=0, fg="white",
        #                font=("Montserrat Bold", 13), relief=SUNKEN, padx=12, pady=1, justify=CENTER)
        # sf.abt.config(command=lambda: sf.about())
        # sf.abt.place(x=1210, y=100)
        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.loginf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.loginf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.loginf1.pack(fill=BOTH, expand=1)
        sf.loginf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.loginf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/burglog.png")
        sf.mal = Label(sf.loginf2, image=sf.logo1, height=618).place(x=-2, y=0)

        sf.lab1 = Label(sf.loginf2, text="Username", bg="#fdcb7a", font=("Montserrat ExtraBold", 20))
        sf.lab1.place(x=120, y=265)
        sf.user = Entry(sf.loginf2, bg="white", font=("Poppins", 13), bd=0, justify='left', width=30)
        sf.user.place(x=360, y=271)
        sf.lab2 = Label(sf.loginf2, text="Password", bg="#fdcb7a", font=("Montserrat ExtraBold", 20))
        sf.lab2.place(x=120, y=358)
        sf.pasd = Entry(sf.loginf2, bg="white", show="*", font=("Poppins", 13), bd=0, justify='left', width=30)
        sf.pasd.place(x=360, y=364)
        sf.lg = Button(sf.loginf2, cursor="hand2", command=lambda: sf.logindatabase(), bg="#fdcb7a", bd=0)
        sf.lg.place(x=185, y=480)
        sf.lgimg = PhotoImage(file="Images/Buttons/logbutton.png")
        sf.lg.config(image=sf.lgimg)
        sf.scr.bind('<Return>', lambda event: sf.logindatabase())

        def clear(sf):
            sf.user.delete(0, END)
            sf.pasd.delete(0, END)

        sf.cl = Button(sf.loginf2, cursor="hand2", command=lambda: clear(sf), bg="#fdcb7a", bd=0)
        sf.cl.place(x=465, y=480)
        sf.climg = PhotoImage(file="Images/Buttons/clear.png")
        sf.cl.config(image=sf.climg)

        sf.rg = Button(sf.loginf2, command=lambda: sf.Register(), cursor="hand2", bg="#fdcb7a", bd=0)
        sf.rg.place(x=1000, y=510)
        sf.rgimg = PhotoImage(file="Images/Buttons/register.png")
        sf.rg.config(image=sf.rgimg)

        extpath = "Images\\Offers"
        files = os.listdir(extpath)
        d = random.choice(files)
        sf.ext = PhotoImage(file="Images/Offers/" + d)
        sf.url = Label(sf.loginf2, image=sf.ext, cursor="hand2", bg="#fdcb7a").place(x=900, y=140)
        sf.loginf2.pack(fill=BOTH, expand=1)

        sf.scr.mainloop()

    def resultlog(sf):
        sf.loguser = sf.user.get()
        sf.logpass = sf.pasd.get()
        return sf.loguser, sf.logpass

    def about(sf):
        sf.scr1 = Tk()
        sf.scr1.title("About Us")
        sf.scr1.geometry("620x80+80+10")
        sf.L = Label(sf.scr1,
                     text="NEW BURGER ISLAND\nWe Are Not The Best But Want To Become Best\nPlease Provide Feedbacks\nNew Burger Island Is A Copyright of 2019-20")
        sf.L.pack()
        sf.scr1.mainloop()

    def resultadmin(sf):
        sf.loguser = sf.usera.get()
        sf.logpass = sf.pasda.get()
        return sf.loguser, sf.logpass

    # --  page 3------
    def Register(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.regf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.regf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.regf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.regf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.regf1.pack(fill=BOTH, expand=1)

        sf.regf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.regf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/burgermain.png")
        sf.mal = Label(sf.regf2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.c.create_rectangle(150, 100, 1216, 450, fill="#d3ede6", outline="white", width=6)
        sf.log = Label(sf.regf2, text="REGISTRATION", fg="white", bg="#fdcb7a", width=20, font=("Montserrat ExtraBold", 35, 'bold'))
        sf.log.place(x=370, y=90)
        sf.lab1 = Label(sf.regf2, text="First Name:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab1.place(x=190, y=220)
        sf.first = Entry(sf.regf2, bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.first.place(x=430, y=220)
        sf.lab2 = Label(sf.regf2, text="Last Name:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab2.place(x=730, y=220)
        sf.last = Entry(sf.regf2, bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.last.place(x=920, y=220)
        sf.lab3 = Label(sf.regf2, text="Username:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab3.place(x=190, y=290)
        sf.usern = Entry(sf.regf2, bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.usern.place(x=430, y=290)
        sf.lab4 = Label(sf.regf2, text="Password:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab4.place(x=730, y=290)
        sf.passd = Entry(sf.regf2, show="*", bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.passd.place(x=920, y=290)
        sf.lab5 = Label(sf.regf2, text="Email:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab5.place(x=190, y=360)
        sf.email = Entry(sf.regf2, bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.email.place(x=430, y=360)
        sf.lab6 = Label(sf.regf2, text="Mobile No.:", bg="#fdcb7a", font=("Montserrat ExtraBold", 18))
        sf.lab6.place(x=730, y=360)
        sf.mob = Entry(sf.regf2, bg="white", width=22, font=("Poppins", 13), bd=1)
        sf.mob.place(x=920, y=360)
        sf.bc = Button(sf.regf2, text="BACK", cursor="hand2", command=lambda: sf.Login(), fg="white", bg="#FF9A03",
                       font=("Montserrat ExtraBold", 16), bd=3)
        sf.bc.place(x=370, y=480)
        sf.rg = Button(sf.regf2, text="REGISTER", cursor="hand2", fg="white", bg="#FF9A03",
                       command=lambda: sf.Regdatabase(), font=("Montserrat ExtraBold", 16), bd=3)
        sf.rg.place(x=610, y=480)

        def clear(sf):
            sf.usern.delete(0, END)
            sf.passd.delete(0, END)
            sf.first.delete(0, END)
            sf.last.delete(0, END)
            sf.email.delete(0, END)
            sf.mob.delete(0, END)

        sf.cl = Button(sf.regf2, text="CLEAR", cursor="hand2", fg="white", bg="#FF9A03", command=lambda: clear(sf),
                       font=("Montserrat ExtraBold", 16), bd=3)
        sf.cl.place(x=910, y=480)
        sf.regf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    def resultreg(sf):
        sf.reguser = sf.usern.get()
        sf.regpasd = sf.passd.get()
        sf.firstname = sf.first.get()
        sf.lastname = sf.last.get()
        sf.Email = sf.email.get()
        sf.Mob = sf.mob.get()
        return sf.reguser, sf.regpasd, sf.firstname, sf.lastname, sf.Email, sf.Mob

    # --  page 4------
    def adminmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.admainf1 = Frame(sf.scr, bg="#fdcb7a", height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.png")
        sf.ba = Label(sf.admainf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.admainf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.admainf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()
        sf.admainf1.pack(fill=BOTH)

        def Ref(sf):
            sf.con = connect("burger.db")
            ##            sf.x=random.randint(100, 500)
            ##            sf.randomRef = str(sf.x)
            sf.cur = sf.con.cursor()
            try:
                sf.cur.execute(
                    "create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                sf.con.commit()
            except:
                pass
            x = sf.cur.execute("select count(*) from orderdetail")
            ordno = list(x)[0][0] + 1
            sf.order.set(ordno)

            sf.v1 = sf.vp1.get()
            if sf.v1 == "Medium":
                sf.p1 = float(sf.aloo_tikki.get()) * 150
            elif sf.v1 == "Large":
                sf.p1 = float(sf.aloo_tikki.get()) * 200
            else:
                sf.p1 = float(sf.aloo_tikki.get()) * 100
            sf.v2 = sf.vp2.get()
            if sf.v2 == "Medium":
                sf.p2 = float(sf.cheese_burger.get()) * 350
            elif sf.v2 == "Large":
                sf.p2 = float(sf.cheese_burger.get()) * 500
            else:
                sf.p2 = float(sf.cheese_burger.get()) * 200
            sf.v3 = sf.vp3.get()
            if sf.v3 == "Medium":
                sf.p3 = float(sf.mushroom.get()) * 385
            elif sf.v3 == "Large":
                sf.p3 = float(sf.mushroom.get()) * 550
            else:
                sf.p3 = float(sf.mushroom.get()) * 225
            sf.v4 = sf.vp4.get()
            if sf.v4 == "Medium":
                sf.p4 = float(sf.combo.get()) * 295
            elif sf.v4 == "Large":
                sf.p4 = float(sf.combo.get()) * 485
            else:
                sf.p4 = float(sf.combo.get()) * 199
            sf.v5 = sf.vp5.get()
            if sf.v5 == "Medium":
                sf.p5 = float(sf.chicken.get()) * 350
            elif sf.v5 == "Large":
                sf.p5 = float(sf.chicken.get()) * 550
            else:
                sf.p5 = float(sf.chicken.get()) * 200
            sf.v6 = sf.vp6.get()
            if sf.v6 == "Medium":
                sf.p6 = float(sf.chicken_crispy.get()) * 400
            elif sf.v6 == "Large":
                sf.p6 = float(sf.chicken_crispy.get()) * 600
            else:
                sf.p6 = float(sf.chicken_crispy.get()) * 250
            sf.v7 = sf.vp7.get()
            if sf.v7 == "Medium":
                sf.p7 = float(sf.chicken_whooper.get()) * 385
            elif sf.v7 == "Large":
                sf.p7 = float(sf.chicken_whooper.get()) * 550
            else:
                sf.p7 = float(sf.chicken_whooper.get()) * 225
            sf.v8 = sf.vp8.get()
            if sf.v8 == "Medium":
                sf.p8 = float(sf.chicken_cheese.get()) * 295
            elif sf.v8 == "Large":
                sf.p8 = float(sf.chicken_cheese.get()) * 485
            else:
                sf.p8 = float(sf.chicken_cheese.get()) * 199
            sf.p9 = float(sf.Roasted_Chicken.get()) * 109
            sf.p10 = float(sf.Chicken_Meatballs.get()) * 99
            sf.p11 = float(sf.Boneles_sChicken.get()) * 139
            sf.p12 = float(sf.Coke_Mobile.get()) * 45
            sf.p13 = float(sf.Burger_Pizza.get()) * 99
            sf.p14 = float(sf.White_Pasta.get()) * 135

            sf.costofmeal = "Rs.", str('%.2f' % (
                    sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 + sf.p9 + sf.p10 + sf.p11 + sf.p12 + sf.p13 + sf.p14))
            sf.sgst = ((
                               sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 + sf.p9 + sf.p10 + sf.p11 + sf.p12 + sf.p13 + sf.p14) * .025)
            sf.Totalcost = (
                    sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 + sf.p9 + sf.p10 + sf.p11 + sf.p12 + sf.p13 + sf.p14)
            sf.cgst = ((
                               sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 + sf.p9 + sf.p10 + sf.p11 + sf.p12 + sf.p13 + sf.p14) * .025)
            sf.central = "Rs." + str('%.2f' % sf.cgst)
            sf.OverAllCost = "Rs." + str(int(sf.sgst + sf.Totalcost + sf.cgst))
            sf.state = "Rs." + str('%.2f' % sf.sgst)
            sf.money = int(sf.sgst + sf.Totalcost + sf.cgst)
            sf.centralgst.set(sf.central)
            sf.cost.set(sf.costofmeal)
            sf.stategst.set(sf.state)
            sf.Total.set(sf.OverAllCost)

        def reset(sf):
            sf.aloo_tikki.set("0")
            sf.cheese_burger.set("0")
            sf.mushroom.set("0")
            sf.combo.set("0")
            sf.chicken.set("0")
            sf.chicken_crispy.set("0")
            sf.chicken_whooper.set("0")
            sf.chicken_cheese.set("0")
            sf.Coke_Mobile.set("0")
            sf.Burger_Pizza.set("0")
            sf.White_Pasta.set("0")
            sf.Roasted_Chicken.set("0")
            sf.Chicken_Meatballs.set("0")
            sf.Boneles_sChicken.set("0")
            sf.Total.set("0")
            sf.centralgst.set("0")
            sf.stategst.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")
            sf.vp1.set("Medium")
            sf.vp2.set("Medium")
            sf.vp3.set("Medium")
            sf.vp4.set("Medium")
            sf.vp5.set("Medium")
            sf.vp6.set("Medium")
            sf.vp7.set("Medium")
            sf.vp8.set("Medium")

        def price(sf):
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Burger", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Aloo Tikki", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹150/₹200/₹100", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Cheese Veg", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹350/₹500/₹200", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Mushroom", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Combo", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹295/₹485/₹199", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Burger", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹350/₹550/₹200", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Crispy", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Whooper", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Cheese", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹295/₹485/₹199", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Specialty Chicken", fg="black", anchor=W)
            sf.lblinfo.grid(row=11, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Roasted Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹109", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Meatballs", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Boneless Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹139", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Sides & Beverages", fg="black", anchor=W)
            sf.lblinfo.grid(row=15, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Coke Mobile", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹45", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Burger Pizza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="White Pasta", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹135", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=2)

            sf.roo.mainloop()

        sf.admainf2 = Frame(sf.scr, width=1366, height=618)
        sf.logo1 = PhotoImage(file="Images/Assets/burgermain.png")
        sf.mal = Label(sf.admainf2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.aloo_tikki = StringVar()
        sf.cheese_burger = StringVar()
        sf.mushroom = StringVar()
        sf.combo = StringVar()
        sf.chicken = StringVar()
        sf.chicken_crispy = StringVar()
        sf.chicken_whooper = StringVar()
        sf.chicken_cheese = StringVar()
        sf.Coke_Mobile = StringVar()
        sf.Burger_Pizza = StringVar()
        sf.White_Pasta = StringVar()
        sf.Roasted_Chicken = StringVar()
        sf.Chicken_Meatballs = StringVar()
        sf.Boneles_sChicken = StringVar()
        sf.Total = StringVar()
        sf.centralgst = StringVar()
        sf.stategst = StringVar()
        sf.cost = StringVar()
        sf.order = StringVar()
        sf.Cutomer_name = StringVar()
        sf.cusmob = StringVar()
        sf.vp1 = StringVar()
        sf.vp2 = StringVar()
        sf.vp3 = StringVar()
        sf.vp4 = StringVar()
        sf.vp5 = StringVar()
        sf.vp6 = StringVar()
        sf.vp7 = StringVar()
        sf.vp8 = StringVar()
        reset(sf)
        sf.l = ["Medium", "Large", "Regular"]

        # veg burger
        sf.lbl1 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 17, 'bold'), bg="#fdcb7a",
                        text="VEG BURGER", fg="#22aa00", bd=10, anchor='w')
        sf.lbl1.place(x=170, y=10)
        sf.lbl11 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=6, bg="#fdcb7a",
                         text="Items", bd=6, anchor='w')
        sf.lbl11.place(x=80, y=60)
        sf.lbl12 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=7, bg="#fdcb7a",
                         text="Size", bd=6, anchor='w')
        sf.lbl12.place(x=260, y=60)
        sf.lbl13 = Label(sf.admainf2, font=('Montserrat ExtraBold', 14), width=8, bg="#fdcb7a",
                         text="Quantity", bd=6, anchor='w')
        sf.lbl13.place(x=360, y=60)

        sf.lblalt = Label(sf.admainf2, font=('Poppins', 14, 'bold'), text="Aloo Tikki:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblalt.place(x=80, y=105)
        sf.opalt = OptionMenu(sf.admainf2, sf.vp1, *sf.l)
        sf.opalt.config(width=6)
        sf.opalt.place(x=265, y=110)
        sf.txtalt = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.aloo_tikki, bd=2, width=4,
                          bg="white", justify='right')
        sf.txtalt.place(x=400, y=110)

        sf.lblchbr = Label(sf.admainf2, font=('Poppins', 14, 'bold'), text="Cheese:", bg="#fdcb7a",
                           fg="#7769ad", bd=6, anchor='w')
        sf.lblchbr.place(x=80, y=145)
        sf.opchbr = OptionMenu(sf.admainf2, sf.vp2, *sf.l)
        sf.opchbr.config(width=6)
        sf.opchbr.place(x=265, y=150)
        sf.txtchbr = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.cheese_burger, bd=2, width=4,
                           bg="white", justify='right')
        sf.txtchbr.place(x=400, y=150)

        sf.lblmus = Label(sf.admainf2, font=('Poppins', 14, 'bold'), text="Mushroom:", bg="#fdcb7a", fg="#7769ad",
                          bd=6, anchor='w')
        sf.lblmus.place(x=80, y=185)
        sf.opmus = OptionMenu(sf.admainf2, sf.vp3, *sf.l)
        sf.opmus.config(width=6)
        sf.opmus.place(x=265, y=190)
        sf.txtmus = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.mushroom, bd=2, width=4,
                          bg="white", justify='right')
        sf.txtmus.place(x=400, y=190)

        sf.lblcom = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Combo:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblcom.place(x=80, y=225)
        sf.opcom = OptionMenu(sf.admainf2, sf.vp4, *sf.l)
        sf.opcom.config(width=6)
        sf.opcom.place(x=265, y=230)
        sf.txtcom = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.combo, width=4,
                          bg="white", bd=2, justify='right')
        sf.txtcom.place(x=400, y=230)

        # sf.non veg

        sf.lbl2 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 17, 'bold'), bg="#fdcb7a",
                        text="NON-VEG BURGER", fg="brown", bd=10, anchor='w')
        sf.lbl2.place(x=140, y=300)
        sf.lbl21 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=6, bg="#fdcb7a",
                         text="Items", bd=6, anchor='w')
        sf.lbl21.place(x=80, y=350)
        sf.lbl22 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=7, bg="#fdcb7a",
                         text="Size", bd=6, anchor='w')
        sf.lbl22.place(x=260, y=350)
        sf.lbl23 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=8, bg="#fdcb7a",
                         text="Quantity", bd=6, anchor='w')
        sf.lbl23.place(x=360, y=350)

        sf.lblckn = Label(sf.admainf2, pady=0, font=('Poppins', 14, 'bold'), text="Chicken:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblckn.place(x=80, y=395)
        sf.opckn = OptionMenu(sf.admainf2, sf.vp5, *sf.l)
        sf.opckn.config(width=6)
        sf.opckn.place(x=265, y=400)
        sf.txtckn = Entry(sf.admainf2, width=4, font=('ariel', 14, 'bold'), textvariable=sf.chicken, bd=2,
                          bg="white", justify='right')
        sf.txtckn.place(x=400, y=400)

        sf.lblckcr = Label(sf.admainf2, pady=0, font=('Poppins', 14, 'bold'), text="Chicken Crispy:", bg="#fdcb7a",
                           fg="#7769ad", bd=6, anchor='w')
        sf.lblckcr.place(x=80, y=435)
        sf.opckcr = OptionMenu(sf.admainf2, sf.vp6, *sf.l)
        sf.opckcr.config(width=6)
        sf.opckcr.place(x=265, y=440)
        sf.txtckcr = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.chicken_crispy, bd=2, width=4,
                           bg="white", justify='right')
        sf.txtckcr.place(x=400, y=440)

        sf.lblckwh = Label(sf.admainf2, pady=0, font=('Poppins', 14, 'bold'), text="Chicken Whooper:", bg="#fdcb7a",
                           fg="#7769ad", bd=6, anchor='w')
        sf.lblckwh.place(x=80, y=475)
        sf.opckwh = OptionMenu(sf.admainf2, sf.vp7, *sf.l)
        sf.opckwh.config(width=6)
        sf.opckwh.place(x=265, y=480)
        sf.txtckwh = Entry(sf.admainf2, width=4, font=('ariel', 14, 'bold'), textvariable=sf.chicken_whooper, bd=2,
                           bg="white", justify='right')
        sf.txtckwh.place(x=400, y=480)

        sf.lblchch = Label(sf.admainf2, pady=0, font=('Poppins', 14, 'bold'), text="Chicken Cheese:", bg="#fdcb7a",
                           fg="#7769ad", bd=6, anchor='w')
        sf.lblchch.place(x=80, y=515)
        sf.opchch = OptionMenu(sf.admainf2, sf.vp8, *sf.l)
        sf.opchch.config(width=6)
        sf.opchch.place(x=265, y=520)
        sf.txtchch = Entry(sf.admainf2, font=('ariel', 14, 'bold'), width=4, textvariable=sf.chicken_cheese, bd=2,
                           bg="white", justify='right')
        sf.txtchch.place(x=400, y=520)

        # Special
        sf.lbl3 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 17), bg="#fdcb7a",
                        text="SPECIALTY", fg="brown", bd=10, anchor='w')
        sf.lbl3.place(x=630, y=10)
        sf.lbl31 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=6, bg="#fdcb7a",
                         text="Items", bd=6, anchor='w')
        sf.lbl31.place(x=550, y=60)
        sf.lbl33 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=8, bg="#fdcb7a",
                         text="Quantity", bd=6, anchor='w')
        sf.lbl33.place(x=780, y=60)

        sf.lblros = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Roasted Chicken:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblros.place(x=550, y=105)
        sf.txtros = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Roasted_Chicken, bd=2, width=4,
                          bg="white", justify='right')
        sf.txtros.place(x=820, y=110)

        sf.lblmeat = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Chicken Meatballs:", bg="#fdcb7a",
                           fg="#7769ad", bd=6, anchor='w')
        sf.lblmeat.place(x=550, y=145)
        sf.txtmeat = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Chicken_Meatballs, bd=2, width=4,
                           bg="white", justify='right')
        sf.txtmeat.place(x=820, y=150)

        sf.lblbon = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Boneless Chicken:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblbon.place(x=550, y=185)
        sf.txtbon = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Boneles_sChicken, bd=2, width=4,
                          bg="white", justify='right')
        sf.txtbon.place(x=820, y=190)

        # Sides
        sf.lbl4 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 17, 'bold'), bg="#fdcb7a",
                        text="SIDES", fg="#22aa00", bd=10, anchor='w')
        sf.lbl4.place(x=660, y=300)
        sf.lbl41 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=6, bg="#fdcb7a",
                         text="Items", bd=6, anchor='w')
        sf.lbl41.place(x=550, y=350)
        sf.lbl43 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 14), width=8, bg="#fdcb7a",
                         text="Quantity", bd=6, anchor='w')
        sf.lbl43.place(x=780, y=350)

        sf.lblcok = Label(sf.admainf2, pady=0, font=('Poppins', 14, 'bold'), text="Coke Mobile:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblcok.place(x=550, y=395)
        sf.txtcok = Entry(sf.admainf2, width=4, font=('ariel', 14, 'bold'), textvariable=sf.Coke_Mobile, bd=2,
                          bg="white", justify='right')
        sf.txtcok.place(x=820, y=400)

        sf.lblbur = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Burger Pizza:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblbur.place(x=550, y=435)
        sf.txtbur = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Burger_Pizza, bd=2, width=4,
                          bg="white", justify='right')
        sf.txtbur.place(x=820, y=440)

        sf.lblpas = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="White Pasta:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblpas.place(x=550, y=475)
        sf.txtpas = Entry(sf.admainf2, width=4, font=('ariel', 14, 'bold'), textvariable=sf.White_Pasta, bd=2,
                          bg="white", justify='right')
        sf.txtpas.place(x=820, y=480)

        # customer
        sf.lbl6 = Label(sf.admainf2, pady=2, font=('Montserrat ExtraBold', 17, 'bold'), bg="#fdcb7a",
                        text="CUSTOMER DETAILS", fg="#22aa00", bd=10, anchor='w')
        sf.lbl6.place(x=995, y=10)

        sf.lblnam = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), width=10, text="Name:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblnam.place(x=965, y=75)
        sf.txtnam = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Cutomer_name, bd=2, width=16,
                          bg="white", justify='left')
        sf.txtnam.place(x=1105, y=85)

        sf.lblmob = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Mobile No:", bg="#fdcb7a",
                          fg="#7769ad",
                          bd=6, anchor='w')
        sf.lblmob.place(x=965, y=115)
        sf.txtmob = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.cusmob, width=16, bd=2,
                          bg="white", justify='left')
        sf.txtmob.place(x=1105, y=125)

        # bill
        sf.lbl5 = Label(sf.admainf2, pady=0, font=('Montserrat ExtraBold', 17, 'bold'), bg="#fdcb7a",
                        text="BILL PAYMENT", fg="brown", bd=10, anchor='w')
        sf.lbl5.place(x=1030, y=170)

        sf.lblord = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), width=10, text="Order No:", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblord.place(x=965, y=235)
        sf.txtord = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.order, bd=2, width=16,
                          bg="white", justify='right')
        sf.txtord.place(x=1105, y=245)

        sf.lblco = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Subtotal:", bg="#fdcb7a",
                         fg="#7769ad",
                         bd=6, anchor='w')
        sf.lblco.place(x=965, y=275)
        sf.txtco = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.cost, width=16, bd=2,
                         bg="white", justify='right')
        sf.txtco.place(x=1105, y=285)

        sf.lblser = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="CGST (2.5%):", bg="#fdcb7a",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblser.place(x=965, y=315)
        sf.txtcgst = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.centralgst, width=16, bd=2,
                           bg="white", justify='right')
        sf.txtcgst.place(x=1105, y=325)

        sf.lbltax = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="SGST (2.5%):", bg="#fdcb7a",
                          fg="#7769ad", bd=6,
                          anchor='w')
        sf.lbltax.place(x=965, y=355)
        sf.txtsgst = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.stategst, bd=2, width=16,
                           bg="white", justify='right')
        sf.txtsgst.place(x=1105, y=365)

        sf.lbltot = Label(sf.admainf2, pady=2, font=('Poppins', 14, 'bold'), text="Total:", bg="#fdcb7a", fg="#7769ad",
                          bd=6, anchor='w')
        sf.lbltot.place(x=965, y=395)
        sf.txttot = Entry(sf.admainf2, font=('ariel', 14, 'bold'), textvariable=sf.Total, bd=2, width=16,
                          bg="white", justify='right')
        sf.txttot.place(x=1105, y=405)

        sf.btnprice = Button(sf.admainf2, pady=0, bd=0, bg="#fdcb7a", command=lambda: price(sf))
        sf.btnpriceimg = PhotoImage(file="Images/Buttons/pricebutton.png")
        sf.btnprice.config(image=sf.btnpriceimg)
        sf.btnprice.place(x=990, y=470)

        sf.btnTotal = Button(sf.admainf2, pady=0, bd=0, text="TOTAL", bg="#fdcb7a", command=lambda: Ref(sf))
        sf.btnTotalimg = PhotoImage(file="Images/Buttons/totalbutton.png")
        sf.btnTotal.config(image=sf.btnTotalimg)
        sf.btnTotal.place(x=1150, y=470)

        sf.btnreset = Button(sf.admainf2, pady=0, bd=0, text="RESET", bg="#fdcb7a", command=lambda: reset(sf))
        sf.btnresetimg = PhotoImage(file="Images/Buttons/resetbutton.png")
        sf.btnreset.config(image=sf.btnresetimg)
        sf.btnreset.place(x=990, y=540)

        sf.btnpay = Button(sf.admainf2, pady=0, bd=0, text="PAY", bg="#fdcb7a", command=lambda: sf.adminorderdetail())
        sf.btnpayimg = PhotoImage(file="Images/Buttons/paybutton.png")
        sf.btnpay.config(image=sf.btnpayimg)
        sf.btnpay.place(x=1150, y=540)

        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.admainf2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=85, y=563)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)
        sf.admainf2.pack(fill=BOTH, expand=1)

        sf.scr.mainloop()

    def resultadminorder(sf):
        r1 = sf.aloo_tikki.get()
        r2 = sf.cheese_burger.get()
        r3 = sf.mushroom.get()
        r4 = sf.combo.get()
        r5 = sf.chicken.get()
        r6 = sf.chicken_crispy.get()
        r7 = sf.chicken_whooper.get()
        r8 = sf.chicken_cheese.get()
        r9 = sf.Coke_Mobile.get()
        r10 = sf.Burger_Pizza.get()
        r11 = sf.White_Pasta.get()
        r12 = sf.Roasted_Chicken.get()
        r13 = sf.Chicken_Meatballs.get()
        r14 = sf.Boneles_sChicken.get()
        r20 = sf.Cutomer_name.get()
        r21 = sf.cusmob.get()
        r22 = sf.vp1.get()
        r23 = sf.vp2.get()
        r24 = sf.vp3.get()
        r25 = sf.vp4.get()
        r26 = sf.vp5.get()
        r27 = sf.vp6.get()
        r28 = sf.vp7.get()
        r29 = sf.vp8.get()
        r30 = sf.txtalt.get()
        r31 = sf.txtchbr.get()
        r32 = sf.txtmus.get()
        r33 = sf.txtcom.get()
        r34 = sf.txtckn.get()
        r35 = sf.txtckcr.get()
        r36 = sf.txtckwh.get()
        r37 = sf.txtchch.get()
        r38 = sf.txtros.get()
        r39 = sf.txtmeat.get()
        r40 = sf.txtbon.get()
        r41 = sf.txtcok.get()
        r42 = sf.txtbur.get()
        r43 = sf.txtpas.get()

        l1 = [r1, r22, 30]
        l2 = [r2, r23, 31]
        l3 = [r3, r24, 32]
        l4 = [r4, r25, 33]
        l5 = [r5, r26, 34]
        l6 = [r6, r27, 35]
        l7 = [r7, r28, 36]
        l8 = [r8, r29, 37]
        l9 = [r12, r38]
        l10 = [r13, r39]
        l11 = [r14, r40]
        l12 = [r9, r41]
        l13 = [r10, r42]
        l14 = [r11, r43]

        return r20, r21, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14

    # --  page 5------
    def menulist(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.menuf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.menuf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.menuf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.menuf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.menuf1.pack(fill=BOTH, expand=1)

        sf.menuf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.menuf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/var.png")
        sf.mal = Label(sf.menuf2, image=sf.logo1, height=618).place(x=-2, y=-2)
        sf.vgbt = Button(sf.menuf2, cursor="hand2", command=lambda: sf.vegburger(sf.x), bg="#fdcb7a", bd=0)
        sf.vgbt.place(x=180, y=400)
        sf.vgbtimg = PhotoImage(file="Images/Buttons/1.png")
        sf.vgbt.config(image=sf.vgbtimg)

        sf.nvgbt = Button(sf.menuf2, cursor="hand2", command=lambda: sf.nonvegburger(sf.x), bg="#fdcb7a", bd=0)
        sf.nvgbt.place(x=455, y=400)
        sf.nvgbtimg = PhotoImage(file="Images/Buttons/2.png")
        sf.nvgbt.config(image=sf.nvgbtimg)

        sf.spbt = Button(sf.menuf2, cursor="hand2", command=lambda: sf.SpecialChi(sf.x), bg="#fdcb7a", bd=0)
        sf.spbt.place(x=730, y=400)
        sf.spbtimg = PhotoImage(file="Images/Buttons/3.png")
        sf.spbt.config(image=sf.spbtimg)

        sf.sdbt = Button(sf.menuf2, cursor="hand2", command=lambda: sf.sidebev(sf.x), bg="#fdcb7a", bd=0)
        sf.sdbt.place(x=1005, y=400)
        sf.sdbtimg = PhotoImage(file="Images/Buttons/4.png")
        sf.sdbt.config(image=sf.sdbtimg)

        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.menuf2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)
        sf.menuf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 6------
    def burgmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.pizf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.pizf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.pizf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.pizf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.pizf1.pack(fill=BOTH, expand=1)

        sf.pizf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.pizf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/del.png")
        sf.mal = Label(sf.pizf2, image=sf.logo1, height=618).place(x=-2, y=-2)

        sf.de = Button(sf.pizf2, cursor="hand2", fg="white", command=lambda: sf.menulist("deli"),
                       bg="#fdcb7a", bd=0)
        sf.de.place(x=400, y=390)
        sf.deimg = PhotoImage(file="Images/Buttons/5.png")
        sf.de.config(image=sf.deimg)
        sf.pu = Button(sf.pizf2, cursor="hand2", command=lambda: sf.menulist("pick"), bd=0)
        sf.pu.place(x=810, y=390)
        sf.puimg = PhotoImage(file="Images/Buttons/6.png")
        sf.pu.config(image=sf.puimg)
        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.pizf2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)
        sf.pizf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 7------
    def vegburger(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.vegf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.vegf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.vegf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.vegf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.vegf1.pack(fill=BOTH, expand=1)

        sf.vegf2 = Frame(sf.scr, height=618, width=1366)

        sf.c = Canvas(sf.vegf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/5.png")
        sf.mal = Label(sf.vegf2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.q1 = StringVar()
        sf.q2 = StringVar()
        sf.q3 = StringVar()
        sf.q4 = StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # burger 1
        sf.labgh = Label(sf.vegf2, text="₹150/₹200/₹100", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=350, y=200)
        # ch1=sf.check(sf.vegf2,100)
        sf.v1 = IntVar()
        sf.C11 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v1, bg="#febc56")
        sf.C11.place(x=350, y=220)
        sf.C12 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v1, bg="#febc56")
        sf.C12.place(x=450, y=220)
        sf.C13 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v1, bg="#febc56")
        sf.C13.place(x=550, y=220)
        sf.C11.select()
        sf.C11.deselect()
        sf.C11.invoke()
        sf.labghi = Label(sf.vegf2, text="Quantity : ", bg="#febc56", fg="white", font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=245)
        sf.qty1 = Entry(sf.vegf2, textvariable=sf.q1, bg="white", font=("default", 12), width=4, )
        sf.qty1.place(x=455, y=245)
        sf.add1 = Button(sf.vegf2, text="ADD", command=lambda: addch1(), bg="#FF9A03", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add1.place(x=650, y=178)

        def addch1():
            if sf.v1.get() == 10:
                ch1 = "Medium"
                pric1 = 150
            elif sf.v1.get() == 20:
                ch1 = "Large"
                pric1 = 200
            else:
                ch1 = "Regular"
                pric1 = 100
            sf.addlist(["Aloo Tikki Burger", ch1, sf.q1.get(), pric1 * int(sf.q1.get())])

        # burger 2
        sf.labkl = Label(sf.vegf2, text="₹350/₹500/₹200", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labkl.place(x=350, y=410)
        ##        ch2=sf.check(sf.vegf2,220)
        sf.v2 = IntVar()

        sf.C21 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v2, bg="#febc56")
        sf.C21.place(x=350, y=430)
        sf.C22 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v2, bg="#febc56")
        sf.C22.place(x=450, y=430)
        sf.C23 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v2, bg="#febc56")
        sf.C23.place(x=550, y=430)
        sf.C21.select()
        sf.C21.deselect()
        sf.C21.invoke()
        sf.labghi = Label(sf.vegf2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=455)
        sf.qty2 = Entry(sf.vegf2, textvariable=sf.q2, bg="white", font=("default", 12), width=4, )
        sf.qty2.place(x=455, y=455)
        sf.add2 = Button(sf.vegf2, text="ADD", command=lambda: addch2(), bg="#FF9A03", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add2.place(x=650, y=378)

        def addch2():
            if sf.v2.get() == 10:
                ch2 = "Medium"
                pric2 = 350
            elif sf.v2.get() == 20:
                ch2 = "Large"
                pric2 = 500
            else:
                ch2 = "Regular"
                pric2 = 200

            sf.addlist(["Cheese Burger", ch2, sf.q2.get(), pric2 * int(sf.q2.get())])

        # burger 3
        sf.labgh = Label(sf.vegf2, text="₹385/₹550/₹225", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=960, y=200)
        # ch3=sf.check(sf.vegf2,340)
        sf.v3 = IntVar()
        sf.C31 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v3, bg="#febc56")
        sf.C31.place(x=960, y=220)
        sf.C32 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v3, bg="#febc56")
        sf.C32.place(x=1060, y=220)
        sf.C33 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v3, bg="#febc56")
        sf.C33.place(x=1160, y=220)
        sf.C31.select()
        sf.C31.deselect()
        sf.C31.invoke()

        sf.labghij = Label(sf.vegf2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=965, y=245)
        sf.qty3 = Entry(sf.vegf2, textvariable=sf.q3, bg="white", font=("default", 12), width=4, )
        sf.qty3.place(x=1065, y=245)

        sf.add3 = Button(sf.vegf2, text="ADD", command=lambda: addch3(), bg="#FF9A03", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add3.place(x=1220, y=173)

        def addch3():
            if sf.v3.get() == 10:
                ch3 = "Medium"
                pric3 = 385
            elif sf.v3.get() == 20:
                ch3 = "Large"
                pric3 = 550
            else:
                ch3 = "Regular"
                pric3 = 225
            sf.addlist(["Mushroom     ", ch3, sf.q3.get(), pric3 * int(sf.q3.get())])

        # burger 4
        sf.labghk = Label(sf.vegf2, text="₹295/₹485/₹199", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labghk.place(x=960, y=410)
        # ch4=sf.check(sf.vegf2,460)
        sf.v4 = IntVar()
        sf.C41 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v4, bg="#febc56")
        sf.C41.place(x=980, y=430)
        sf.C42 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v4, bg="#febc56")
        sf.C42.place(x=1080, y=430)
        sf.C43 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v4, bg="#febc56")
        sf.C43.place(x=1180, y=430)
        sf.C41.select()
        sf.C41.deselect()
        sf.C41.invoke()

        sf.labghij = Label(sf.vegf2, text="Quantity : ", bg="#febc56", fg="white",
                           font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=980, y=455)
        sf.qty4 = Entry(sf.vegf2, textvariable=sf.q4, bg="white", font=("default", 12), width=4, )
        sf.qty4.place(x=1080, y=455)

        sf.add4 = Button(sf.vegf2, text="ADD", command=lambda: addch4(), bg="#FF9A03", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add4.place(x=1220, y=378)

        def addch4():
            if sf.v4.get() == 10:
                ch4 = "Medium"
                pric4 = 295
            elif sf.v4.get() == 20:
                ch4 = "Large"
                pric4 = 485
            else:
                ch4 = "Regular"
                pric4 = 199
            sf.addlist(["Combo  ", ch4, sf.q4.get(), pric4 * int(sf.q4.get())])

        sf.con = Button(sf.vegf2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#FF9A03", cursor="hand2",
                        fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.con.place(x=500, y=520)
        sf.more = Button(sf.vegf2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#FF9A03", cursor="hand2",
                         fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.more.place(x=750, y=520)
        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.vegf2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)
        sf.vegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    def addlist(sf, q):
        if q[-2] != "0" and q[-2].isdigit():
            sf.cartlist.append(q)
            sf.amount = sf.amount + q[-1]
            messagebox.showinfo("Cart", "Item Successfully added")
        else:
            messagebox.showinfo("Cart", "Enter Valid Quantity to add")
        print(sf.cartlist, sf.amount)

    # --  page 8------
    def nonvegburger(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.nonvegf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.nonvegf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.nonvegf1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.nonvegf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.nonvegf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.nonvegf1.pack(fill=BOTH, expand=1)

        sf.nonvegf2 = Frame(sf.scr, height=618, width=1366)

        sf.c = Canvas(sf.nonvegf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/6.png")
        sf.mal = Label(sf.nonvegf2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.q5 = StringVar()
        sf.q6 = StringVar()
        sf.q7 = StringVar()
        sf.q8 = StringVar()
        sf.q5.set("0")
        sf.q6.set("0")
        sf.q7.set("0")
        sf.q8.set("0")
        # burger 1
        sf.labgh = Label(sf.nonvegf2, text="₹350/₹550/₹200", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=350, y=200)
        # ch5=sf.check(sf.nonvegf2,100)
        sf.v5 = IntVar()
        sf.C51 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v5, bg="#febc56")
        sf.C51.place(x=350, y=220)
        sf.C52 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v5, bg="#febc56")
        sf.C52.place(x=450, y=220)
        sf.C53 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v5, bg="#febc56")
        sf.C53.place(x=550, y=220)
        sf.C51.select()
        sf.C51.deselect()
        sf.C51.invoke()
        sf.labghi = Label(sf.nonvegf2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=245)
        sf.qty5 = Entry(sf.nonvegf2, textvariable=sf.q5, bg="white", font=("default", 12), width=4, )
        sf.qty5.place(x=455, y=245)

        sf.add5 = Button(sf.nonvegf2, text="ADD", command=lambda: addch5(), bg="#FF9A03", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add5.place(x=650, y=178)

        def addch5():
            if sf.v5.get() == 10:
                ch5 = "Medium"
                pric5 = 350
            elif sf.v5.get() == 20:
                ch5 = "Large"
                pric5 = 550
            else:
                ch5 = "Regular"
                pric5 = 200
            sf.addlist(["Chicken", ch5, sf.q5.get(), pric5 * int(sf.q5.get())])

        # burger 2
        sf.labkl = Label(sf.nonvegf2, text="₹400/₹600/₹250", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labkl.place(x=350, y=410)
        # ch6=sf.check(sf.nonvegf2,220)
        sf.v6 = IntVar()
        sf.C61 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v6, bg="#febc56")
        sf.C61.place(x=350, y=430)
        sf.C62 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v6, bg="#febc56")
        sf.C62.place(x=450, y=430)
        sf.C63 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v6, bg="#febc56")
        sf.C63.place(x=550, y=430)
        sf.C61.select()
        sf.C61.deselect()
        sf.C61.invoke()
        sf.labghi = Label(sf.nonvegf2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=455)
        sf.qty6 = Entry(sf.nonvegf2, textvariable=sf.q6, bg="white", font=("default", 12), width=4, )
        sf.qty6.place(x=455, y=455)

        sf.add6 = Button(sf.nonvegf2, text="ADD", command=lambda: addch6(), bg="#FF9A03", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add6.place(x=670, y=378)

        def addch6():
            if sf.v6.get() == 10:
                ch6 = "Medium"
                pric6 = 400
            elif sf.v6.get() == 20:
                ch6 = "Large"
                pric6 = 600
            else:
                ch6 = "Regular"
                pric6 = 250
            sf.addlist(["Chicken Crispy", ch6, sf.q6.get(), pric6 * int(sf.q6.get())])

        # burger 3
        sf.labgh = Label(sf.nonvegf2, text="₹385/₹550/₹225", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=960, y=200)
        # ch7=sf.check(sf.nonvegf2,340)
        sf.v7 = IntVar()
        sf.C71 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v7, bg="#febc56")
        sf.C71.place(x=960, y=220)
        sf.C72 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v7, bg="#febc56")
        sf.C72.place(x=1060, y=220)
        sf.C73 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v7, bg="#febc56")
        sf.C73.place(x=1160, y=220)
        sf.C71.select()
        sf.C71.deselect()
        sf.C71.invoke()
        sf.labghij = Label(sf.nonvegf2, text="Quantity : ", bg="#febc56", fg="white",
                           font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=965, y=245)
        sf.qty7 = Entry(sf.nonvegf2, textvariable=sf.q7, bg="white", font=("default", 12), width=4, )
        sf.qty7.place(x=1065, y=245)

        sf.add7 = Button(sf.nonvegf2, text="ADD", command=lambda: addch7(), bg="#FF9A03", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add7.place(x=1220, y=173)

        def addch7():
            if sf.v7.get() == 10:
                ch7 = "Medium"
                pric7 = 385
            elif sf.v7.get() == 20:
                ch7 = "Large"
                pric7 = 550
            else:
                ch7 = "Regular"
                pric7 = 225
            sf.addlist(["Chicken Whooper", ch7, sf.q7.get(), pric7 * int(sf.q7.get())])

        # burger 4
        sf.labghk = Label(sf.nonvegf2, text="₹295/₹485/₹199", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labghk.place(x=960, y=410)
        # ch8=sf.check(sf.nonvegf2,460)
        sf.v8 = IntVar()
        sf.C81 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v8, bg="#febc56")
        sf.C81.place(x=980, y=430)
        sf.C82 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v8, bg="#febc56")
        sf.C82.place(x=1080, y=430)
        sf.C83 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v8, bg="#febc56")
        sf.C83.place(x=1180, y=430)
        sf.C81.select()
        sf.C81.deselect()
        sf.C81.invoke()
        sf.labghij = Label(sf.nonvegf2, text="Quantity : ", bg="#febc56", fg="white",
                           font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=980, y=455)
        sf.qty8 = Entry(sf.nonvegf2, textvariable=sf.q8, bg="white", font=("default", 12), width=4, )
        sf.qty8.place(x=1080, y=455)
        sf.add8 = Button(sf.nonvegf2, text="ADD", command=lambda: addch8(), bg="#FF9A03", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add8.place(x=1220, y=378)

        def addch8():
            if sf.v8.get() == 10:
                ch8 = "Medium"
                pric8 = 295
            elif sf.v8.get() == 20:
                ch8 = "Large"
                pric8 = 485
            else:
                ch8 = "Regular"
                pric8 = 199
            sf.addlist(["Chicken Cheese", ch8, sf.q8.get(), pric8 * int(sf.q8.get())])

        sf.con = Button(sf.nonvegf2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#FF9A03",
                        cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.con.place(x=500, y=520)
        sf.more = Button(sf.nonvegf2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#FF9A03",
                         cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.more.place(x=750, y=520)

        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.nonvegf2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)
        sf.nonvegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 9------
    def SpecialChi(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.spef1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.spef1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.spef1, image=sf.logo, height=150).place(x=-2, y=0)
        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.spef1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.spef1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.spef1.pack(fill=BOTH, expand=1)

        sf.spef2 = Frame(sf.scr, height=618, width=1366)

        sf.c = Canvas(sf.spef2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/7.png")
        sf.mal = Label(sf.spef2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.q9 = StringVar()
        sf.q10 = StringVar()
        sf.q11 = StringVar()
        sf.q9.set("0")
        sf.q10.set("0")
        sf.q11.set("0")
        # burger 1
        sf.labgh = Label(sf.spef2, text="₹109", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=350, y=200)
        sf.labghi = Label(sf.spef2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=245)
        sf.qty9 = Entry(sf.spef2, textvariable=sf.q9, bg="white", font=("default", 12), width=4, )
        sf.qty9.place(x=455, y=245)
        sf.add9 = Button(sf.spef2, text="ADD", command=lambda: addch9(), bg="#FF9A03", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add9.place(x=650, y=173)

        def addch9():
            sf.addlist(["Roasted Chicken", str("Medium"), sf.q9.get(), 109 * int(sf.q9.get())])

        # burger 2
        sf.labkl = Label(sf.spef2, text="₹99", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labkl.place(x=350, y=410)
        sf.labghi = Label(sf.spef2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=455)
        sf.qty10 = Entry(sf.spef2, textvariable=sf.q10, bg="white", font=("default", 12), width=4, )
        sf.qty10.place(x=455, y=455)
        sf.add10 = Button(sf.spef2, text="ADD",
                          command=lambda: sf.addlist(
                              ["Chicken Meatballs", str("Medium"), sf.q10.get(), 99 * int(sf.q10.get())]),
                          bg="#FF9A03", cursor="hand2", fg="white", bd=4, font=("default", 12, 'bold'))
        sf.add10.place(x=670, y=378)
        # burger 3
        sf.labgh = Label(sf.spef2, text="₹139", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=960, y=200)
        sf.labghij = Label(sf.spef2, text="Quantity : ", bg="#febc56", fg="white",
                           font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=965, y=245)
        sf.qty11 = Entry(sf.spef2, textvariable=sf.q11, bg="white", font=("default", 12), width=4, )
        sf.qty11.place(x=1065, y=245)
        sf.add11 = Button(sf.spef2, text="ADD",
                          command=lambda: sf.addlist(
                              ["Boneless Chiken", str("Medium"), sf.q11.get(), 139 * int(sf.q11.get())]),
                          bg="#FF9A03", cursor="hand2", fg="white", bd=4, font=("default", 12, 'bold'))
        sf.add11.place(x=1220, y=173)
        sf.con = Button(sf.spef2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#FF9A03",
                        cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.con.place(x=500, y=520)
        sf.more = Button(sf.spef2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#FF9A03",
                         cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.more.place(x=750, y=520)
        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.spef2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)

        sf.spef2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 10------
    def sidebev(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.sidef1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.sidef1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="Images/Assets/logo.PNG")
        sf.ba = Label(sf.sidef1, image=sf.logo, height=150).place(x=-2, y=0)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.sidef1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.sidef1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.sidef1.pack(fill=BOTH, expand=1)

        sf.sidef2 = Frame(sf.scr, height=618, width=1366)

        sf.c = Canvas(sf.sidef2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="Images/Assets/8.png")
        sf.mal = Label(sf.sidef2, image=sf.logo1, height=618).place(x=-2, y=0)
        sf.q12 = StringVar()
        sf.q13 = StringVar()
        sf.q14 = StringVar()
        sf.q12.set("0")
        sf.q13.set("0")
        sf.q14.set("0")
        # burger 1
        sf.labgh = Label(sf.sidef2, text="₹45", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=350, y=200)
        sf.labghi = Label(sf.sidef2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=245)
        sf.qty12 = Entry(sf.sidef2, textvariable=sf.q12, bg="white", font=("default", 12), width=4, )
        sf.qty12.place(x=455, y=245)
        sf.add12 = Button(sf.sidef2, text="ADD",
                          command=lambda: sf.addlist(
                              ["Coke Moble", str("Medium"), sf.q12.get(), 45 * int(sf.q12.get())]),
                          bg="#FF9A03", cursor="hand2", fg="white", bd=4, font=("default", 12, 'bold'))
        sf.add12.place(x=650, y=173)
        # burger 2
        sf.labkl = Label(sf.sidef2, text="₹99", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labkl.place(x=350, y=410)
        sf.labghi = Label(sf.sidef2, text="Quantity : ", bg="#febc56", fg="white",
                          font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghi.place(x=355, y=455)
        sf.qty13 = Entry(sf.sidef2, textvariable=sf.q13, bg="white", font=("default", 12), width=4, )
        sf.qty13.place(x=445, y=455)
        sf.add13 = Button(sf.sidef2, text="ADD",
                          command=lambda: sf.addlist(
                              ["Burger Pizza", str("Medium"), sf.q13.get(), 99 * int(sf.q13.get())]),
                          bg="#FF9A03", cursor="hand2", fg="white", bd=4, font=("default", 12, 'bold'))
        sf.add13.place(x=670, y=378)
        # burger 3
        sf.labgh = Label(sf.sidef2, text="₹135", bg="#febc56", fg="white", font=("default", 10, 'bold'))
        sf.labgh.place(x=960, y=200)
        sf.labghij = Label(sf.sidef2, text="Quantity : ", bg="#febc56", fg="white",
                           font=("Montserrat ExtraBold", 10, 'bold'))
        sf.labghij.place(x=965, y=245)
        sf.qty14 = Entry(sf.sidef2, textvariable=sf.q14, bg="white", font=("default", 12), width=4, )
        sf.qty14.place(x=1065, y=245)
        sf.add14 = Button(sf.sidef2, text="ADD",
                          command=lambda: sf.addlist(
                              ["White Pasta", str("Medium"), sf.q14.get(), 135 * int(sf.q14.get())]),
                          bg="#FF9A03", cursor="hand2", fg="white", bd=4, font=("default", 12, 'bold'))
        sf.add14.place(x=1220, y=173)
        sf.con = Button(sf.sidef2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#FF9A03",
                        cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.con.place(x=500, y=520)
        sf.more = Button(sf.sidef2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#FF9A03",
                         cursor="hand2", fg="white", bd=3, font=("Montserrat ExtraBold", 12, 'bold'))
        sf.more.place(x=750, y=520)
        def logout():
            sf.akyn = messagebox.askyesno("Are you sure?", "Are you sure want to log out?")
            if sf.akyn:
                sf.Login()

        sf.out = Button(sf.sidef2, bg="#fdcb7a", cursor="hand2", command=lambda: logout(), bd=0)
        sf.out.place(x=10, y=580)
        sf.outimg = PhotoImage(file="Images/Buttons/logoutbutton.png")
        sf.out.config(image=sf.outimg)

        sf.sidef2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 11------
    def Address(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.addf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.addf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="Images/Assets/logo.png")
        sf.c.create_image(683, 75, image=sf.logo)
        ''''sf.out = Button(sf.addf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2", fg="white",
                        font=("default", 16))
        sf.out.place(x=1200, y=100)'''''

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.addf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.addf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.addf1.pack(fill=BOTH, expand=1)

        sf.addf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.addf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="burgermain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.addf2, text="Address", fg="white", bg="#0b1335", width=20, font=("default", 27))
        sf.log.place(x=480, y=110)
        sf.c.create_rectangle(150, 100, 1216, 450, fill="#d3ede6", outline="white", width=6)
        sf.lab1 = Label(sf.addf2, text="City", bg="#d3ede6", font=("cooper black", 18))
        sf.lab1.place(x=190, y=200)
        sf.city = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.city.place(x=430, y=200)
        sf.lab2 = Label(sf.addf2, text="Locality", bg="#d3ede6", font=("cooper black", 18))
        sf.lab2.place(x=730, y=200)
        sf.loc = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.loc.place(x=918, y=200)
        sf.lab3 = Label(sf.addf2, text="Building Name", bg="#d3ede6", font=("cooper black", 18))
        sf.lab3.place(x=190, y=250)
        sf.buil = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.buil.place(x=430, y=250)
        sf.lab4 = Label(sf.addf2, text="House No.", bg="#d3ede6", font=("cooper black", 18))
        sf.lab4.place(x=730, y=250)
        sf.hou = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.hou.place(x=918, y=250)
        sf.lab5 = Label(sf.addf2, text="Landmark", bg="#d3ede6", font=("cooper black", 18))
        sf.lab5.place(x=190, y=300)
        sf.lan = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.lan.place(x=430, y=300)
        sf.bc = Button(sf.addf2, text="Back", command=lambda: sf.Orderde(sf.x), cursor="hand2", fg="white",
                       bg="#0b1335", font=("default", 18), bd=5)
        sf.bc.place(x=370, y=370)
        sf.rg = Button(sf.addf2, text="Order Now", command=lambda: sf.orderpay(sf.x), cursor="hand2", fg="white",
                       bg="#0b1335", font=("default", 18), bd=5)
        sf.rg.place(x=610, y=370)

        def clear(sf):
            sf.city.delete(0, END)
            sf.loc.delete(0, END)
            sf.buil.delete(0, END)
            sf.hou.delete(0, END)
            sf.lan.delete(0, END)

        sf.cl = Button(sf.addf2, text="Clear", command=lambda: clear(sf), cursor="hand2", fg="white", bg="#0b1335",
                       font=("default", 18), bd=5)
        sf.cl.place(x=910, y=370)
        sf.addf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # --  page 12------
    def Orderde(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Burger Island")
        sf.scr.geometry("1366x768+80+10")
        sf.scr.resizable(False, False)
        file = "Images/Assets/burger.ico"
        sf.scr.iconbitmap(file)
        sf.ordf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.ordf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="Images/Assets/logo.png")
        sf.c.create_image(683, 75, image=sf.logo)

        def time():
            string = strftime('%I:%M:%S %p')
            sf.tim.config(text=string)
            sf.tim.after(1000, time)

        sf.stringdate = strftime('%d %b %Y')
        sf.strdat = Label(sf.ordf1, text=sf.stringdate, fg="black", font=("Montserrat ExtraBold", 15), bg="white")
        sf.strdat.place(x=1025, y=65)
        sf.tim = Label(sf.ordf1, fg="black", font=("Montserrat ExtraBold", 13), bg="white")
        sf.tim.place(x=1040, y=95)
        time()

        sf.ordf1.pack(fill=BOTH, expand=1)

        sf.ordf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.ordf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="burgermain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.ordf2, text="YOUR ORDER", bg="#9db1f2", font=("Cooper Black", 22))
        sf.log.place(x=450, y=4)
        sf.c.create_rectangle(250, 50, 800, 500, fill="#d3ede6", outline="white", width=6)
        sf.amt = sf.amount
        sf.text = "Total : " + str(sf.amt)
        sf.tot = Label(sf.ordf2, text=sf.text, bg="#f2da9d", width=12, font=("Cooper Black", 22))
        sf.tot.place(x=900, y=250)
        if sf.x == "deli":
            sf.y = sf.Address
        if sf.x == "pick":
            sf.y = sf.orderpay
        sf.pay = Button(sf.ordf2, text="Pay", command=lambda: sf.y(sf.x), bg="#0b1335", cursor="hand2", fg="white",
                        bd=5, font=("default", 18, 'bold'))
        sf.pay.place(x=900, y=300)
        sf.exi = Button(sf.ordf2, text="Add more", command=lambda: sf.menulist(sf.x), bg="#0b1335", cursor="hand2",
                        fg="white", bd=5, font=("default", 18, 'bold'))
        sf.exi.place(x=1070, y=300)
        sf.c.create_text(525, 80, text="Items\tSize\tQty\tPrice", font=("cooper black", 18))
        sf.c.create_text(525, 90, text="_______________________________________", font=("cooper black", 18))
        y = 100
        for i in sf.cartlist:
            y += 30
            s = i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + str(i[3])
            sf.c.create_text(525, y, text=s, font=("default", 16))

        sf.ordf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    # -----  database-------
    def logindatabase(sf):
        sf.credlog = sf.resultlog()
        sf.con = connect("burger.db")
        sf.cur = sf.con.cursor()
        try:
            sf.cur.execute(
                "create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x = sf.cur.execute(
            "select count(*) from customer where username=%r and password=%r" % (sf.credlog[0], sf.credlog[1]))
        if list(x)[0][0] == 0:
            if sf.credlog[0] == "" or sf.credlog[1] == "":
                messagebox.showinfo("Login", "Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login", "You are Not Registered Yet")

        else:
            y = sf.cur.execute(
                "select admin from customer where username=%r and password=%r" % (sf.credlog[0], sf.credlog[1]))
            for admin in y:
                if list(admin)[0] == 1:
                    messagebox.showinfo("Login",
                                        "You have Successfully Logged In\n\nWelcome to the Burger Island Admin")
                    sf.adminmain()
                else:
                    messagebox.showinfo("Login", "You have Successfully Log In\nWelcome to the Burger Island")
                    sf.burgmain()

    def Regdatabase(sf):
        sf.credreg = sf.resultreg()
        sf.con = connect("burger.db")
        sf.cur = sf.con.cursor()
        try:
            sf.cur.execute(
                "create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x = sf.cur.execute(
            "select count(*) from customer where username=%r and mob=%r " % (sf.credreg[0], sf.credreg[5]))
        if list(x)[0][0] == 0:
            if sf.credreg[0] == "" or sf.credreg[1] == "" or sf.credreg[2] == "" or sf.credreg[3] == "" or sf.credreg[
                5] == "":
                messagebox.showinfo("Register", "Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r,%r)" % (
                    sf.credreg[0], sf.credreg[1], sf.credreg[2], sf.credreg[3], sf.credreg[4], sf.credreg[5], 0))
                sf.con.commit()
                messagebox.showinfo("Register", "You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register", "Username Already Exist \nEnter New Username")

    def adminorderdetail(sf):
        sf.credadmord = sf.resultadminorder()
        if sf.money != 0 and sf.credadmord[0] != "" and sf.credadmord[1] != "":
            if messagebox.askyesno("Pay", "Want to make payment"):
                sf.con = connect("burger.db")
                sf.cur = sf.con.cursor()
                od = []
                try:
                    sf.cur.execute(
                        "create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                except:
                    pass
                for i in sf.credadmord[3:]:
                    if i[-1] != "0":
                        od.append(i)
                a = sf.credadmord[0]
                b = sf.credadmord[1]
                print(a, b, str(sf.money), od)
                s = "insert into orderdetail(name,mobile,money,orderdet) values(%r,%r,%r,%r)" % (
                    a, b, str(sf.money), str(od))
                sf.cur.execute(s)
                sf.con.commit()
                messagebox.showinfo("Pay", "Successfully Paid")
        else:
            messagebox.showinfo("Pay", "Enter Customer's Name and Mobile No  and  Order Something")

    # except:
    #   messagebox.showinfo("Pay","Enter Total button then Pay button")
    def orderpay(sf, x):
        messagebox.askquestion("Pay", "You will be redirected to a external page")
        sf.scr.destroy()
        import external


x = Burger()
x.Login()

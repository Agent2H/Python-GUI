from tkinter import *
from tkinter import Label
import os
from socket import *
import socket
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime
from datetime import timedelta


def delete0():
    screen.destroy()


def delete3():
    screen5.destroy()


def delete4():
    screen6.destroy()


def admin_main_interface():
    screen7.withdraw()
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Food Management Interface For Admin")
    screen9.geometry("1400x750")
    screen9.config(bg="cadet blue")

    FoodID = StringVar()
    Foodname = StringVar()
    Foodbrand = StringVar()
    Foodtype = StringVar()
    Foodnumber = StringVar()
    ExpiryDate = StringVar()
    ShipDate = StringVar()

    # ========================Functions========
    def update():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen9.txtFoodID.get()
        namestring = screen9.txtFoodname.get()
        brandstring = screen9.txtFoodbrand.get()
        typestring = screen9.txtFoodtype.get()
        numberstring = screen9.txtFoodnumber.get()
        expirystring = screen9.txtexpirydate.get()
        message = "u+" + idstring + "+" + namestring + "+" + brandstring + "+" + typestring + "+" + numberstring + "+" + expirystring
        '''
        client.send("u+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def Addnew():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen9.txtFoodID.get()
        namestring = screen9.txtFoodname.get()
        brandstring = screen9.txtFoodbrand.get()
        typestring = screen9.txtFoodtype.get()
        numberstring = screen9.txtFoodnumber.get()
        expirystring = screen9.txtexpirydate.get()
        message = "a+" + idstring + "+" + namestring + "+" + brandstring + "+" + typestring + "+" + numberstring + "+" + expirystring
        '''
        client.send("a+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())

        client.close()

    def Display():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        client.send("d".encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def erase():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen9.txtFoodID.get()
        namestring = screen9.txtFoodname.get()
        brandstring = screen9.txtFoodbrand.get()
        typestring = screen9.txtFoodtype.get()
        numberstring = screen9.txtFoodnumber.get()
        expirystring = screen9.txtexpirydate.get()
        message = "e+" + idstring + "+" + namestring + "+" + brandstring + "+" + typestring + "+" + numberstring + "+" + expirystring
        '''
        client.send("t+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def inquirybrand():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen9.txtFoodID.get()
        namestring = screen9.txtFoodname.get()
        brandstring = screen9.txtFoodbrand.get()
        typestring = screen9.txtFoodtype.get()
        numberstring = screen9.txtFoodnumber.get()
        expirystring = screen9.txtexpirydate.get()
        message = "s+++" + brandstring + "+++"
        '''
        client.send("s+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def inquirytype():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen9.txtFoodID.get()
        namestring = screen9.txtFoodname.get()
        brandstring = screen9.txtFoodbrand.get()
        typestring = screen9.txtFoodtype.get()
        numberstring = screen9.txtFoodnumber.get()
        expirystring = screen9.txtexpirydate.get()
        message = "t++++" + typestring + "++"
        '''
        client.send("t+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def iExit():
        iExit = tkinter.messagebox.askyesno("Food Management Interface For User", "Confirm if you want to exit")
        if iExit > 0:
            screen9.destroy()
            return

    # ===========Frames====================
    MainFrame = Frame(screen9, bg="cadet blue")
    MainFrame.grid()

    TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
    TitFrame.pack(side=TOP)

    screen9.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Food Warehouse Management System",
                           bg="Ghost White")
    screen9.lblTit.grid()

    ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=300, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                               font=('arial', 20, 'bold'), text="Food Info\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White",
                                font=('arial', 20, 'bold'), text="Food Details\n")
    DataFrameRight.pack(side=RIGHT)

    # =============================Labels and Entry Widget=======================================
    screen9.lblFoodID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food ID:", padx=2, pady=2,
                              bg="Ghost White")
    screen9.lblFoodID.grid(row=0, column=0, sticky=W)
    screen9.txtFoodID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=FoodID, width=39)
    screen9.txtFoodID.grid(row=0, column=1)

    screen9.lblFoodname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food name:", padx=2, pady=2,
                                bg="Ghost White")
    screen9.lblFoodname.grid(row=1, column=0, sticky=W)
    screen9.txtFoodname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodname, width=39)
    screen9.txtFoodname.grid(row=1, column=1)

    screen9.lblFoodbrand = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food brand:", padx=2, pady=2,
                                 bg="Ghost White")
    screen9.lblFoodbrand.grid(row=2, column=0, sticky=W)
    screen9.txtFoodbrand = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodbrand, width=39)
    screen9.txtFoodbrand.grid(row=2, column=1)

    screen9.lblFoodtype = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food type:", padx=2, pady=2,
                                bg="Ghost White")
    screen9.lblFoodtype.grid(row=3, column=0, sticky=W)
    screen9.txtFoodtype = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodtype, width=39)
    screen9.txtFoodtype.grid(row=3, column=1)

    screen9.lblFoodnumber = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food quantity:", padx=2, pady=2,
                                  bg="Ghost White")
    screen9.lblFoodnumber.grid(row=4, column=0, sticky=W)
    screen9.txtFoodnumber = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodnumber, width=39)
    screen9.txtFoodnumber.grid(row=4, column=1)
    screen9.lblshipdate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Shipment:", padx=2, pady=2,
                                bg="Ghost White")
    screen9.lblshipdate.grid(row=5, column=0, sticky=W)
    screen9.txtshipdate = DateEntry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ShipDate, width=39)
    screen9.txtshipdate.grid(row=5, column=1)
    screen9.lblexpirydate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Expiry:", padx=2, pady=2,
                                  bg="Ghost White")
    screen9.lblexpirydate.grid(row=6, column=0, sticky=W)
    screen9.txtexpirydate = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ExpiryDate, width=39)
    screen9.txtexpirydate.grid(row=6, column=1)
    # =======================================ListBox & ScrollBar Widget===========================
    scrollbar = Scrollbar(DataFrameRight)
    scrollbar.grid(row=0, column=1, sticky='ns')

    foodlist = Listbox(DataFrameRight, width=60, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
    foodlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=foodlist.yview)

    # =======================================Button Widget========================================
    screen9.btnregister = Button(ButtonFrame, text="Register", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=Addnew)

    screen9.btnregister.grid(row=0, column=0)
    screen9.btndisplay = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=Display)
    screen9.btndisplay.grid(row=0, column=1)
    screen9.btnupdate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                               command=update)
    screen9.btnupdate.grid(row=0, column=2)
    screen9.btninquirybrand = Button(ButtonFrame, text="Brand Inquiry", font=('arial', 20, 'bold'), height=1, width=10,
                                     bd=4,
                                     command=inquirybrand)
    screen9.btninquirybrand.grid(row=0, column=3)
    screen9.btninquirytype = Button(ButtonFrame, text="Type Inquiry", font=('arial', 20, 'bold'), height=1,
                                    width=10, bd=4,
                                    command=inquirytype)
    screen9.btninquirytype.grid(row=0, column=4)
    screen9.btndelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                               command=erase)
    screen9.btndelete.grid(row=0, column=5)
    screen9.btnexit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                             command=iExit)
    screen9.btnexit.grid(row=0, column=6)


def user_main_interface():
    screen3.withdraw()
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Food Management Interface For User")
    screen8.geometry("1400x750")
    screen8.config(bg="cadet blue")

    FoodID = StringVar()
    Foodname = StringVar()
    Foodbrand = StringVar()
    Foodtype = StringVar()
    Foodnumber = StringVar()
    ShipDate = StringVar()
    ExpiryDate = StringVar()

    # ===========Function==================

    def Addnew():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen8.txtFoodID.get()
        namestring = screen8.txtFoodname.get()
        brandstring = screen8.txtFoodbrand.get()
        typestring = screen8.txtFoodtype.get()
        numberstring = screen8.txtFoodnumber.get()
        expirystring = screen8.txtexpirydate.get()
        message = "a+" + idstring + "+" + namestring + "+" + brandstring + "+" + typestring + "+" + numberstring + "+" + expirystring
        '''
        client.send("a+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        client.close()

    def Display():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        client.send("d".encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def erase():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen8.txtFoodID.get()
        namestring = screen8.txtFoodname.get()
        brandstring = screen8.txtFoodbrand.get()
        typestring = screen8.txtFoodtype.get()
        numberstring = screen8.txtFoodnumber.get()

        expirystring = screen8.txtexpirydate.get()
        message = "e+" + idstring + "+" + namestring + "+" + brandstring + "+" + typestring + "+" + numberstring + "+" + expirystring
        '''
        client.send("e+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()

        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def inquirybrand():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen8.txtFoodID.get()
        namestring = screen8.txtFoodname.get()
        brandstring = screen8.txtFoodbrand.get()
        typestring = screen8.txtFoodtype.get()
        numberstring = screen8.txtFoodnumber.get()

        expirystring = screen8.txtexpirydate.get()
        message = "s+++" + brandstring + "+++"
        '''
        client.send("s+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()
        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def inquirytype():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 54000))
        foodlist.delete(0, END)
        idstring = screen8.txtFoodID.get()
        namestring = screen8.txtFoodname.get()
        brandstring = screen8.txtFoodbrand.get()
        typestring = screen8.txtFoodtype.get()
        numberstring = screen8.txtFoodnumber.get()

        expirystring = screen8.txtexpirydate.get()
        message = "t++++" + typestring + "++"
        '''
        client.send("t+".encode())
        client.send(idstring.encode())
        client.send("+".encode())
        client.send(namestring.encode())
        client.send("+".encode())
        client.send(brandstring.encode())
        client.send("+".encode())
        client.send(typestring.encode())
        client.send("+".encode())
        client.send(numberstring.encode())
        client.send("+".encode())
        client.send(unitstring.encode())
        client.send("+".encode())
        client.send(storagestring.encode())
        client.send("+".encode())
        client.send(expirystring.encode())
        '''
        client.send(message.encode())
        from_server = client.recv(4096).decode()
        client.close()
        print(from_server)
        x = from_server.split('\n')
        for i in x:
            foodlist.insert(END, i)

    def iExit():
        iExit = tkinter.messagebox.askyesno("Food Management Interface For User", "Confirm if you want to exit")
        if iExit > 0:
            screen8.destroy()
            return

    def callback():
        if Foodtype.get() == "Refrigerated":
            screen8.txtexpirydate.insert(0, screen8.txtshipdate.get_date() + timedelta(days=365))
        elif Foodtype.get() == "Room":
            screen8.txtexpirydate.insert(0, screen8.txtshipdate.get_date() + timedelta(days=30))
        elif Foodtype.get() == "Frozen":
            screen8.txtexpirydate.insert(0, screen8.txtshipdate.get_date() + timedelta(days=730))
        return 0
    # ===========Frames====================
    MainFrame = Frame(screen8, bg="cadet blue")
    MainFrame.grid()

    TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
    TitFrame.pack(side=TOP)

    screen8.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Food Warehouse Management System",
                           bg="Ghost White")
    screen8.lblTit.grid()

    ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                               font=('arial', 20, 'bold'), text="Food Info\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White",
                                font=('arial', 20, 'bold'), text="Food Details\n")
    DataFrameRight.pack(side=RIGHT)

    # =============================Labels and Entry Widget=======================================
    screen8.lblFoodID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food ID:", padx=2, pady=2,
                              bg="Ghost White")
    screen8.lblFoodID.grid(row=0, column=0, sticky=W)
    screen8.txtFoodID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=FoodID, width=39)
    screen8.txtFoodID.grid(row=0, column=1)

    screen8.lblFoodname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food name:", padx=2, pady=2,
                                bg="Ghost White")
    screen8.lblFoodname.grid(row=1, column=0, sticky=W)
    screen8.txtFoodname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodname, width=39)
    screen8.txtFoodname.grid(row=1, column=1)

    screen8.lblFoodbrand = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food brand:", padx=2, pady=2,
                                 bg="Ghost White")
    screen8.lblFoodbrand.grid(row=2, column=0, sticky=W)
    screen8.txtFoodbrand = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodbrand, width=39)
    screen8.txtFoodbrand.grid(row=2, column=1)

    screen8.lblFoodtype = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food type:", padx=2, pady=2,
                                bg="Ghost White")
    screen8.lblFoodtype.grid(row=3, column=0, sticky=W)
    screen8.txtFoodtype = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodtype, validate="focusout",
                                validatecommand=callback, width=39)
    screen8.txtFoodtype.grid(row=3, column=1)

    screen8.lblFoodnumber = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Food quantity:", padx=2, pady=2,
                                  bg="Ghost White")
    screen8.lblFoodnumber.grid(row=4, column=0, sticky=W)
    screen8.txtFoodnumber = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Foodnumber, width=39)
    screen8.txtFoodnumber.grid(row=4, column=1)
    screen8.lblshipdate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Shipment:", padx=2, pady=2,
                                bg="Ghost White")
    screen8.lblshipdate.grid(row=5, column=0, sticky=W)
    screen8.txtshipdate = DateEntry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ShipDate, width=39)
    screen8.txtshipdate.grid(row=5, column=1)
    screen8.lblexpirydate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of expiration:", padx=2, pady=2,
                                  bg="Ghost White")
    screen8.lblexpirydate.grid(row=6, column=0, sticky=W)
    screen8.txtexpirydate = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ExpiryDate, width=39)
    screen8.txtexpirydate.grid(row=6, column=1)
    '''
    if StorageType.get() == "Refrigerated":
        ExpiryDate == screen8.txtshipdate.selection_get() + timedelta(days=4)
    '''
    # =======================================ListBox & ScrollBar Widget===========================
    scrollbar = Scrollbar(DataFrameRight)
    scrollbar.grid(row=0, column=1, sticky='ns')

    foodlist = Listbox(DataFrameRight, width=60, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
    foodlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=foodlist.yview)

    # =======================================Button Widget========================================
    screen8.btnregister = Button(ButtonFrame, text="Register", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=Addnew)

    screen8.btnregister.grid(row=0, column=0)
    screen8.btndisplay = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=Display)
    screen8.btndisplay.grid(row=0, column=1)

    screen8.btninquirybrand = Button(ButtonFrame, text="Brand Inquiry", font=('arial', 20, 'bold'), height=1, width=10,
                                     bd=4,
                                     command=inquirybrand)
    screen8.btninquirybrand.grid(row=0, column=2)
    screen8.btninquirytype = Button(ButtonFrame, text="Type Inquiry", font=('arial', 20, 'bold'), height=1,
                                    width=10, bd=4,
                                    command=inquirytype)
    screen8.btninquirytype.grid(row=0, column=3)
    screen8.btndelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                               command=erase)
    screen8.btndelete.grid(row=0, column=4)
    screen8.btnexit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                             command=iExit)
    screen8.btnexit.grid(row=0, column=5)


def login_success_admin():
    admin_main_interface()


def login_success_user():
    user_main_interface()


def password_not_recognised():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="Wrong Password").pack()
    Button(screen5, text="OK", command=delete3).pack()


def user_not_found():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Success")
    screen6.geometry("150x100")
    Label(screen6, text="User Not Found").pack()
    Button(screen6, text="OK", command=delete4).pack()


def register_user():
    print("Working..")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def admin_login_verify():
    username2 = username_verify2.get()
    password2 = password_verify2.get()
    username_entry2.delete(0, END)
    password_entry2.delete(0, END)

    file2 = open("Admin.txt", "r")
    lines = file2.readlines()
    if username2 in lines[0]:
        if password2 in lines[1]:
            login_success_admin()
        else:
            password_not_recognised()
    else:
        user_not_found()


def user_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success_user()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    screen.withdraw()
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="ID").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def access_permission():
    screen.withdraw()
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Access permission")
    screen2.geometry("300x250")
    Label(screen2, text="Please choose your access permission").pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Admin", height="2", width="30", command=admin).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="User", height="2", width="30", command=user).pack()


def admin():
    screen2.withdraw()
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Admin Login")
    screen7.geometry("300x250")
    Label(screen7, text="Please enter details below to login").pack()
    Label(screen7, text="").pack

    global username_verify2
    global password_verify2

    username_verify2 = StringVar()
    password_verify2 = StringVar()

    global username_entry2
    global password_entry2

    Label(screen7, text="Username").pack()
    username_entry2 = Entry(screen7, textvariable=username_verify2)
    username_entry2.pack()
    Label(screen7, text="").pack()
    Label(screen7, text="Password").pack()
    password_entry2 = Entry(screen7, textvariable=password_verify2)
    password_entry2.pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Login", width=10, height=1, command=admin_login_verify).pack()


def user():
    screen2.withdraw()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("User Login")
    screen3.geometry("300x250")
    Label(screen3, text="Please enter details below to login").pack()
    Label(screen3, text="").pack

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen3, text="Username").pack()
    username_entry1 = Entry(screen3, textvariable=username_verify)
    username_entry1.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Password").pack()
    password_entry1 = Entry(screen3, textvariable=password_verify)
    password_entry1.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Login", width=10, height=1, command=user_login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("FOOD MANAGEMENT")
    Label(text="", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=access_permission).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 54000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

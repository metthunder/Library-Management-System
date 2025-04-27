from tkinter import*
from PIL import ImageTk,Image 
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sqltr
file=open(".details.txt","a+")
file.seek(0)
x=file.readlines()
if len(x)==0:
    print("WE NEED SOME OF YOUR DETAILS FOR FUTURE REFERENCE:")
    user_name=input("ENTER YOUR NAME:")
    file.write(user_name)
    file.write("\n")
    mysql_password=input("ENTER YOUR MYSQL PASSWORD:")
    file.write(mysql_password)
    file.write("\n")
    app_password=input("SET A PASSWORD FOR THIS MANAGEMENT SYSTEM:")
    file.write(app_password)
    file.close()
    z=1
else:
    z=0
    file.seek(0)
    l=file.readlines()
    user_name=l[0]
    mysql_password=l[1][0:-1]
    app_password=l[2]
    file.close()
def passw():
    ini.iconify()
    mydb=sqltr.connect(host="localhost",user="root",password=mysql_password)
    if mydb.is_connected():
        print("Successfully Connected to Mysql Database.")
    else:
        print("Facing Some Problems In Connecting With Mysql Database.")
        return
    cur=mydb.cursor()
    cur.execute("create database if not exists Library_Management_System")
    cur.execute("use Library_Management_System")
    cur.execute("create table if not exists book_info(BOOKID int(10) primary key, BOOK_NAME varchar(50) not null, AUTHOR_NAME varchar(50) not null,AVAILABILITY int(5))")
    #library management system(main window)
    global log
    global imag
    window=Toplevel()
    window.iconify()
    window.state("zoomed")
    window.geometry("1425x800")
    window.attributes("-fullscreen", True)
    window.bind("<F11>", lambda event: window.attributes("-fullscreen",
                                       not window.attributes("-fullscreen")))
    window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))
    window.configure(bg='black')
    window.title("LIBRARY MANAGEMENT SYSTEM  =_=  ^_^")
    global blogo
    global image3
    blogo=Image.open('Image\\book club.PNG')
    image3=blogo.resize((180,180),Image.ANTIALIAS)
    blogo=ImageTk.PhotoImage(image3)
    picture3=Label(window,image=blogo,relief="solid")
    picture3.place(x=1100,y=20)
    log=Image.open('Image\\logo.PNG')
    imag=log.resize((180,180),Image.ANTIALIAS)
    log=ImageTk.PhotoImage(imag)
    picture1=Label(window,image=log,relief="solid")
    picture1.place(x=80,y=20)
    label1=Label(window,text="LIBRARY MANAGEMENT SYSTEM",relief="solid",width="25",bg='black',fg='antique white',font=("chopsic",30,"bold"))
    label1.pack(pady=6)
    label1=Label(window,text="ARMY PUBLIC SCHOOL",width="25",bg='black',fg='antique white',font=("cabin sketch",38,"bold","underline"))
    label1.pack(pady=10)
    label1=Label(window,text="Welcome to library management system!!!",width="37",bg='black',fg='antique white',font=("CookieMonster",23,"italic"))
    label1.pack(pady=10)
    label=Label(window,text="I HAVE ALWAYS IMAGINED THAT PARADISE WILL BE A KIND OF LIBRARY.",width="70",fg='antique white',bg='black',font=("bradley hand itc",16,"bold"))
    label.pack(pady=10)
    global libra
    global image2
    libr=Image.open('Image\\mp.PNG')
    image2=libr.resize((800,500),Image.ANTIALIAS)
    libra=ImageTk.PhotoImage(image2)
    picture1=Label(window,image=libra,relief="solid")
    picture1.pack(padx=30,pady=20,anchor='nw',side='left')
    def exitt():
        ini.destroy()
        exit()
#========================================================================================================
    #BOOK INFORMATION SYSTEM(function defining)
    def hit1():                              #to open book information system
        def hit11():                         #inserting a record
            window11=Tk()
            window11.geometry("550x350")
            window11.configure(bg='black')
            window11.title("INSERTING INFORMATION OF NEW BOOK...")
            label2=Label(window11,text="ENTER BOOK ID  :",width="25",bg='black',fg='antique white',font=("bradley hand itc",15,'bold')).grid(row=1,column=1)
            BookID=Entry(window11)
            BookID.grid(row=1,column=2)
            label2=Label(window11,text="ENTER BOOK NAME  :",bg='black',fg='antique white',width="25",font=("bradley hand itc",15,'bold')).grid(row=2,column=1)
            BookName=Entry(window11)
            BookName.grid(row=2,column=2)
            label2=Label(window11,text="ENTER AUTHOR NAME  :",bg='black',fg='antique white',width="25",font=("bradley hand itc",15,'bold')).grid(row=3,column=1)
            AuthorName=Entry(window11)
            AuthorName.grid(row=3,column=2)
            label2=Label(window11,text="ENTER STOCK  :",width="25",bg='black',fg='antique white',font=("bradley hand itc",15,'bold')).grid(row=4,column=1)
            Stock=Entry(window11)
            Stock.grid(row=4,column=2)
            def insertt():
                if len(BookID.get())>0 and len(BookName.get())>0 and len((AuthorName.get()))>0 and len((Stock.get()))>0:
                    cur.execute("select count(*) from book_info where bookid={}".format(BookID.get()))
                    b=cur.fetchone()
                    if b[0]==0:
                        cur.execute("insert into book_info values({},'{}','{}',{})".format(BookID.get(),BookName.get(),AuthorName.get(),Stock.get()))
                        mydb.commit()
                        window11.destroy()
                        messagebox.showinfo("INFORMATION","RECORD INSERTED SUCCESSFULLY")
                    else:
                        messagebox.showwarning("Try another BOOK ID","Book with this book ID already exists")
                else:
                    messagebox.showwarning("Invalid Insertion","All entries must be filled!")
            b1=Button(window11,text="SUBMIT",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=insertt)
            b1.grid(row=8,column=1,pady=10)                
        def hit12():                   #updating a record
            window12=Tk()
            window12.geometry("700x400")
            window12.configure(bg='black')
            window12.title("UPDATING A BOOK INFO...")
            label=Label(window12,text="WHICH VALUE DO YOU WANT TO UPDATE:",bg='black',fg='antique white',width="40",font=("bradley hand itc",20,"italic","bold"))
            label.grid(row=1)
            n=StringVar()
            upd=ttk.Combobox(window12,width=28,textvariable=n)
            upd['values']=('--SELECT CATEGORY--','BOOK NAME','AUTHOR NAME','STOCK')
            upd.grid(row=3)
            upd.current(0)
            def updating():
                def update1():
                    if len(OBkn.get())>0 and len(NBkn.get())>0:
                        cur.execute("select count(*) from book_info where BOOKID={}".format(OBkn.get()))
                        n=cur.fetchone()
                        if n[0]>0:                        
                            cur.execute("update book_info set book_name='{}' where BOOKID={}".format(NBkn.get(),OBkn.get()))
                            mydb.commit()
                            window12.destroy()
                            messagebox.showinfo("INFORMATION","UPDATED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID UPDATION","No book with such book ID exists")
                    else:
                        messagebox.showwarning("WARNING","All entries must be filled!")
                def update2():
                    if len(NATn.get())>0 and len(OATn.get())>0:
                        cur.execute("select count(*) from book_info where BOOKID={}".format(OATn.get()))
                        n=cur.fetchone()
                        if n[0]>0: 
                            cur.execute("update book_info set author_name='{}' where BOOKID={}".format(NATn.get(),OATn.get()))
                            mydb.commit()
                            window12.destroy()
                            messagebox.showinfo("INFORMATION","UPDATED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID UPDATION","No book with such book ID exists")
                    else:
                        messagebox.showwarning("WARNING","All entries must be filled!")
                def update3():
                    if len(NSn.get())>0 and len(OSn.get())>0:
                        cur.execute("select count(*) from book_info where BOOKID={}".format(OSn.get()))
                        n=cur.fetchone()
                        if n[0]>0: 
                            cur.execute("update book_info set availability={} where BOOKID={}".format(NSn.get(),OSn.get()))
                            mydb.commit()
                            window12.destroy()
                            messagebox.showinfo("INFORMATION","UPDATED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID UPDATION","No book with such book ID exists")
                    else:
                        messagebox.showwarning("WARNING","All entries must be filled!")
                if upd.current()==1:
                    Label(window12,text="BOOK ID:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    OBkn=Entry(window12)
                    OBkn.grid(row=10,column=0)
                    Label(window12,text="NEW BOOK NAME:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=12)
                    NBkn=Entry(window12)
                    NBkn.grid(row=14,column=0)
                    Button(window12,text="UPDATE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=update1).grid(row=16,column=0,pady=10)
                if upd.current()==2:
                    Label(window12,text="BOOK ID:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    OATn=Entry(window12)
                    OATn.grid(row=10,column=0)
                    Label(window12,text="NEW AUTHOR NAME:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=12)
                    NATn=Entry(window12)
                    NATn.grid(row=14,column=0)
                    Button(window12,text="UPDATE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=update2).grid(row=16,column=0,pady=10)
                if upd.current()==3:
                    Label(window12,text="BOOK ID:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    OSn=Entry(window12)
                    OSn.grid(row=10,column=0)
                    Label(window12,text="NEW STOCK:",bg='black',fg='antique white',width="20",font=("bradley hand itc",20,"italic","bold")).grid(row=12)
                    NSn=Entry(window12)
                    NSn.grid(row=14,column=0)
                    Button(window12,text="UPDATE",activebackground="black",bg='black',fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=update3).grid(row=16,column=0,pady=10)
              
            Button(window12,text="SUBMIT",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=updating).grid(row=6,column=0,pady=10)
        def hit13():                         #deletion of record
            window13=Tk()
            window13.geometry("500x300")
            window13.configure(bg='black')
            window13.title("DELETION OF RECORD...")
            label=Label(window13,text="DELETE RECORD HAVING:",bg='black',fg='antique white',width="30",font=("bradley hand itc",20,"italic","bold"))
            label.grid(row=1)
            n=StringVar()
            delet=ttk.Combobox(window13,width=35,textvariable=n)
            delet['values']=('--SELECT CATEGORY--','BOOK ID','BOOK NAME','AUTHOR NAME')
            delet.grid(row=3)
            delet.current(0)
            def deleting():
                def delet1():
                    if len(Bki.get())>0:
                        cur.execute("select count(*) from book_info where bookid={}".format(Bki.get()))
                        n=cur.fetchone()
                        if n[0]>0:
                            cur.execute("delete from book_info where bookid={}".format(Bki.get()))
                            mydb.commit()
                            window13.destroy()
                            messagebox.showinfo("INFORMATION","DELETED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID DELETION","No book exists with such book ID")
                    else:
                        messagebox.showwarning("WARNING","Please enter Book ID!")
                def delet2():
                    if len(Bname.get())>0:
                        cur.execute("select count(*) from book_info where book_name='{}'".format(Bname.get()))
                        n=cur.fetchone()
                        if n[0]>0:
                            cur.execute("delete from book_info where book_name='{}'".format(Bname.get()))
                            mydb.commit()
                            window13.destroy()
                            messagebox.showinfo("INFORMATION","DELETED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID DELETION","No book exists with such name")
                    else:
                        messagebox.showwarning("WARNING","Please enter Book name!")
                def delet3():
                    if len(An.get())>0:
                        cur.execute("select count(*) from book_info where author='{}'".format(An.get()))
                        n=cur.fetchone()
                        if n[0]>0:
                            cur.execute("delete from book_info where author='{}'".format(An.get()))
                            mydb.commit()
                            window13.destroy()
                            messagebox.showinfo("INFORMATION","DELETED SUCCESSFULLY")
                        else:
                            messagebox.showwarning("INVALID DELETION","No book exists with such Author name")
                    else:
                        messagebox.showwarning("WARNING","Please enter Author name!")
                if delet.current()==1:
                    Label(window13,text="BOOK ID:",bg='black',fg='antique white',width="15",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    Bki=Entry(window13)
                    Bki.grid(row=10,column=0)
                    Button(window13,text="DELETE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=delet1).grid(row=12,column=0,pady=10)
                if delet.current()==2:
                    Label(window13,text="BOOK NAME:",bg='black',fg='antique white',width="15",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    Bname=Entry(window13)
                    Bname.grid(row=10,column=0)
                    Button(window13,text="DELETE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=delet2).grid(row=12,column=0,pady=10)
                if delet.current()==3:
                    Label(window13,text="AUTHOR NAME:",bg='black',fg='antique white',width="15",font=("bradley hand itc",20,"italic","bold")).grid(row=8)
                    An=Entry(window13)
                    An.grid(row=10,column=0)
                    Button(window13,text="DELETE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=delet3).grid(row=12,column=0,pady=10)
            Button(window13,text="SUBMIT",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=deleting).grid(row=6,column=0,pady=10)
        def hit14():#display of record
            cur.execute("select count(*) from book_info")
            n=cur.fetchone()
            if n[0]>0:
                window14=Tk()
                window14.geometry("1340x730")            
                window14.config(bg='black')
                window14.title("DISPLAYING RECORDS...")
                cur.execute("select* from book_info")
                label=Label(window14,text="BOOK ID",width="15",bg='black',fg='antique white',font=("a alloy ink",20,"italic"))
                label.grid(row=0,column=0)
                label=Label(window14,text="BOOK NAME",width="20",bg='black',fg='antique white',font=("a alloy ink",20,"italic"))
                label.grid(row=0,column=1)
                label=Label(window14,text="AUTHOR NAME",width="20",bg='black',fg='antique white',font=("a alloy ink",20,"italic"))
                label.grid(row=0,column=2)
                label=Label(window14,text="AVAILABLE",width="20",bg='black',fg='antique white',font=("a alloy ink",20,"italic"))
                label.grid(row=0,column=3)
                if n[0]>0:
                    for i in range(2,n[0]+2):
                        res=cur.fetchone()
                        for j in range(0,4):
                            label=Label(window14,text=res[j],bg='black',fg='antique white',width="25",font=("bradley hand itc",15,"italic","bold"))
                            label.grid(row=i,column=j)
            else:
                messagebox.showinfo("INFORMATION","NO RECORD FOUND")
            
        def hit15():       #SEARCHING RECORDS
            window15=Tk()
            window15.geometry("300x200")
            window15.configure(bg='black')
            window15.title("SEARCHING OF RECORDS...")
            sear=Entry(window15)
            sear.grid(row=4,column=0,pady=5,padx=20)
            def searching():
                if len(sear.get())!=0:
                    cur.execute('select count(*) from book_info where bookid like "%{}%" or book_name like "%{}%" or author_name like "%{}%" or availability like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get()))
                    n=cur.fetchone()
                    if n[0]>0:
                        cur.execute('select * from book_info where bookid like "%{}%" or book_name like "%{}%" or author_name like "%{}%" or availability like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get()))
                        window16=Tk()
                        window16.configure(bg='black')
                        window16.geometry("1340x730")
                        window16.title("DISPLAYING SEARCHED RECORDS...")
                        label=Label(window16,text="BOOK ID",bg='black',fg='antique white',width="15",font=("a alloy ink",20,"italic"))
                        label.grid(row=0,column=0)
                        label=Label(window16,text="BOOK NAME",bg='black',fg='antique white',width="20",font=("a alloy ink",20,"italic"))
                        label.grid(row=0,column=1)
                        label=Label(window16,text="AUTHOR NAME",bg='black',fg='antique white',width="20",font=("a alloy ink",20,"italic"))
                        label.grid(row=0,column=2)
                        label=Label(window16,text="AVAILABLE",width="20",bg='black',fg='antique white',font=("a alloy ink",20,"italic"))
                        label.grid(row=0,column=3)
                        if n[0]>0:
                            for i in range(2,n[0]+2):
                                res=cur.fetchone()
                                for j in range(0,4):
                                   label=Label(window16,text=res[j],bg='black',fg='antique white',width="25",font=("bradley hand itc",15,"italic","bold"))
                                   label.grid(row=i,column=j)
                            window15.destroy()
                    else:
                        messagebox.showinfo("INFORMATION","NO SUCH RECORD EXISTS!  -_-")
                else:
                    messagebox.showwarning("Warning","Please write something to search!")
            Button(window15,text="SEARCH",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=searching).grid(row=6,column=0,pady=5,padx=20)
                
        def hit16():
            window1.destroy()
        #book information system(main window)
        window1=Toplevel()
        window1.geometry("1400x800")
        window1.attributes("-fullscreen", True)
        window.bind("<Escape>", lambda event: window1.attributes("-fullscreen", False))
        window1.configure(bg='black')
        window1.title("BOOK INFORMATION SYSTEM")
        label1=Label(window1,text="BOOK INFORMATION SYSTEM",relief="solid",width="27",font=("chopsic",30,"bold"),bg='black',fg='antique white')
        label1.pack(pady=5)
        label1=Label(window1,text="ARMY PUBLIC SCHOOL",bg='black',fg='antique white',width="35",font=("cabin sketch",38,"underline","bold"))
        label1.pack(pady=5)
        label2=Label(window1,text="Welcome to book information system!!!",bg='black',fg='antique white',width="40",font=("CookieMonster",23,"italic"))
        label2.pack(pady=5)
        label=Label(window1,text="KNOWLEDGE IS THE WEAPON OF HUMAN MANKIND. ",width="50",bg='black',fg='antique white',font=("bradley hand itc",16,"bold")).pack(pady=5)
        global bms
        global image3
        bms=Image.open('Image\\books.PNG')
        image3=bms.resize((650,500),Image.ANTIALIAS)
        bms=ImageTk.PhotoImage(image3)
        picture2=Label(window1,image=bms,relief="solid")
        picture2.pack(padx=80,pady=30,side='left',anchor='nw')
        global slogo
        global image10,addbook,deletebook,displaybook,searchbook,updatebook,back,close
        slogo=Image.open('Image\\logo.PNG')
        image10=slogo.resize((180,180),Image.ANTIALIAS)
        slogo=ImageTk.PhotoImage(image10)
        picture1=Label(window1,image=slogo,relief="solid")
        picture1.place(x=80,y=20)
        addbook=PhotoImage(file="Image\\add book.png")
        addbook=addbook.zoom(6)
        addbook=addbook.subsample(12)
        deletebook=PhotoImage(file="Image\\delete book.png")
        deletebook=deletebook.zoom(7)
        deletebook=deletebook.subsample(12)
        displaybook=PhotoImage(file="Image\\display book.png")
        displaybook=displaybook.zoom(7)
        displaybook=displaybook.subsample(52)
        searchbook=PhotoImage(file="Image\\search book.png")
        searchbook=searchbook.zoom(6)
        searchbook=searchbook.subsample(12)
        updatebook=PhotoImage(file="Image\\upd.png")
        updatebook=updatebook.zoom(6)
        updatebook=updatebook.subsample(20)
        back=PhotoImage(file="Image\\back.png")
        back=back.zoom(8)
        back=back.subsample(21)
        close=PhotoImage(file="Image\\close.png")
        close=close.zoom(14)
        close=close.subsample(52)
        btn1=Button(window1,text="ADD NEW BOOK",image=addbook,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit11)
        btn1.place(x=850,y=250)
        btn1=Button(window1,text="UPDATE A BOOK",bg='black',activebackground="black",fg='antique white',image=updatebook,compound="top",bd=0,font=("times new roman",16,"italic","bold"),command=hit12)
        btn1.place(x=1150,y=250)                        
        btn1=Button(window1,text="DELETE A BOOK",image=deletebook,compound="top",bg='black',activebackground="black",bd=0,fg='antique white',font=("times new roman",16,"italic","bold"),command=hit13)                           #hit13
        btn1.place(x=840,y=380)
        btn1=Button(window1,text="DISPLAY BOOKS",image=displaybook,compound="top",bg='black',activebackground="black",bd=0,fg='antique white',font=("times new roman",16,"italic","bold"),command=hit14)                           #hit13
        btn1.place(x=1150,y=385)
        btn1=Button(window1,text="SEARCH",bg='black',fg='antique white',compound="top",activebackground="black",bd=0,image=searchbook,font=("times new roman",16,"italic","bold"),command=hit15)
        btn1.place(x=1200,y=525)
        btn1=Button(window1,text="BACK",bd=0,bg='black',image=back,fg='antique white',activebackground="black",compound="top",font=("times new roman",16,"italic","bold"),command=hit16)                                             #hit16
        btn1.place(x=890,y=520)
        btn1=Button(window1,text="CLOSE",bd=0,bg='black',image=close,fg='antique white',activebackground="black",compound="top",font=("times new roman",16,"italic","bold"),command=exitt)                                             #hit16
        btn1.place(x=1050,y=625)
#==========================================================================================================
    #ISSUE BOOK SYSTEM(main window)    
    def hit2():
        window2=Toplevel()
        cur.execute("create table if not exists student_issued(adm_no int(10) not null,student_name varchar(50) not null,class varchar(4) not null,section varchar(4) not null,bookid int(10) not null,doi date not null,status varchar(20))")
        window2.geometry("1400x800")
        window2.attributes("-fullscreen", True)
        window2.bind("<Escape>", lambda event: window2.attributes("-fullscreen", False))
        window2.configure(bg='black')
        window2.title("ISSUE BOOK SYSTEM")
        label1=Label(window2,text="ISSUE BOOK SYSTEM",bg='black',fg='antique white1',relief="solid",width="20",font=("chopsic",30,"bold"))
        label1.pack(pady=5)
        label1=Label(window2,text="ARMY PUBLIC SCHOOL",bg='black',fg='antique white1',width="35",font=("cabin sketch",38,"underline","bold"))
        label1.pack(pady=5)
        label1=Label(window2,text="Welcome to issue book system!!!",bg='black',fg='antique white1',width="35",font=("CookieMonster",23,"italic"))
        label1.pack(pady=5)
        label=Label(window2,text="IF YOU DON'T SACRIFICE FOR YOUR DREAMS THEN YOUR DREAM WILL BECOME YOUR SACRIFICE.",width="85",fg='antique white',bg='black',font=("bradley hand itc",16,"bold"))
        label.pack(pady=5)
        global slogo
        slogo=Image.open('Image\\logo.PNG')
        image10=slogo.resize((150,150),Image.ANTIALIAS)
        slogo=ImageTk.PhotoImage(image10)
        picture5=Label(window2,image=slogo,relief="solid")
        picture5.place(x=80,y=20)
        global bms
        global image3
        bms=Image.open('Image\\dark book.PNG')
        image3=bms.resize((800,550),Image.ANTIALIAS)
        bms=ImageTk.PhotoImage(image3)
        picture2=Label(window2,image=bms,relief="solid")
        picture2.pack(padx=80,pady=30,side='left',anchor='nw')

        def hit21():                                        #ISSUE BOOK
            window21=Toplevel()
            window21.geometry("1400x800")
            window21.attributes("-fullscreen", True)
            window21.bind("<F11>", lambda event: window21.attributes("-fullscreen",
                                                not window21.attributes("-fullscreen")))
            window21.bind("<Escape>", lambda event: window21.attributes("-fullscreen", False))
            window21.configure(bg='black')
            window21.title("STUDENTS WHO ISSUED BOOKS")
            label1=Label(window21,text="STUDENT DETAILS",bg='black',fg='antique white1',relief="solid",width="16",font=("chopsic",30,"bold"))
            label1.pack(pady=10)
            label1=Label(window21,text="ARMY PUBLIC SCHOOL",bg='black',fg='antique white1',width="35",font=("cabin sketch",38,"underline","bold"))
            label1.pack(pady=10)
            global ims,image4,logoo,image50
            logoo=Image.open('Image\\logo.PNG')
            image50=logoo.resize((150,150),Image.ANTIALIAS)
            logoo=ImageTk.PhotoImage(image50)
            picture50=Label(window21,image=logoo,relief="solid")
            picture50.place(x=80,y=20)
            ims=Image.open('Image\\issue2.PNG')
            image4=ims.resize((800,550),Image.ANTIALIAS)
            ims=ImageTk.PhotoImage(image4)
            picture3=Label(window21,image=ims,relief="solid")
            picture3.pack(padx=80,pady=30,side='left',anchor='nw')
            def hit211():                               #Insertion of student details issuing books
                window211=Toplevel()
                window211.geometry("500x400")
                window211.configure(bg='black')
                window211.title("INSERTING INFORMATION OF STUDENTS...")
                label2=Label(window211,text="ENTER ADMISSION NO.  :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=1,column=1)
                adm=Entry(window211)
                adm.grid(row=1,column=2)
                label2=Label(window211,text="ENTER STUDENT NAME  :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=2,column=1)
                sn=Entry(window211)
                sn.grid(row=2,column=2)
                label2=Label(window211,text="ENTER CLASS  :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=3,column=1)
                clas=Entry(window211)
                clas.grid(row=3,column=2)
                label2=Label(window211,text="ENTER SECTION :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=4,column=1)
                S=Entry(window211)
                S.grid(row=4,column=2)
                label2=Label(window211,text="ENTER BOOKID :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=5,column=1)
                bi=Entry(window211)
                bi.grid(row=5,column=2)
                label2=Label(window211,text="ENTER DOI(YYYY/MM/DD) :",bg='black',fg='antique white1',width="25",font=("bradley hand itc",15,'bold')).grid(row=6,column=1)
                di=Entry(window211)
                di.grid(row=6,column=2)
                def insert():
                    if len(adm.get())>0 and len(sn.get()) and len(clas.get())>0 and len(S.get())>0 and len(bi.get())>0 and len(di.get())>0:
                        if len(di.get())==10 and di.get()[4]=='/' and di.get()[7]=='/' and int(di.get()[5:7])<=12 and int(di.get()[8:10])<=31:
                            cur.execute("select count(*) from book_info where bookid like '{}'".format(bi.get()))
                            chk=cur.fetchone()
                            if chk[0]>0:
                                cur.execute("select * from book_info where bookid={}".format(bi.get()))
                                h=cur.fetchone()
                                if h[3]>0:                    
                                    cur.execute("insert into student_issued(adm_no,student_name,class,section,bookid,doi,status) values({},'{}','{}','{}',{},'{}','{}')".format(adm.get(),sn.get(),clas.get(),S.get(),bi.get(),di.get(),"not returned"))
                                    cur.execute("update book_info set availability=availability-1 where bookid={}".format(bi.get()))
                                    mydb.commit()
                                    window211.destroy()
                                    messagebox.showinfo("INFORMATION","BOOK ISSUED SUCCESSFULLY")
                                else:
                                    messagebox.showwarning("INVALID ISSUING...","This book is not available right now!")
                            else:
                                messagebox.showwarning("INVALID ISSUING...","Library doesn't have any book with this BookID!")
                        else:
                            messagebox.showwarning("INVALID ISSUING...","Please enter valid date of issuing!")
                    else:
                        messagebox.showwarning("INVALID ISSUING...","All entries must be filled!")
                Button(window211,text="SUBMIT",width=7,bg='black',activebackground="black",fg='antique white1',height=1,font=("bradley hand itc",16,"italic","bold"),command=insert).grid(row=9,column=1,pady=10)
            def hit212():                         #deletion of record
                window212=Tk()
                window212.geometry("600x300")
                window212.configure(bg='black')
                window212.title("DELETION OF RECORD...")
                label=Label(window212,text="DELETE RECORD HAVING:",bg='black',fg='antique white',width="25",font=("bradley hand itc",20,"italic","bold",'underline'))
                label.grid(row=1)
                label=Label(window212,text="ENTER ADMISSION NUMBER  :",bg='black',fg='antique white',width="25",font=("bradley hand itc",15,'bold'))
                label.grid(row=2,column=0)
                an=Entry(window212)
                an.grid(row=2,column=1)
                label=Label(window212,text="ENTER BOOK ID:",bg='black',fg='antique white',width="25",font=("bradley hand itc",15,'bold'))
                label.grid(row=3,column=0)
                bi=Entry(window212)
                bi.grid(row=3,column=1)
                label=Label(window212,text="ENTER DOI(YYYY/MM/DD)):",bg='black',fg='antique white',width="25",font=("bradley hand itc",15,'bold'))
                label.grid(row=4,column=0)
                d=Entry(window212)
                d.grid(row=4,column=1)
                def deleting():
                    if len(bi.get())>0 and len(an.get())>0 and len(d.get())>0:
                        cur.execute("select count(*) from student_issued where bookid={} and adm_no={} and doi='{}'".format(bi.get(),an.get(),d.get()))
                        x=cur.fetchone()
                        if x[0]>0:
                            cur.execute("delete from student_issued where bookid={} and adm_no={} and doi='{}'".format(bi.get(),an.get(),d.get()))
                            cur.execute("update book_info set availability=availability+1 where bookid={}".format(bi.get()))
                            mydb.commit()
                            window212.destroy()
                            messagebox.showinfo("INFORMATION","DELETED SUCCESSFULLY")
                        else:
                            messagebox.showinfo("INFORMATION","No record exists with such details!")
                    else:
                        messagebox.showwarning("WARNING","All entries must be filled!")
                Button(window212,text="DELETE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=deleting).grid(row=6,column=0,pady=10)
            def hit213():               #DISPLAYING RECORDS
                cur.execute("select count(*) from student_issued")
                n=cur.fetchone()
                if n[0]>0:
                    window213=Tk()
                    window213.geometry("1340x730")            
                    window213.configure(bg='black')
                    window213.title("DISPLAYING RECORDS...")
                    cur.execute("select* from student_issued")
                    label=Label(window213,text="ADMISSION NO.",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=0)
                    label=Label(window213,text="NAME",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=1)
                    label=Label(window213,text="CLASS",width="10",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=2)
                    label=Label(window213,text="SECTION",width="10",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=3)
                    label=Label(window213,text="BOOK ID",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=4)
                    label=Label(window213,text="DATE OF ISSUING",width="17",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                    label.grid(row=0,column=5)
                    for i in range(2,n[0]+2):
                        res=cur.fetchone()
                        for j in range(0,6):
                            label=Label(window213,text=res[j],bg='black',fg='antique white',width="15",font=("bradley hand itc",12,"italic",'bold'))
                            label.grid(row=i,column=j)
                else:
                    messagebox.showinfo("INFORMATION","No record is there in table!")
            def hit214():      #SEARCHING RECORDS       
                window214=Tk()
                window214.geometry("300x200")
                window214.configure(bg='black')
                window214.title("SEARCHING OF RECORDS...")
                sear=Entry(window214)
                sear.grid(row=4,column=0,pady=5,padx=20)
                def searching():
                    if len(sear.get())!=0:
                        cur.execute("select count(*) from student_issued")
                        v=cur.fetchone()
                        if v[0]>0:
                            cur.execute('select count(*) from student_issued where adm_no like "%{}%" or student_name like "%{}%" or class like "%{}%" or section like "%{}%" or bookid like "%{}%"or doi like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get(),sear.get(),sear.get()))
                            n=cur.fetchone()
                            if n[0]>0:
                                cur.execute('select * from student_issued where adm_no like "%{}%" or student_name like "%{}%" or class like "%{}%" or section like "%{}%" or bookid like "%{}%"or doi like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get(),sear.get(),sear.get()))
                                window2141=Tk()
                                window2141.configure(bg='black')
                                window2141.geometry("1340x730")
                                window2141.title("DISPLAYING SEARCHED RECORDS...")
                                label=Label(window2141,text="ADMISSION NO.",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=0)
                                label=Label(window2141,text="NAME",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=1)
                                label=Label(window2141,text="CLASS",width="10",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=2)
                                label=Label(window2141,text="SECTION",width="10",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=3)
                                label=Label(window2141,text="BOOK ID",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=4)
                                label=Label(window2141,text="DATE OF ISSUING",width="17",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                                label.grid(row=0,column=5)
                                if n[0]>0:
                                    for i in range(2,n[0]+2):
                                        res=cur.fetchone()
                                        for j in range(0,6):
                                           label=Label(window2141,text=res[j],bg='black',fg='antique white',width="15",font=("bradley hand itc",13,"italic","bold"))
                                           label.grid(row=i,column=j)
                                    window214.destroy()
                            else:
                                messagebox.showinfo("INFORMATION","NO SUCH RECORD EXISTS!")
                        else:
                            messagebox.showinfo("INFORMATION","Table is empty!!")
                    else:
                        messagebox.showwarning("Warning","Please write something to search!")
                Button(window214,text="SEARCH",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=searching).grid(row=6,column=0,pady=5,padx=20)           
                

            def hit215():
                window21.destroy()
            def hit216():
                exitt()
            btn1=Button(window21,text="INSERT",bg='black',activebackground="black",fg='antique white1',width=30,height=1,bd=10,font=("times new roman",16,"italic","bold"),command=hit211)                        
            btn1.pack(padx=20,pady=10)
            btn1=Button(window21,text="DELETE",bg='black',activebackground="black",fg='antique white1',width=30,height=1,bd=10,font=("times new roman",16,"italic","bold"),command=hit212)                         
            btn1.pack(padx=20,pady=10)
            btn1=Button(window21,text="DISPLAY STUDENTS",bg='black',activebackground="black",fg='antique white1',width=30,bd=10,height=1,font=("times new roman",16,"italic","bold"),command=hit213)                
            btn1.pack(padx=20,pady=10)
            btn1=Button(window21,text="SEARCH",bg='black',activebackground="black",fg='antique white1',width=30,height=1,bd=10,font=("times new roman",16,"italic","bold"),command=hit214)
            btn1.pack(padx=20,pady=10)
            btn1=Button(window21,text="BACK",bg='black',activebackground="black",fg='antique white1',width=30,height=1,bd=10,font=("times new roman",16,"italic","bold"),command=hit215)                                             
            btn1.pack(padx=20,pady=10)
            btn1=Button(window21,text="CLOSE",bg='black',activebackground="black",fg='antique white1',width=30,height=1,bd=10,font=("times new roman",16,"italic","bold"),command=hit216)                                             
            btn1.pack(padx=20,pady=10)
        def hit22():                                #FINE DETAILS
            window22s=Tk()
            window22s.geometry("450x200")
            window22s.title("FINE ENTRY...")
            window22s.configure(bg='black')
            f=Entry(window22s)
            Label(window22s,text="ENTER FINE TO BE CHARGED PER DAY:",width=35,bg='black',fg='antique white',font=("times new roman",16,"bold")).grid(row=1,column=0,padx=20,pady=20)
            f.grid(row=2,column=0,padx=20,pady=5)
            def fine_details():
                if len(f.get())>0:
                    cur.execute('select count(*) from student_issued where (datediff(curdate(),doi))>7 and status like "not returned"')
                    n=cur.fetchone()
                    if n[0]>0:
                        window22=Tk()
                        window22.geometry("1340x730")            
                        window22.configure(bg='black')
                        window22.title("FINE DETAILS...")
                        cur.execute('select adm_no,student_name,bookid,doi,(datediff(curdate(),doi)-7)*{} from student_issued where (datediff(curdate(),doi))>7 and status like "not returned"'.format(f.get()))
                        window22s.destroy()
                        label=Label(window22,text="ADMISSION NO.",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=0)
                        label=Label(window22,text="NAME",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=1)
                        label=Label(window22,text="BOOK ID",width="12",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=2)
                        label=Label(window22,text="DATE OF ISSUING",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=3)
                        label=Label(window22,text="FINE TILL NOW",width="20",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=4)
                        if n[0]>0:
                            for i in range(2,n[0]+2):
                                res=cur.fetchone()
                                for j in range(0,5):
                                    label=Label(window22,text=res[j],bg='black',fg='antique white',width="15",font=("bradley hand itc",15,"italic",'bold'))
                                    label.grid(row=i,column=j)
                        window22.mainloop()
                    else:
                        messagebox.showinfo("INFORMATION","NO FINE TO BE CHARGED ON ANY STUDENT.")
                else:
                    messagebox.showwarning("WARNING","Please enter fine to charged per day!")
            Button(window22s,text="SUBMIT",bg='black',activebackground="black",fg='antique white1',width=10,height=1,font=("times new roman",16,"italic","bold"),command=fine_details).grid(row=3,column=0,pady=15)
        def hit23():                        #FINE CALCULATOR
            window23=Tk()
            window23.geometry("760x300")
            window23.title("Fine Calculator...")
            window23.config(bg='black')
            def returnEntry():
                if len(date1.get())>0 and len(date2.get())>0 and len(fpd.get())>0:
                    if len(date1.get())==10 and date1.get()[4]=='/' and date1.get()[7]=='/' and int(date1.get()[5:7])<=12 and int(date1.get()[8:10])<=31:
                        if len(date2.get())==10 and date2.get()[4]=='/' and date2.get()[7]=='/' and int(date2.get()[5:7])<=12 and int(date2.get()[8:10])<=31:
                            cur.execute("select datediff('{}','{}')".format(date2.get(),date1.get()))
                            answer=cur.fetchone()[0]
                            fine_days=answer-7
                            fine=fine_days*int((fpd.get()))
                            if fine>0:
                                resultLabel.config(text=fine)
                            else:
                                fine="NO FINE"
                                resultLabel.config(text=fine)
                        else:
                            messagebox.showwarning("WARNING","Please enter proper Date of returning!")
                    else:
                        messagebox.showwarning("WARNING","Please enter  proper Date of issuing!")
                else:
                    messagebox.showwarning("WARNING","All entries must be filled!")
            label=Label(window23,text="ENTER DATE OF ISSUING (YYYY/MM/DD):",bg='black',fg='antique white1',width="45",font=("bradley hand itc",15,"bold")).grid(row=1,column=1)
            date1=Entry(window23)
            date1.grid(row=1,column=2,pady=10)
            label=Label(window23,text="ENTER DATE OF RETURNING (YYYY/MM/DD):",bg='black',fg='antique white1',width="45",font=("bradley hand itc",15,"bold")).grid(row=3,column=1)
            date2=Entry(window23)
            date2.grid(row=3,column=2,pady=10)
            label=Label(window23,text="FINE PER DAY:",bg='black',fg='antique white1',width="45",font=("bradley hand itc",15,"bold")).grid(row=5,column=1)
            fpd=Entry(window23)
            fpd.grid(row=5,column=2,pady=10)
            label=Label(window23,text="FINE/PENALTY:",bg='black',fg='antique white1',width="45",font=("bradley hand itc",15,"bold")).grid(row=7,column=1)
            resultLabel=Label(window23,text="",width=20)
            resultLabel.grid(row=7,column=2,pady=5)
            enterEntry=Button(window23,text="Calculate",width=12,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"bold"),command=returnEntry)
            enterEntry.grid(row=9,column=1,pady=20)
        def hit24():
            window2.destroy()
             
        global stud,fine,back2,close2,calc
        back2=PhotoImage(file="Image\\back.png")
        back2=back2.zoom(8)
        back2=back2.subsample(21)
        stud=PhotoImage(file="Image\\ib.png")
        stud=stud.zoom(8)
        stud=stud.subsample(21)
        fine=PhotoImage(file="Image\\fine.png")
        fine=fine.zoom(14)
        fine=fine.subsample(21)
        calc=PhotoImage(file="Image\\fc.png")
        calc=calc.zoom(10)
        calc=calc.subsample(21)
        close2=PhotoImage(file="Image\\close.png")
        close2=close2.zoom(6)
        close2=close2.subsample(21)
        btn1=Button(window2,text="ISSUE BOOKS",image=stud,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit21)
        btn1.place(x=950,y=260)
        btn1=Button(window2,text="FINE DETAILS",image=fine,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit22)
        btn1.place(x=1175,y=235)
        btn1=Button(window2,text="FINE CALCULATOR",image=calc,compound="top",bg='black',activebackground="black",fg='antique white1',bd=0,font=("times new roman",16,"italic","bold"),command=hit23)   
        btn1.place(x=920,y=410)
        btn1=Button(window2,text="BACK",image=back2,compound="top",bg='black',activebackground="black",fg='antique white1',bd=0,font=("times new roman",16,"italic","bold"),command=hit24)
        btn1.place(x=1215,y=450)
        btn1=Button(window2,text="CLOSE",image=close1,bd=0,compound="top",bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=exitt)
        btn1.place(x=1090,y=625)
#======================================================================================================
    #RETURNING BOOK SYSTEM(main window)
    def hit3():
        cur.execute("create table if not exists student_return(adm_no int(10) not null,student_name varchar(50) not null,class varchar(4) not null,section varchar(4) not null,bookid int(10) not null,dor date not null)")
        window3=Toplevel()
        window3.geometry("900x600")
        window3.configure(bg='black')
        window3.attributes("-fullscreen", True)
        window3.bind("<F11>", lambda event: window3.attributes("-fullscreen",
                                            not window3.attributes("-fullscreen")))
        window3.bind("<Escape>", lambda event: window3.attributes("-fullscreen", False))
        window3.title("RETURNING BOOK SYSTEM")
        label1=Label(window3,text="RETURNING BOOK SYSTEM",relief="solid",bg='black',fg='antiquewhite1',width="25",font=("chopsic",30,"bold"))
        label1.pack(pady=10)
        label1=Label(window3,text="ARMY PUBLIC SCHOOL",bg='black',fg='antiquewhite1',width="35",font=("cabin sketch",38,"underline"))
        label1.pack(pady=10)
        label1=Label(window3,text="Welcome to returning book system!!!",bg='black',fg='antiquewhite1',width="35",font=("CookieMonster",30,"italic"))
        label1.pack(pady=10)
        global rms,image5,sclogo,image9
        sclogo=Image.open('Image\\logo.PNG')
        image9=sclogo.resize((180,180),Image.ANTIALIAS)
        sclogo=ImageTk.PhotoImage(image9)
        picture1=Label(window3,image=sclogo,relief="solid")
        picture1.place(x=80,y=20)
        rms=Image.open('Image\\light book.PNG')
        image5=rms.resize((700,550),Image.ANTIALIAS)
        rms=ImageTk.PhotoImage(image5)
        picture4=Label(window3,image=rms,bd=0)
        picture4.pack(padx=80,pady=30,side='left',anchor='nw')
        def hit311():                               #Insertion of student details issuing books
            window311=Tk()
            window311.geometry("650x400")
            window311.configure(bg='black')
            window311.title("INSERTING INFORMATION OF STUDENTS...")
            label2=Label(window311,text="ENTER ADMISSION NO.  :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=1,column=1)
            adm=Entry(window311)
            adm.grid(row=1,column=2)
            label2=Label(window311,text="ENTER STUDENT NAME  :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=2,column=1)
            sn=Entry(window311)
            sn.grid(row=2,column=2)
            label2=Label(window311,text="ENTER CLASS  :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=3,column=1)
            clas=Entry(window311)
            clas.grid(row=3,column=2)
            label2=Label(window311,text="ENTER SECTION :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=4,column=1)
            S=Entry(window311)
            S.grid(row=4,column=2)
            label2=Label(window311,text="ENTER BOOKID :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=5,column=1)
            bi=Entry(window311)
            bi.grid(row=5,column=2)
            label2=Label(window311,text="ENTER DOR(YYYY/MM/DD) :",bg='black',fg='antique white1',width="35",font=("bradley hand itc",15)).grid(row=6,column=1)
            di=Entry(window311)
            di.grid(row=6,column=2)
            def insert():
                if len(adm.get())>0 and len(sn.get())>0 and len(clas.get())>0 and len(S.get())>0 and len(bi.get())>0 and len(di.get())>0:
                    if len(di.get())==10 and di.get()[4]=='/' and di.get()[7]=='/' and int(di.get()[5:7])<=12 and int(di.get()[8:10])<=31:
                        cur.execute("insert into student_return(adm_no,student_name,class,section,bookid,dor) values({},'{}','{}','{}',{},'{}')".format(adm.get(),sn.get(),clas.get(),S.get(),bi.get(),di.get()))
                        cur.execute('update student_issued set status="returned" where adm_no like {} and student_name like "{}" and bookid like "{}"'.format(adm.get(),sn.get(),bi.get()))
                        cur.execute("update book_info set availability=availability+1 where bookid={}".format(bi.get()))
                        mydb.commit()
                        window311.destroy()
                        messagebox.showinfo("INFORMATION","RECORD INSERTED SUCCESSFULLY")
                    else:
                        messagebox.showwarning("WARNING","Please enter Date of Returning in proper format!")
                else:
                    messagebox.showwarning("WARNING","All entries must be filled")
            Button(window311,text="SUBMIT",width=7,bg='black',activebackground="black",fg='antique white1',height=1,font=("bradley hand itc",16,"italic","bold"),command=insert).grid(row=9,column=1,pady=10)
        def hit312():                         #deletion of record
            window312=Tk()
            window312.geometry("600x300")
            window312.configure(bg='black')
            window312.title("DELETION OF RECORD...")
            label=Label(window312,text="DELETE RECORD HAVING:",bg='black',fg='antique white',width="25",font=("bradley hand itc",20,"italic","bold","underline"))
            label.grid(row=1)
            label=Label(window312,text="ENTER ADMISSION NUMBER  :",bg='black',fg='antique white',width="25",font=("bradley hand itc",15))
            label.grid(row=2,column=0)
            an=Entry(window312)
            an.grid(row=2,column=1)
            label=Label(window312,text="ENTER BOOK ID:",bg='black',fg='antique white',width="25",font=("bradley hand itc",15))
            label.grid(row=3,column=0)
            bi=Entry(window312)
            bi.grid(row=3,column=1)
            label=Label(window312,text="ENTER DOR(YYYY/MM/DD)):",bg='black',fg='antique white',width="25",font=("bradley hand itc",15))
            label.grid(row=4,column=0)
            d=Entry(window312)
            d.grid(row=4,column=1)
            def deleting():
                if len(an.get())>0 and len(bi.get())>0 and len(d.get())>0:
                    if len(d.get())==10 and d.get()[4]=='/' and d.get()[7]=='/' and int(d.get()[5:7])<=12 and int(d.get()[8:10])<=31:                
                        cur.execute("delete from student_return where bookid={} and adm_no={} and dor='{}'".format(bi.get(),an.get(),d.get()))
                        cur.execute("update book_info set availability=availability-1 where bookid like '{}'".format(bi.get()))
                        mydb.commit()
                        window312.destroy()
                        messagebox.showinfo("INFORMATION","DELETED SUCCESSFULLY")
                    else:
                        messagebox.showwarning("WARNING","Please enter Date of Returning in proper format!")
                else:
                    messagebox.showwarning("WARNING","All entries must be filled")
            Button(window312,text="DELETE",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=deleting).grid(row=7,column=0,pady=10)
        def hit313():                       #DISPLAYING OF RECORDS
            cur.execute("select count(*) from student_return")
            n=cur.fetchone()
            if n[0]>0:
                window313=Tk()
                window313.geometry("1340x730")            
                window313.configure(bg='black')
                window313.title("DISPLAYING RECORDS...")
                cur.execute("select* from student_return")
                label=Label(window313,text="ADMISSION NO.",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=0)
                label=Label(window313,text="NAME",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=1)
                label=Label(window313,text="CLASS",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=2)
                label=Label(window313,text="SECTION",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=3)
                label=Label(window313,text="BOOK ID",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=4)
                label=Label(window313,text="DATE OF RETURNING",width="18",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                label.grid(row=0,column=5)
                for i in range(2,n[0]+2):
                    res=cur.fetchone()
                    for j in range(0,6):
                        label=Label(window313,text=res[j],bg='black',fg='antique white',width="15",font=("bradley hand itc",15,"italic","bold"))
                        label.grid(row=i,column=j)
            else:
                messagebox.showinfo("INFORMATION","Table is empty, no record is there!")
        def hit314():      #SEARCHING RECORDS       
            window314=Tk()
            window314.geometry("300x200")
            window314.configure(bg='black')
            window314.title("SEARCHING OF RECORDS...")
            sear=Entry(window314)
            sear.grid(row=4,column=0,pady=5,padx=20)
            def searching():
                if len(sear.get())>0:
                    cur.execute('select count(*) from student_return where adm_no like "%{}%" or student_name like "%{}%" or class like "%{}%" or section like "%{}%" or bookid like "%{}%"or dor like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get(),sear.get(),sear.get()))
                    n=cur.fetchone()
                    if n[0]>0:
                        cur.execute('select * from student_return where adm_no like "%{}%" or student_name like "%{}%" or class like "%{}%" or section like "%{}%" or bookid like "%{}%"or dor like "%{}%"'.format(sear.get(),sear.get(),sear.get(),sear.get(),sear.get(),sear.get()))
                        window3141=Tk()
                        window3141.configure(bg='black')
                        window3141.geometry("1340x730")
                        window3141.title("DISPLAYING SEARCHED RECORDS...")
                        label=Label(window3141,text="ADMISSION NO.",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=0)
                        label=Label(window3141,text="NAME",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=1)
                        label=Label(window3141,text="CLASS",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=2)
                        label=Label(window3141,text="SECTION",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=3)
                        label=Label(window3141,text="BOOK ID",width="15",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=4)
                        label=Label(window3141,text="DATE OF RETURNING",width="18",bg='black',fg='antique white',font=("algerian",16,"italic","bold"))
                        label.grid(row=0,column=5)
                        if n[0]>0:
                            for i in range(2,n[0]+2):
                                res=cur.fetchone()
                                for j in range(0,6):
                                   label=Label(window3141,text=res[j],bg='black',fg='antique white',width="15",font=("bradley hand itc",15,"italic","bold"))
                                   label.grid(row=i,column=j)
                            window314.destroy()
                    else:
                        messagebox.showinfo("INFORMATION","NO SUCH RECORD EXISTS  -_-")
                else:
                    messagebox.showwarning("WARNING","Please write something to search!")
            Button(window314,text="SEARCH",bg='black',activebackground="black",fg='antique white',width=7,height=1,font=("bradley hand itc",16,"italic","bold"),command=searching).grid(row=6,column=0,pady=5,padx=20)
        def hit315():
            window3.destroy()
        def hit316():
            exitt()
        global ins,dele,dis,sear2,back3,close3
        dis=PhotoImage(file="Image\\display.png")
        dis=dis.zoom(10)
        dis=dis.subsample(21)
        sear2=PhotoImage(file="Image\\search.png")
        sear2=sear2.zoom(10)
        sear2=sear2.subsample(21)
        dele=PhotoImage(file="Image\\bin.png")
        dele=dele.zoom(10)
        dele=dele.subsample(21)
        ins=PhotoImage(file="Image\\Return_insert.png")
        ins=ins.zoom(10)
        ins=ins.subsample(21)
        back3=PhotoImage(file="Image\\back.png")
        back3=back3.zoom(8)
        back3=back3.subsample(21)
        close3=PhotoImage(file="Image\\close.png")
        close3=close3.zoom(8)
        close3=close3.subsample(21)
        btn1=Button(window3,text="INSERT",image=ins,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit311)                        
        btn1.place(x=900,y=245)
        btn1=Button(window3,text="DELETE",image=dele,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit312)                         
        btn1.place(x=1150,y=245)
        btn1=Button(window3,text="DISPLAY  STUDENTS",image=dis,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit313)                
        btn1.place(x=840,y=400)
        btn1=Button(window3,text="SEARCH",image=sear2,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit314)
        btn1.place(x=1150,y=400)
        btn1=Button(window3,text="BACK",image=back3,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit315)                                             
        btn1.place(x=905,y=575)
        btn1=Button(window3,text="CLOSE",image=close3,compound="top",bd=0,bg='black',activebackground="black",fg='antique white1',font=("times new roman",16,"italic","bold"),command=hit316)                                             
        btn1.place(x=1165,y=575)
    #library management system(buttons)
    global bmsimag,ibms,rbs,close1
    bmsimag=PhotoImage(file="Image\\bms icon.png")
    bmsimag=bmsimag.zoom(8)
    bmsimag=bmsimag.subsample(51)
    ibms=PhotoImage(file="Image\\ims.png")
    ibms=ibms.zoom(10)
    ibms=ibms.subsample(24)
    rbs=PhotoImage(file="Image\\return book.png")
    rbs=rbs.zoom(8)
    rbs=rbs.subsample(12)
    close1=PhotoImage(file="Image\\close.png")
    close1=close1.zoom(6)
    close1=close1.subsample(21)
    btn1=Button(window,text=" MANAGE BOOKS",image=bmsimag,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit1)
    btn1.place(x=860,y=260)
    btn1=Button(window,text="ISSUE BOOK",image=ibms,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit2)
    btn1.place(x=1150,y=245)
    btn1=Button(window,text="RETURN BOOK",image=rbs,compound="top",bg='black',activebackground="black",fg='antique white',bd=0,font=("times new roman",16,"italic","bold"),command=hit3)
    btn1.place(x=875,y=400)
    btn1=Button(window,text="CLOSE",image=close1,compound="top",bd=0,bg='black',activebackground="black",fg='antique white',font=("times new roman",16,"italic","bold"),command=exitt)
    btn1.place(x=1175,y=425)
    label=Label(window,text="-:CREATED BY:-",width="15",bg='black',fg='antique white',font=("paint drops",20)).place(x=980,y=575)
    label=Label(window,text="YATHARTH SARASWAT",width="20",bg='black',fg='antique white',font=("paint drops",30)).place(x=875,y=610)
    label=Label(window,text="Thanks for using this software.",bg='black',fg='antique white',width="45",font=("cabin sketch",15,"bold")).place(x=850,y=690)
    window.deiconify()
if z!=1:
    ini=Tk()
    ini.geometry("300x200")
    ini.title("ENTER PASSWORD ●●●●●...")
    ini.configure(bg='black')
    pas=Entry(ini,show="●")
    Label(ini,text="ENTER PASSWORD:",width=20,bg='black',fg='antique white',font=("times new roman",16,"italic","bold")).grid(row=2,column=0,padx=20,pady=20)
    pas.grid(row=4,column=0,padx=20,pady=5)
    def correct():
        passing=pas.get()
        if passing==app_password:
            passw()
            ini.iconify()
        else:
            messagebox.showerror("INCORRECT PASSWORD","PLEASE ENTER CORRECT PASSWORD!")
            exit()
    btn1=Button(ini,text="SUBMIT",width=7,height=1,bg='black',fg='antique white',font=("times new roman",16,"italic","bold"),command=correct)
    btn1.grid(padx=20,pady=10)
else:
    ini=Tk()
    ini.geometry("300x200")
    ini.title("ENTER PASSWORD ●●●●●...")
    ini.configure(bg='black')
    pas=Entry(ini,show="●")
    Label(ini,text="ENTER PASSWORD:",width=20,bg='black',fg='antique white',font=("times new roman",16,"italic","bold")).grid(row=2,column=0,padx=20,pady=20)
    pas.grid(row=4,column=0,padx=20,pady=5)
    def correct():
        passing=pas.get()
        if passing==app_password:
            passw()
            ini.iconify()
        else:
            messagebox.showerror("INCORRECT PASSWORD","PLEASE ENTER CORRECT PASSWORD!")
            exit()
    btn1=Button(ini,text="SUBMIT",width=7,height=1,bg='black',activebackground="black",fg='antique white',font=("times new roman",16,"italic","bold"),command=correct)
    btn1.grid(padx=20,pady=10)
    ini.attributes('-topmost', 1)

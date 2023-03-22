from tkinter import*
from tkinter import ttk

import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1070+0+0")
        
        # ==============================Variable===============
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysofbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
        
        
        lbltitle=Label(self.root,text="Library Management System", bg="powder blue", fg="green",bd=20,relief=RIDGE,font=("times new roman", 50, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)   
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1920,height=400)
        
        # =======================================DataFrameLeft========================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="green",bd=12,relief=RIDGE,font=("times new roman", 13, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMember = Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No = Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)
        
        lblTitle = Label(DataFrameLeft,font=("arial",12,"bold"),text="Title",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName = Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName = Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code: ",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Moblie",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)
              
        
        lblAuthor_Name=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name",padx=2,pady=6,bg="powder blue")
        lblAuthor_Name.grid(row=2,column=2,sticky=W)
        txtAuthor_Name=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=29)
        txtAuthor_Name.grid(row=2,column=3)
        
        lblDate_Borrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed",padx=2,pady=6,bg="powder blue")
        lblDate_Borrowed.grid(row=3,column=2,sticky=W)
        txtDate_Borrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDate_Borrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDays_On_Book=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDays_On_Book.grid(row=5,column=2,sticky=W)
        txtDays_On_Book=Entry(DataFrameLeft,textvariable=self.daysofbook_var,font=("arial",13,"bold"),width=29)
        txtDays_On_Book.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDate_Over_Due=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due",padx=2,pady=6,bg="powder blue")
        lblDate_Over_Due.grid(row=7,column=2,sticky=W)
        txtDate_Over_Due=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDate_Over_Due.grid(row=7,column=3)
        
        lblActual_Price=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price",padx=2,pady=6,bg="powder blue")
        lblActual_Price.grid(row=8,column=2,sticky=W)
        txtActual_Price=Entry(DataFrameLeft,textvariable=self.finalprice,font=("arial",13,"bold"),width=29)
        txtActual_Price.grid(row=8,column=3)
        
        
        DataFrameRight=LabelFrame(frame,text="Book Details", bg="powder blue", fg="green",bd=12,relief=RIDGE,font=("times new roman", 13, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman", 13, "bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook',
                 'Into to Machine Lear','Machine tecno','My Python','Joss Ellif guru','Elite Jungle Python','Jungli Python',
                 'Machine Python','Advance Python','Inton Python','RedChilli Python','Ishq Python']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysofbook_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs. 780")
                
        '''
        elif
        elif
        elif
        elif
        for more books and add details for it.
        '''
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        # ========================================Button Frame============================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1920,height=70)
        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnShowData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)
        
        btnUpdateData=Button(Framebutton,text="Update Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdateData.grid(row=0,column=2)
        
        btnDeleteData=Button(Framebutton,text="Delete Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnDeleteData.grid(row=0,column=3)
        
        btnResetData=Button(Framebutton,text="Reset Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnResetData.grid(row=0,column=4)
        
        btnExitData=Button(Framebutton,text="Exit Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnExitData.grid(row=0,column=5)
        
        # =========================================Information Frame=================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1920,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname",
                                                            "address1","address2","postid","mobile","bookid","booktitle",
                                                            "author","dateborrowed","datedue","days","latereturnfine",
                                                            "dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book Title")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysofbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finalprice.get(),
                                                                                                                self.booktitle_var.get()
                                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member Has been inserted successfully")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysofbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])
        
        
        
             
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
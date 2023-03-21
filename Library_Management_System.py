from tkinter import*
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")
        
        lbltitle=Label(self.root,text="Library Management System", bg="powder blue", fg="green",bd=20,relief=RIDGE,font=("times new roman", 50, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)   
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1920,height=400)
        
        # =======================================DataFrameLeft========================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="green",bd=12,relief=RIDGE,font=("times new roman", 13, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMember = Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No = Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)
        
        lblTitle = Label(DataFrameLeft,font=("arial",12,"bold"),text="Title",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName = Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName = Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code: ",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Moblie",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)
        
        lblAuthor_Name=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name",padx=2,pady=6,bg="powder blue")
        lblAuthor_Name.grid(row=1,column=2,sticky=W)
        txtAuthor_Name=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAuthor_Name.grid(row=1,column=3)
        
        lblDate_Borrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lblDate_Borrowed.grid(row=5,column=0,sticky=W)
        txtDate_Borrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtDate_Borrowed.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        lbl=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,pady=6,bg="powder blue")
        lbl.grid(row=5,column=0,sticky=W)
        txt=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txt.grid(row=5,column=1)
        
        

        
        
        
        
        DataFrameLeft=LabelFrame(frame,text="Book Details", bg="powder blue", fg="green",bd=12,relief=RIDGE,font=("times new roman", 13, "bold"))
        DataFrameLeft.place(x=910,y=5,width=540,height=350)
        
        # ========================================Button Frame============================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1920,height=70)
        
        # =========================================Information Frame=================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1920,height=195)
        
        
        
             
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
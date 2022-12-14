import mysql.connector
con = mysql.connector.connect(host = 'localhost' , user = 'root' , password = 'groot' , database = 'classmanagement')
cur = con.cursor()


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from tkinter import Text,Tk
import datetime
global time
now = datetime.datetime.now()
time=now.strftime("%Y-%m-%d %H:%M:%S")
global NEWPASSWORD
global NEWUSERNAME
NEWPASSWORD="1"#DELETE IT  AFTER CONNECTION
NEWUSERNAME="1"#DELETE IT AFTER CONNECTION
global NAME

#t=tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ", "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
#t.destroy()
def enquiryadmin():
    def h():
        w10.destroy()
        enquiry1.destroy()

    def r():
        global w10
        w10=Tk()
        w10.geometry("170x70")
        w10.configure(background = "lightblue")
        w10.title("Enquiry")
        l10=Label(w10,text="Enquiry has been recorded!!!")
        l10.place(x=10,y=10)
        b0=Button(w10,text="OK",command=h)
        b0.place(x=55,y=40)
        NAME2=entry23.get()
        PhoneNo=(entry24.get())
        Purpose2=purpose.get()
        w10.mainloop()
    def enquiry1destroy():
        enquiry1.destroy()

                   
    global enquiry1
    enquiry1=Tk()
    enquiry1.title("ENQUIRY")
    enquiry1.geometry("700x450")
    enquiry1.configure(bg="lightblue")
    global purpose
    purpose=StringVar()
    global entry23
    global entry24
    global box2
    global PhoneNo
    
    label22 = Label(enquiry1, text="ENQUIRY", font=("arial", 25), bg="violetred1")
    label22.pack(side=TOP, fill=X)
    label1 = Label(enquiry1, text="NAME:", font=("arial", 17))
    label1.place(x=100, y=150)
    label2 = Label(enquiry1, text="PHONE NO.:", font=("arial", 17))
    label2.place(x=100, y=210)
    label3 = Label(enquiry1, text="PURPOSE:", font=("arial", 17))
    label3.place(x=100, y=270)
    entry23 = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    entry23.place(x=300, y=150)
    button = Button(enquiry1, text="Submit", width=30, bg="violetred1", command=r)
    button.place(x=300, y=320)
    button1=Button(enquiry1, text="<< BACK", width=30, bg="violetred1",command=enquiry1destroy)
    button1.place(x=0,y=0)
    entry24 = Entry(enquiry1, bd=5, width=20, font=("arial", 15),text="Select")
    entry24.place(x=300, y=210)
    entry24 = tkinter.IntVar()
    box2 = ttk.Combobox(enquiry1, textvariable=purpose, state="readonly", font=("arial", 12, "bold"), width=25)
    box2['values'] = ['FOR TAKING ADMISSION IN THE SCHOOL', 'FOR TAKING TRANSFER CERTIFICATE(TC)', 'ABOUT SCHOOL RELATED ISSUES','OTHERS']    
    box2.current(0)
    box2.place(x=300, y=270)
    sql = "Insert into enquiry values( %s , %s , %s ) "
    val = ( entry23.get(), entry24.get() , purpose.get() )
    cur.execute(sql,val)
    con.commit()


def viewenquiry():
     rt = Tk()
     rt.title("VISITORS")
     rt.geometry("610x500")
     mainlabel =Label(rt, text="VISITOR", font=("times new roman", 35), bg="MediumOrchid2")
     mainlabel.pack(side=TOP, fill=X)
     chat1 = ttk.Treeview(rt,height=20 , columns=('PHONE NO.','ENQUIRY','DATE,TIME'), selectmode="extended")
     chat1.heading('#0', text='NAME', anchor=CENTER)
     chat1.heading('#1', text='PHONE NO.', anchor=CENTER)
     chat1.heading('#2', text='ENQUIRY', anchor=CENTER)
     chat1.heading('#3', text="DATE,TIME", anchor=CENTER)
     chat1.column('#1', stretch=YES, minwidth=50, width=100)
     chat1.column('#3', stretch=YES, minwidth=50, width=100)
     chat1.column('#2', stretch=YES, minwidth=50, width=300)
     chat1.column('#0', stretch=YES, minwidth=50, width=70)
     vsb = ttk.Scrollbar(rt, orient="vertical", command=chat1.yview)
     vsb.place(x=0, y=0, height=475 + 20)
     chat1.configure(yscrollcommand=vsb.set)
     chat1.place(x=25, y=65)
     ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
     ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
     rt.configure(background="white")
    
#please add a prog to view the inquiries inputted and stored in the database	


def fees():
    def reset():
        rollno.configure(state="normal")
        fees.configure(state="normal")
        
        rollno.delete(0,END )
        fees.delete(0, END)
       
        
    def paid():
        pass
    def topay():
        pass
    def addfee():
        pass
    def distroyw():
          fee.destroy()
    def login():
        pass

    fee=Tk()
    fee.title("KVA")
    fee.geometry('250x650')
    fee.configure(background = "lightblue")
    button1 = Button(fee, text="BACK", width=30, bg="Blue", command=distroyw)
    button1.place(x=16, y=0)
    label1=Label(fee,text="ENTER ROLL NO.", font=("arial",17))
    label1.place(x=25, y=150)
    button2=Button(fee,text="LOGIN",width=30,font=("arial",10),bg="lightgreen",command=login )
    button2.place(x=0, y=250)
    button3=Button(fee,text="ADD FEE",width=30,font=("arial",10),bg="lightgreen",command=addfee )
    button3.place(x=0 , y=550)

    button2 = Button(fee, text="RESET", width=30, font=("arial", 10), bg="red", command=reset)
    button2.place(x=0,y=30)
    button4 = Button(fee, text="To Pay", width=10, font=("arial", 10), bg="red", command=topay)
    button4.place(x=160,y=580)
    button5 = Button(fee, text="Paid", width=10, font=("arial", 10), bg="red", command=paid)
    button5.place(x=0,y=580)




    label31=Label(fee,text="TOTEL FEE", font=("arial",17))
    label31.place(x=60, y=450)

    rollno=Entry(fee,bd=5, width=20 ,font=("arial",15))
    rollno.place(x=9,y=200)
    fees=Entry(fee,bd=5, width=20 ,font=("arial",15))
    fees.place(x=9,y=500)


def marks():
    NAME="Lelouch Vi Britannia"

    def showmarks():
        def h(root): 
            for i in range(total_rows): 
                for j in range(total_columns): 
                      
                    lbl= Entry(root, width=17, fg='blue', 
                                   font=('Arial',12,'bold')) 
                      
                    lbl.grid(row=i, column=j) 
                    lbl.insert(END, lsth[i][j])

    #Variable List of marks of the student who opened this program

        MARKSLIST=[100,100,100,100,100,100]   
        
        global lsth  
        lsth = [('Student Name','Maths','Chemistry','Physics','Computer-Science','English'),
                (NAME,MARKSLIST[0],MARKSLIST[1],MARKSLIST[2],MARKSLIST[3],MARKSLIST[4])] 
        total_rows = len(lsth) 
        total_columns = len(lsth[0]) 
        root = Tk()
        root.title("Student's Marks")
        root.configure(background = "pink")
        h(root) 
        root.mainloop()

        
    showmarks()
def viewfees():
    rt = Tk()
    rt.title("FEES")
    rt.geometry("610x500")
    mainlabel =Label(rt, text="FEES", font=("times new roman", 35), bg="MediumOrchid2")
    mainlabel.pack(side=TOP, fill=X)
    chat1 = ttk.Treeview(rt,height=20 , columns=('PHONE NO.','ENQUIRY','DATE,TIME'), selectmode="extended")
    chat1.heading('#0', text='Rollno', anchor=CENTER)
    chat1.heading('#1', text='Name', anchor=CENTER)
    chat1.heading('#2', text='Total fees', anchor=CENTER)
    chat1.heading('#3', text="Paid/Not Paid", anchor=CENTER)
    chat1.column('#1', stretch=YES, minwidth=50, width=100)
    chat1.column('#3', stretch=YES, minwidth=50, width=100)
    chat1.column('#2', stretch=YES, minwidth=50, width=300)
    chat1.column('#0', stretch=YES, minwidth=50, width=70)
    vsb = ttk.Scrollbar(rt, orient="vertical", command=chat1.yview)
    vsb.place(x=0, y=0, height=475 + 20)
    chat1.configure(yscrollcommand=vsb.set)
    chat1.place(x=25, y=65)
    ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
    ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
    rt.configure(background="white")
    sql = "select * from fees where RollNo=%s"

    #please add a prog to view the fees inputted and stored in the database	



def changepassword():
    def h():
        global NEWUSERNAME
        NEWUSERNAME=E101.get()
        c
        NEWPASSWORD=E102.get()
        w01.destroy()
        
    w01=Tk()
    w01.geometry("240x150")
    w01.configure(background = "lightblue")
    w01.title("CHANGE USERNAME & PASSWORD")
    l101=Label(w01,text="NEW USERNAME:-",bg="yellow")
    l101.place(x=30,y=30)
    E101=Entry(w01,width=10)
    E101.place(x=135,y=30)
    l102=Label(w01,text="NEW PASSWORD:-",bg="yellow")
    l102.place(x=30,y=60)
    E102=Entry(w01,width=10)
    E102.place(x=135,y=60)
    b01=Button(w01,text="OK",command=h)
    b01.place(x=95,y=90)
    w01.mainloop()

print(NEWUSERNAME,NEWPASSWORD)

def attendence():
    global i
    global I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,I18,I19,I20,I21,I22,I23,I24,I25,I26
    global I27,I28,I29,I30,I31,I32,I33,I34,I35,I36,I37,I38,I39,I40,I41,I42,I43,I44,I45,I46,I47,I48,I49,I50
    global L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30
    global L31,L32,L33,L34,L35,L36,L37,L38,L39,L40,L41,L42,L43,L44,L45,L46,L47,L48,L49,L50
    global R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26,R27,R28,R29,R30
    global R31,R32,R33,R34,R35,R36,R37,R38,R39,R40,R41,R42,R43,R44,R45,R46,R47,R48,R49,R50
    global rr1,rr2,rr3,rr4,rr5,rr6,rr7,rr8,rr9,rr10,rr11,rr12,rr13,rr14,rr15,rr16,rr17,rr18,rr19,rr20,rr21,rr22,rr23,rr24,rr25,rr26,rr27,rr28,rr29,rr30
    global rr31,rr32,rr33,rr34,rr35,rr36,rr37,rr38,rr39,rr40,rr41,rr42,rr43,rr44,rr45,rr46,rr47,rr48,rr49,rr50
    I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,I18,I19,I20,I21,I22,I23,I24,I25,I26,I27,I28,I29,I30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    I31,I32,I33,I34,I35,I36,I37,I38,I39,I40,I41,I42,I43,I44,I45,I46,I47,I48,I49,I50=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    L31,L32,L33,L34,L35,L36,L37,L38,L39,L40,L41,L42,L43,L44,L45,L46,L47,L48,L49,L50=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26,R27,R28,R29,R30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    R31,R32,R33,R34,R35,R36,R37,R38,R39,R40,R41,R42,R43,R44,R45,R46,R47,R48,R49,R50=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    rr1,rr2,rr3,rr4,rr5,rr6,rr7,rr8,rr9,rr10,rr11,rr12,rr13,rr14,rr15,rr16,rr17,rr18,rr19,rr20,rr21,rr22,rr23,rr24,rr25,rr26,rr27,rr28,rr29,rr30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    rr31,rr32,rr33,rr34,rr35,rr36,rr37,rr38,rr39,rr40,rr41,rr42,rr43,rr44,rr45,rr46,rr47,rr48,rr49,rr50=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    def h():
        w0.destroy()
        w.destroy()
        
    def g():
        global w0
        w0=Tk()
        w0.geometry("150x70")
        w0.configure(background = "lightblue")
        w0.title("ATTENDANCE-SHEET")
        l10=Label(w0,text="Data has been recorded!!!")
        l10.place(x=10,y=10)
        b0=Button(w0,text="OK",command=h)
        b0.place(x=55,y=40)
        w0.mainloop()
        
    def F():
        I=[I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,I18,I19,I20,I21,I22,I23,I24,I25,I26,I27,I28,I29,I30,I31,I32,I33,I34,I35,I36,I37,I38,I39,I40,I41,I42,I43,I44,I45,I46,I47,I48,I49,I50]
        L=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32,L33,L34,L35,L36,L37,L38,L39,L40,L41,L42,L43,L44,L45,L46,L47,L48,L49,L50]
        R=[R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26,R27,R28,R29,R30,R31,R32,R33,R34,R35,R36,R37,R38,R39,R40,R41,R42,R43,R44,R45,R46,R47,R48,R49,R50]
        RR=[rr1,rr2,rr3,rr4,rr5,rr6,rr7,rr8,rr9,rr10,rr11,rr12,rr13,rr14,rr15,rr16,rr17,rr18,rr19,rr20,rr21,rr22,rr23,rr24,rr25,rr26,rr27,rr28,rr29,rr30,rr31,rr32,rr33,rr34,rr35,rr36,rr37,rr38,rr39,rr40,rr41,rr42,rr43,rr44,rr45,rr46,rr47,rr48,rr49,rr50]
        for i in range(0,len(stud)):
            if i<=12:
                I[i]=IntVar() 
                L[i]= Label(w,text=f"{stud[i]}", fg="black", bg="white",width=18,height=1)
                L[i].place(y=40*i,x=00)
                R[i]=Radiobutton(w, text="present", value=1, variable=I[i])
                R[i].place(x=00,y=20+(i*40))
                RR[i]=Radiobutton(w, text="absent", value=2, variable=I[i])
                RR[i].place(x=68,y=20+(i*40))
                AttendanceLIST[i]=I[i].get()
            elif i>12 and i<=24:
                I[i]=IntVar() 
                L[i]= Label(w,text=f"{stud[i]}", fg="black", bg="white",width=18,height=1)
                L[i].place(y=40*(i-13),x=135)
                R[i]=Radiobutton(w, text="present", value=1, variable=I[i])
                R[i].place(x=135,y=20+((i-13)*40))
                RR[i]=Radiobutton(w, text="absent", value=2, variable=I[i])
                RR[i].place(x=203,y=20+((i-13)*40))
                AttendanceLIST[i]=I[i].get()
            elif i>24 and i<=36:
                I[i]=IntVar() 
                L[i]= Label(w,text=f"{stud[i]}", fg="black", bg="white",width=18,height=1)
                L[i].place(y=40*(i-25),x=270)
                R[i]=Radiobutton(w, text="present", value=1, variable=I[i])
                R[i].place(x=270,y=20+((i-25)*40))
                RR[i]=Radiobutton(w, text="absent", value=2, variable=I[i])
                RR[i].place(x=338,y=20+((i-25)*40))
                AttendanceLIST[i]=I[i].get()
            elif i>36 and i<=50:
                I[i]=IntVar() 
                L[i]= Label(w,text=f"{stud[i]}", fg="black", bg="white",width=18,height=1)
                L[i].place(y=40*(i-37),x=405)
                R[i]=Radiobutton(w, text="present", value=1, variable=I[i])
                R[i].place(x=405,y=20+((i-37)*40))
                RR[i]=Radiobutton(w, text="absent", value=2, variable=I[i])
                RR[i].place(x=473,y=20+((i-37)*40))
                AttendanceLIST[i]=I[i].get()
    global w       
    w=Tk()
    w.configure(background = "lightblue")
    w.title("ATTENDANCE")
    w.geometry("550x550")
    global stud
    stud=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]


    AttendanceLIST=[]

    for t in range(1,51):
        AttendanceLIST.append(0)

    F()

    b1=Button(w,text="submit",command=g)
    b1.place(x=230,y=500)
    w.mainloop()
    w.pack()


def timetable():
    def h(root): 
        for i in range(total_rows): 
            for j in range(total_columns):
                if i!=0 and j!=0:
                      lbl= Entry(root, width=18, fg='blue',font=('Arial',8,'bold'))
                      lbl.grid(row=i, column=j)
                      lbl.insert(END, lsth[i][j])
                else:
                    lbl= Entry(root, width=18, fg='brown',font=('Arial',8,'bold'))
                    lbl.grid(row=i, column=j)
                    lbl.insert(END, lsth[i][j])
                    
    
                    
                  
              
    global lsth 
    lsth = [('DAYS','Lecture-1','Lecture-2','Lecture-3','Lecture-4','Lecture-5','Lecture-6','Lecture-7','Lecture-8'),
            ('Monday','Maths','Maths','Chemistry','English','Physics','Physics','Computer-Science','Games'),
            ('Tuesday','Maths','English','Chemistry','Chemistry','Physics-Practicals','Physics-Practicals','Comp-Sc. Practicals','Comp-Sc. Practicals'),
            ('Wednesday','Physics','Physics','Computer-Science','Computer-Science','Maths','Maths','Chemistry','Work-Experience'),
            ('Thursday','Maths','Chemistry','Chemistry','English','Physics','Physics','Computer-Science','Games'),
            ('Friday','Physics','English','Computer-Science','Computer-Science','Games','Chemistry','Maths','Maths'),
            ('Saturday','English','Physics','Physics','Chemistry','Maths','Work-Experience','Chemistry-Practicals','Chemistry-Practicals')] 
    total_rows = len(lsth) 
    total_columns = len(lsth[0]) 
    root = Tk()
    root.title("TIME-TABLE")
    root.configure(background = "green")
    
    h(root) 
    root.mainloop()
def info():
    def h(root): 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                lbl= Entry(root, width=35, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                lbl.grid(row=i, column=j) 
                lbl.insert(END, lsth[i][j])

    global lsth  
    lsth = [('Name of Institution' ,'KENDRIYA VIDYALAYA'),
            ('Affiliation Number','1100002'),
            ('State','MAHARASHTRA'),
            ('District','THANE'),
            ('Postal Address','ORDNANCE ESTATE AMBARNATH'),
            ('Pin Code','421502'),
            ('PhNo.&STD Code','0251682263'),
            ('Email','kvambord@gmail.com'),
            ('Website','http://www.kvambernath.com'),
            ('Year of Foundation','1965'),
            ('Principal/ Head','D S Bhati'),
            ('Admin','4'),
            ('Teaching','34'),
            ('Status of The School','Senior Secondary'),
            ('Type of affiliation','Provisional'),
            ('Management','KENDRIYA VIDYALAYA SANGATHAN')] 

    total_rows = len(lsth) 
    total_columns = len(lsth[0]) 
    root = Tk()
    root.title("School Information")
    root.configure(background = "pink")

    h(root) 
    root.mainloop()

   
def reviews():
    root=Tk()
    root.title("Reviews")
    r1='Anshul Kumar- Quality of Education is Moderate and school has a small Kids Play area.'
    r2='Satish Mehta- Had a wonderful experience at this school spent best time in this school.'
    r3='Ankita Raorane-Really nice school good teachers but building seems to be old'
    r4='Rahul-Had a wonderful experience at this school spent best time in this school.'
    r5='Ajit Wakode-Nestled in greenery... Awesome during monsoon..'
    r6='Sameer Jadhav-Nice school under ordnance factory ambernath big play grounds and awesome teachers'
    r7='Sahil Nair-Very good school but shortage of teachers, every 6 months new teachers are coming and students studies are affected'
 
   
                  
    lbl1= Entry(root, width=110, fg='blue',font=('Arial',12,'bold')) 
    lbl1.grid(row=1, column=1) 
    lbl1.insert(END,r1)

    lbl2= Entry(root, width=110, fg='red',font=('Arial',12,'bold')) 
    lbl2.grid(row=2, column=1) 
    lbl2.insert(END,r2)

    
    lbl3= Entry(root, width=110, fg='pink',font=('Arial',12,'bold')) 
    lbl3.grid(row=3, column=1) 
    lbl3.insert(END,r3)


    
    lbl4= Entry(root, width=110, fg='green',font=('Arial',12,'bold')) 
    lbl4.grid(row=4, column=1) 
    lbl4.insert(END,r4)


    
    lbl5= Entry(root, width=110, fg='orange',font=('Arial',12,'bold')) 
    lbl5.grid(row=5, column=1) 
    lbl5.insert(END,r5)

    lbl6= Entry(root, width=110, fg='yellow',font=('Arial',12,'bold')) 
    lbl6.grid(row=6, column=1) 
    lbl6.insert(END,r6)

    lbl7= Entry(root, width=110, fg='grey',font=('Arial',12,'bold')) 
    lbl7.grid(row=7, column=1) 
    lbl7.insert(END,r7)




def aboutschool():
    root=Tk()
    root.title("About School")
    root.geometry('1000x500')
    r1='Kendriya Vidyalaya Ambarnath O.F., established in 1965. The school is affiliated to the CBSE'
    r2='It functions as a two shift with classes I to XII Science and Commerce.'
    r3='The school is affiliated to the CBSE'
    r4='It is an English Medium school. The school is located in Ambernath.'
    r5='It is a Government School and is part of Kendriya Vidyalaya Sangathan (KVS) and is managed by Defence.'
    r6='The motto of Kendriya Vidyalaya OF is Tat vam Pooshan Apaavrunu.'
    r7='School is part of Kendriya Vidyalaya Sangathan (KVS) an autonomous body formed under Ministry of HRD,Govt. of India.'
    r8='The Kendriya Vidyalaya (KV) is the largest chain of schools in India.'
    r9='KVs are considered to be the best CBSE schools in India as compared to other government schools and are among the top schools in India.'
    r10='K.V.Ambernath is one of the best CBSE schools in, Ambernath and ranks among the top schools in Ambernath.'
    r11='Here, the dedicated and professional teachers ensure that the children get the maximum out of their education '
    r12='The school has given exceptional results in the academic sphere and its students have excelled in extra co-curricular activities too '
    r13='The best gift you can give to your child is a right school for his/her academic, co-curricular and overall development '

    
    lbl1= Entry(root, width=110, fg='blue',font=('Arial',12,'bold')) 
      
    lbl1.grid(row=1, column=1) 
    lbl1.insert(END,r1)
    lbl2= Entry(root, width=110, fg='red',font=('Arial',12,'bold')) 
    lbl2.grid(row=2, column=1) 
    lbl2.insert(END,r2)
    
    lbl3= Entry(root, width=110, fg='yellow',font=('Arial',12,'bold'))
    lbl3.grid(row=3, column=1) 
    lbl3.insert(END,r3)
    
    lbl4= Entry(root, width=110, fg='green',font=('Arial',12,'bold'))
    lbl4.grid(row=4, column=1) 
    lbl4.insert(END,r4)
    
    
    lbl5= Entry(root, width=110, fg='grey',font=('Arial',12,'bold'))
    lbl5.grid(row=5, column=1) 
    lbl5.insert(END,r5)

    lbl6= Entry(root, width=110, fg='orange',font=('Arial',12,'bold'))
    lbl6.grid(row=6, column=1) 
    lbl6.insert(END,r6)
    
    lbl7= Entry(root, width=110, fg='blue',font=('Arial',12,'bold'))
    lbl7.grid(row=7, column=1) 
    lbl7.insert(END,r7)

    lbl8= Entry(root, width=110, fg='red',font=('Arial',12,'bold'))
    lbl8.grid(row=8, column=1) 
    lbl8.insert(END,r8)

    lbl9= Entry(root, width=110, fg='yellow',font=('Arial',12,'bold'))
    lbl9.grid(row=9, column=1) 
    lbl9.insert(END,r9)

    lbl10= Entry(root, width=110, fg='green',font=('Arial',12,'bold'))
    lbl10.grid(row=10, column=1) 
    lbl10.insert(END,r10)

    lbl11= Entry(root, width=110, fg='grey',font=('Arial',12,'bold'))
    lbl11.grid(row=11, column=1) 
    lbl11.insert(END,r11)

    lbl12= Entry(root, width=110, fg='orange',font=('Arial',12,'bold'))
    lbl12.grid(row=12, column=1) 
    lbl12.insert(END,r12)

    lbl13= Entry(root, width=110, fg='blue',font=('Arial',12,'bold'))
    lbl13.grid(row=13, column=1) 
    lbl13.insert(END,r13)


def notice():
    t=tkinter.messagebox.showinfo('NOTICE','No Notice yet!!! Come Soon!!!')

def competition():
    def h(root): 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                lbl= Entry(root, width=17, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                lbl.grid(row=i, column=j) 
                lbl.insert(END, lsth[i][j])
    
    global lsth  
    lsth = [('Essay Writing','2 April'),
            ('Story Writing','5 April'),
            ('Debate','15 April'),
            ('Poem Recitation','25 June'),
            ('English writing','1 July'),
            ('Hindi Writing','15 July'),
            ('Skit','20 August'),
            ('Dance','5 September'),
           ('Song (Group)','1 October'), 
           ('Song (Solo)','10 October'), 
           ('Sports Day','12 November'),
            ('Annual Day','30 November')] 
    total_rows = len(lsth) 
    total_columns = len(lsth[0]) 
    root = Tk()
    root.title("Competition and Events")
    root.configure(background = "pink")
    
    h(root) 
    root.mainloop()
def holiday():
    def h(root): 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                lbl= Entry(root, width=17, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                lbl.grid(row=i, column=j) 
                lbl.insert(END, lsth[i][j])
    
    global lsth  
    lsth = [('New Year','1 January'),
            ('Lohri','14 January'),
            ('Republic Day','26 January'),
            ('Holi','10 March'),
            ('Good Friday','26 April'),
            ('Ambedkar jayanti','14 April'),
            ('Janamasthmi','12 August'),
            ('Muharram','29 August'),
           ('Independence Day','15 August'), 
           ('Gandhi Jayanti','2 October'), 
           ('Dusherra','25 October'),
            ('Diwali','14 November'),
            ('Guru Nanak Jayanti','30 November'),
           ('Christmas','25 December')] 
    total_rows = len(lsth) 
    total_columns = len(lsth[0]) 
    root = Tk()
    root.title("Holiday List 2020")
    root.configure(background = "pink")
    
    h(root) 
    root.mainloop()

def welcome1():
    window = Tk()
    window.title("Enter your name")
    window.geometry('500x300')
    lbl = Label(window, text="Hello, Welcome to KVA",font=("times new roman",20),fg="red")
    lbl2= Label(window, text="ENTER YOUR NAME",font=("times new roman",10),fg="blue")
    lbl.pack(side="top")
    lbl2.pack(side="top")
    NAME=Entry(window,width=35)
    NAME.place(x=145,y=200)
    def destroyw():
        window.destroy()
        start.destroy()
    def clicked():
        
        res = "Welcome " + NAME.get()
        lbl.configure(text= res)
        btni = Button(window, text="LAUNCH", command=destroyw)
        btni.place(x=250,y=250)
    btn = Button(window, text="Click Me", command=clicked)
    btn.place(x=180,y=250)
  

    window.mainloop()
    password()
def welcome2():
    window = Tk()
    window.title("Enter your name")
    window.geometry('500x300')
    lbl = Label(window, text="Hello, Welcome to KVA",font=("times new roman",20),fg="red")
    lbl2= Label(window, text="ENTER YOUR NAME",font=("times new roman",10),fg="blue")
    lbl.pack(side="top")
    lbl2.pack(side="top")
    txt=Entry(window,width=35)
    txt.place(x=145,y=200)
    def destroyw():
        window.destroy()
        start.destroy()
    def clicked():  
        res = "Welcome " + txt.get()
        lbl.configure(text= res)
        btni = Button(window, text="LAUNCH", command=destroyw)
        btni.place(x=250,y=250)
    btn = Button(window, text="Click Me", command=clicked)
    btn.place(x=180,y=250)


    window.mainloop()
    runstudent()
    
    
def entry5():
    global e5
    global e51
    global InputSub
    global InputMarks
    InputSub=0
    InputMarks=0
    e5=0
    e51=0
    def k():
        InputSub=e5
        InputMarks=e51
        w53=Tk()
        w53.geometry('290x50')
        w53.title("Editing Marks Data")
        w53.configure(background = "lightblue")
        L53=Label(w53,text="The changes are made successfully.",bg="lightgreen")
        L53.place(x=30,y=20)
    def f():                                      
        searchitem=int(E52.get())
        print(type(searchitem))
        found = False
        sql= "select RollNo from marks"     
        cur.execute(sql)
        lst=cur.fetchall()
        for i in range(len(lst)):
            tup = lst[i]
            if tup[0]== searchitem:
                found = True
                w5=Tk()
                w5.geometry('700x400')
                w5.title("Editing Marks Data")
                w5.configure(background = "lightblue")
                L5=Label(w5,text="Choose the subject whose marks are to be changed",bg="lightgreen")
                L5.place(x=30,y=20)
                E5=Entry(w5)
                box=ttk.Combobox(w5,textvariable=E5,state="readonly",font=("arial",12,"bold"),width=22)
                box['values']=['CS','CHEMISTRY' ,'PHYSICS','MATHS','ENGLISH']
                box.place(x=310,y=20)
                L53=Label(w5,text="New marks of the chosen subject")
                L53.place(x=60,y=70)
                E51= Entry(w5)
                E51.place(x=245,y=70)
                E51.pack()
                e5=E5.get()
                e51=int(float(E51.get()))
                sql = " update table Marks set %s = %s where RollNo= %s "
                val = (E5.get(),e51,searchitem)
                con.commit()
                B5=Button(w5,text="submit",bg="green",fg="brown",width=10,height=1,command=k)
                B5.place(x=180,y=120)
                break
            else:
                pass
        if found == False:
            w51=Tk()
            w51.title("Invalid roll no")
            w51.configure(background = "lightblue")
            w51.geometry('250x100')
            def g():
                w51.destroy()
            L51=Label(w51,text='The Roll no. was not found in the list!')
            L51.place(x=30,y=30)
            B51=Button(w51,text='OK',bg='green',fg='purple',width=10,height=1,command=g)
            B51.place(x=100,y=60)
            w51.mainloop()
    window=Tk()
    window.title("Editing Marks Data")
    window.geometry('500x130')
    window.configure(background = "lightblue")
    L52=Label(window,text="Roll no. of the student whose marks is to be changed:-")
    L52.place(x=30,y=30)
    E52=Entry(window)
    E52.place(x=327,y=30) 
    B52=Button(window,text='submit',bg='green',fg='purple',width=10,height=1,command=f)
    B52.place(x=200,y=60)
    window.mainloop()

    print(InputMarks)

def entry6():
    global e6
    global e61
    global SectionInput
    global DataInput
    SectionInput=0
    DataInput=0
    e6=0
    e61=0
    def T():
        SectionInput=e6
        DataInput=e61
        w63=Tk()
        w63.geometry('290x50')
        w63.title("Editing Student's Details")
        w63.configure(background = "lightblue")
        L63=Label(w63,text="The changes are made successfully.",bg="lightgreen")
        L63.place(x=30,y=20)
    def P():
        searchitem=int(E62.get())
        found = False
        sql= "select RollNo from marks"     
        cur.execute(sql)
        lst=cur.fetchall()
        for i in range(len(lst)):
            tup = lst[i]
            if tup[0]== searchitem:
                found = True
                w6=Tk()
                w6.geometry('700x400')
                w6.title("Editing Student's Details")
                w6.configure(background = "lightblue")
                L6=Label(w6,text="Choose which one of the details are to be    changed",bg="lightgreen")                                          
                L6.place(x=30,y=20)
                E6=Entry(w6)
                box=ttk.Combobox(w6,textvariable=E6,state="readonly",font=("arial",12,"bold"),width=22)
                box['values']=["Name","DOB","Phone Number","Stream","Class","Section","Admission number"]
                box.place(x=310,y=20)
                L63=Label(w6,text="New data of the chosen section")
                L63.place(x=60,y=70)
                E61=Entry(w6)
                E61.place(x=245,y=70)
                e6=E6.get()
                e61=E61.get()
                sql = " update table Stud_details set %s = %s where RollNo= %s "
                val = ( E6.get(), E61.get(),searchitem)
                con.commit()
                B6=Button(w6,text="submit",bg="green",fg="brown",width=10,height=1,command=T)
                B6.place(x=180,y=120)
                break
            else:
                pass
        if found == False:
            w61=Tk()
            w61.title("Invalid roll no")
            w61.configure(background = "lightblue")
            w61.geometry('250x100')
            def g():
                w61.destroy()
            L61=Label(w61,text='The Roll no. was not found in the list!')
            L61.place(x=30,y=30)
            B61=Button(w61,text='OK',bg='green',fg='purple',width=10,height=1,command=g)
            B61.place(x=100,y=60)
            w61.mainloop()
    window6=Tk()
    window6.title("Editing Student's Details")
    window6.geometry('500x130')
    window6.configure(background = "lightblue")
    L62=Label(window6,text="Roll no. of the student whose details are to be changed:-")
    L62.place(x=30,y=30)
    E62=Entry(window6)
    E62.place(x=350,y=30) 
    B62=Button(window6,text='submit',bg='green',fg='purple',width=10,height=1,command=P)
    B62.place(x=200,y=60)
    window6.mainloop()
def entry9():
    def k():
        pass
        #make if-else statement here if roll no. not found then what to do
        #delete the marks data of roll no. input
        t=tkinter.messagebox.showinfo('NOTICE','Marks deleted successfully')
        window.destroy()
        
    window=Tk()
    window.title("Deleting Marks Data")
    window.geometry('500x130')
    window.configure(background = "lightblue")
    L52=Label(window,text="Roll no. of the student whose marks are to be deleted")
    L52.place(x=30,y=30)
    E52=Entry(window)
    E52.place(x=327,y=30) 
    B52=Button(window,text='submit',bg='green',fg='purple',width=10,height=1,command=k)
    B52.place(x=200,y=60)
    window.mainloop()
def entry10():
    def y():
        pass
        #make if-else statement here if roll no. not found then what to do
        #delete the marks data of roll no. input
        t=tkinter.messagebox.showinfo('NOTICE','Student Data Deleted Successfully')
        window.distroy()
        
    window=Tk()
    window.title("Deleting Student Data")
    window.geometry('500x130')
    window.configure(background = "lightblue")
    L52=Label(window,text="Roll no. of the student whose data is to be deleted")
    L52.place(x=30,y=30)
    E52=Entry(window)
    E52.place(x=327,y=30) 
    B52=Button(window,text='submit',bg='green',fg='purple',width=10,height=1,command=y)
    B52.place(x=200,y=60)
    window.mainloop()
    
    


def entry8():
    window = Tk()
    window.title("CHOICE")
    window.geometry('770x500')
    window.configure(background = "lightblue")
    submit1= Button(window, text="DELETE MARKS DATA ", bg="pink", height=20, width=50 ,command=entry9)
    submit2= Button(window, text="DELETE STUDENT DATA ", bg="pink",height=20, width=50,command=entry10)
    submit1.place(x=10,y=100)
    submit2.place(x=400,y=100)
    window.mainloop()
    
def entry7():
    window = Tk()
    window.title("CHOICE")
    window.geometry('770x500')
    window.configure(background = "lightblue")
    submit1= Button(window, text="CHANGE MARKS DATA ", bg="pink", height=20, width=50 ,command=entry5)
    submit2= Button(window, text="CHANGE STUDENT DATA ", bg="pink",height=20, width=50,command=entry6)
    submit1.place(x=10,y=100)
    submit2.place(x=400,y=100)
    window.mainloop()


def entry3():
      
    root=Tk()
    root.geometry("350x700+0+0")
    label=Label(root,text="REGISTRATION FORM", font=("arial",20), bg="blue")
    label.pack(side=TOP, fill=X)

    label1 =Label(root,text="NAME:",bg="pink")
    label1.place(x=30, y=100)

    label2=Label(root,text="FATHERS NAME:",bg="pink")
    label2.place(x=30, y=150)

    label3=Label(root,text="EMAIL:",bg="pink")
    label3.place(x=30, y=200)

    label4=Label(root,text="CLASS:",bg="pink")
    label4.place(x=30, y=250)

    label5=Label(root,text="TC NO.:",bg="pink")
    label5.place(x=30, y=300)

    label6=Label(root,text="EMAIL ID:",bg="pink")
    label6.place(x=30, y=350)

    label7=Label(root,text="CONTACT NO.:",bg="pink")
    label7.place(x=30, y=400)

    label8=Label(root,text="CATEGORY:",bg="pink")
    label8.place(x=30, y=450)

    label9=Label(root,text="STREAM:",bg="pink")
    label9.place(x=30, y=500)

    label10=Label(root,text="SUBJECT:",bg="pink")
    label10.place(x=30, y=550)

    entry1=Entry(root,width=20)
    entry1.place(x=150,y=100)

    entry2=Entry(root,width=20)
    entry2.place(x=150,y=150)

    entry3=Entry(root,width=20)
    entry3.place(x=150,y=200)

    entry4=Entry(root,width=20)
    entry4.place(x=150,y=250)

    entry5=Entry(root,width=20)
    entry5.place(x=150,y=300)

    entry6=Entry(root,width=20)
    entry6.place(x=150, y=350)

    entry7=Entry(root,width=20)
    entry7.place(x=150, y=400)

    entry8=Entry(root,width=20)
    entry8.place(x=150, y=450)

    entry9=Entry(root,width=20)
    entry9.place(x=150, y=500)

    entry10=Entry(root,width=20)
    entry10.place(x=150, y=550)
    entry31=entry1.get()
    entry32=entry2.get()
    entry33=entry3.get()
    entry34=entry4.get()
    entry35=entry5.get()
    entry36=entry6.get()
    entry37=entry7.get()
    entry38=entry8.get()
    entry39=entry9.get()
    entry310=entry10.get()
    
    
def entry2():
    window = Tk()
    window.title("KVA")
    window.geometry('400x300')
    window.configure(background = "lightblue")
    a = Label(window ,text = "Name")
    b = Label(window ,text = "DOB")
    c = Label(window ,text = "Phone Number")
    d = Label(window ,text = "Stream")
    e = Label(window ,text = "Class")
    f = Label(window ,text = "Section")
    g = Label(window ,text = "Admission number")
    a.place(x=20,y=30)
    b.place(x=20,y=60)
    c.place(x=20,y=90)
    d.place(x=20,y=120)
    e.place(x=20,y=150)
    f.place(x=20,y=180)
    g.place(x=20,y=210)
    a1 = Entry(window)
    b1 = Entry(window)
    c1 = Entry(window)
    d1 = Entry(window)
    e1 = Entry(window)
    f1 = Entry(window)
    g1 = Entry(window)
    a1.place(x=150,y=30)
    b1.place(x=150,y=60)
    c1.place(x=150,y=90)
    d1.place(x=150,y=120)
    e1.place(x=150,y=150)
    f1.place(x=150,y=180)
    g1.place(x=150,y=210)
    entry21=a1.get()
    entry22=b1.get()
    entry23=c1.get()
    entry24=d1.get()
    entry25=e1.get()
    entry26=f1.get()
    entry27=g1.get()

    
    def insert():
        print("Name:",a1.get())
        print("DOB:",b1.get())
        print("Phone number:",c1.get())
        print("Stream:",d1.get())
        print("Class:",e1.get())
        print("Section:",f1.get())
        print("Admission number:",g1.get())
    submit= Button(window, text="Submit Your Response ", bg="pink", command=insert)
    submit.place(x=70,y=250)
    window.mainloop()


def entry1():
    window = Tk()
    window.title("KVA")
    window.geometry('265x320')
    window.configure(background = "lightblue")
    a = Label(window ,text = "Name")
    b = Label(window ,text = "Total Marks")
    c = Label(window ,text = "Maths")
    d = Label(window ,text = "Physics")
    e = Label(window ,text = "Chemistry")
    f = Label(window ,text = "CS")
    g = Label(window ,text = "English")
    h = Label(window ,text = "Roll number")
    a.place(x=20,y=30)
    b.place(x=20,y=60)
    c.place(x=20,y=90)
    d.place(x=20,y=120)
    e.place(x=20,y=150)
    f.place(x=20,y=180)
    g.place(x=20,y=210)
    h.place(x=20,y=240)
    a1 = Entry(window)
    b1 = Entry(window)
    c1 = Entry(window)
    d1 = Entry(window)
    e1 = Entry(window)
    f1 = Entry(window)
    g1 = Entry(window)
    h1 = Entry(window)
    a1.place(x=100,y=30)
    b1.place(x=100,y=60)
    c1.place(x=100,y=90)
    d1.place(x=100,y=120)
    e1.place(x=100,y=150)
    f1.place(x=100,y=180)
    g1.place(x=100,y=210)
    h1.place(x=100,y=240)
    entry11=a1.get()
    entry12=b1.get()
    entry13=c1.get()
    entry14=d1.get()
    entry15=e1.get()
    entry16=f1.get()
    entry17=g1.get()
    entry18=h1.get()
    
    
    def insert():
        print("Name:",a1.get())
        print("Total Marks:",b1.get())
        print("Maths:",c1.get())
        print("Physics:",d1.get())
        print("Chemistry:",e1.get())
        print("Computer Science:",f1.get())
        print("English:",g1.get())
        print("Roll Number:",h1.get())
    submit= Button(window, text="Submit Your Response ", bg="pink", command=insert)
    submit.place(x=70,y=275)
    window.mainloop()
    window.configure(text="Button was clicked !!")
def runadmin():
    firstw=Tk()
    firstw.title("Kendriya Vidyalaya Ambernath : ADMINISTRATION")
    firstw.geometry("1024x720")
    firstw.configure(background = "lightblue")
    label=Label(text="Kendriya Vidyalaya Ambernath",font=("times new roman",50),bg="blue")
    label2=Label(text="WELCOME",font=("times new roman",50),bg="white")
    label.pack(side=TOP ,fill=X)
    label2.pack(side=BOTTOM ,fill=X)
    label3=Label(text="Made by Brij , Bhawika and Anurag",font=("Arial Bold",20),bg="lightblue")
    label3.place(x=280,y=90)
    label3=Label(text="",font=("times new roman",20),bg="lightblue")
    label4=Label(firstw,text=str(now.strftime("%Y-%m-%d %H:%M:%S")),font=("times new roman",10),bg="white")
    label4.pack(side=BOTTOM ,fill=X)
    submith = Button(firstw, text="Holidays and Leaves", bg="lightgreen" ,command=holiday,font=('Times New Roman','15'),width='15')
    submith.place(x=830,y=150)
    submitc = Button(firstw, text="Competition/events", bg="LightGrey" ,command=competition,font=('Times New Roman','15'),width='15')
    submitc.place(x=830,y=250)
    submitn = Button(firstw, text="Notice", bg="red" ,command=notice,font=('Times New Roman','15'),width='15')
    submitn.place(x=830,y=350)
    submita = Button(firstw, text="About", bg="yellow" ,command=aboutschool,font=('Times New Roman','15'),width='15')
    submita.place(x=830,y=450)
    submitr = Button(firstw, text="Reviews", bg="orange" ,command=reviews,font=('Times New Roman','15'),width='15')
    submitr.place(x=830,y=550)
    submiti = Button(firstw, text="School info", bg="pink" ,command=info,font=('Times New Roman','15'),width='15')
    submiti.place(x=430,y=150)
    submitc = Button(firstw, text="Change Password", bg="violetred" ,command=changepassword,font=('Times New Roman','15'),width='15')
    submitc.place(x=430,y=250)
    submitt = Button(firstw, text="Time Table", bg="orange" ,command=timetable,font=('Times New Roman','15'),width='15')
    submitt.place(x=430,y=350)
    submitf = Button(firstw, text="Fees", bg="orchid" ,command=fees,font=('Times New Roman','15'),width='15')
    submitf.place(x=430,y=450)
    submite = Button(firstw, text="View Enquiry", bg="lightgreen" ,command=viewenquiry,font=('Times New Roman','15'),width='15')
    submite.place(x=430,y=550)
    submitvf = Button(firstw, text="Viewfees", bg="orchid" ,command=viewfees,font=('Times New Roman','15'),width='15')
    submitvf.place(x=220,y=350)
    submit1 = Button(firstw, text="Enter Marks Detail", bg="lightgreen" ,command=entry1,font=('Times New Roman','15'),width='15')
    submit1.place(x=10,y=150)
    submit2 = Button(firstw, text="Enter Student Detail", bg="orange",font=('Times New Roman','15'), command=entry2,width='15')
    submit2.place(x=10,y=250)
    submit3= Button(firstw, text="New Registration", bg="pink",font=('Times New Roman','15'), command=entry3,width='15')
    submit3.place(x=10,y=350)
    submit4= Button(firstw, text="Modify Existing Data", bg="orange",font=('Times New Roman','15'), command=entry7,width='15')
    submit4.place(x=10,y=450)
    submit5= Button(firstw, text="Attendance", bg="yellow",font=('Times New Roman','15'), command=attendence,width='15')
    submit5.place(x=10,y=550)
    submit6= Button(firstw, text="Delete existing data", bg="yellow",font=('Times New Roman','15'), command=entry8,width='15')
    submit6.place(x=630,y=350)
def runstudent():
    firstw=Tk()
    firstw.title("Kendriya Vidyalaya Ambernath : STUDENTS")
    firstw.geometry("1024x720")
    firstw.configure(background = "lightblue")
    label=Label(text="Kendriya Vidyalaya Ambernath",font=("times new roman",50),bg="blue")
    label2=Label(text="WELCOME",font=("times new roman",50),bg="white")
    label4=Label(firstw,text=str(now.strftime("%Y-%m-%d %H:%M:%S")),font=("times new roman",10),bg="white")
    label.pack(side=TOP ,fill=X)
    label2.pack(side=BOTTOM ,fill=X)
    label4.pack(side=BOTTOM ,fill=X)
    label3=Label(text="Made by Brij , Bhawika and Anurag",font=("Arial Bold",20),bg="lightblue")
    label3.place(x=300,y=90)
    label3=Label(text="",font=("times new roman",20),bg="lightblue")
    submith = Button(firstw, text="Holidays and Leaves", bg="red" ,command=holiday,font=('Times New Roman','20'),width='20')
    submith.place(x=260,y=150)
    submitc = Button(firstw, text="Competition and events", bg="orange" ,command=competition,font=('Times New Roman','20'),width='20')
    submitc.place(x=260,y=250)
    submitn = Button(firstw, text="Notice Board", bg="lightgreen" ,command=notice,font=('Times New Roman','20'),width='20')
    submitn.place(x=260,y=350)
    submitm = Button(firstw, text="Marks", bg="blue" ,command=marks,font=('Times New Roman','20'),width='20')
    submitm.place(x=260,y=450)
    submita = Button(firstw, text="About KVA", bg="yellow" ,command=aboutschool,font=('Times New Roman','20'),width='15')
    submita.place(x=10,y=150)
    submitr = Button(firstw, text="Reviews", bg="orange" ,command=reviews,font=('Times New Roman','20'),width='15')
    submitr.place(x=10,y=250)
    submiti = Button(firstw, text="School info", bg="pink" ,command=info,font=('Times New Roman','20'),width='15')
    submiti.place(x=10,y=350)
    submitt = Button(firstw, text="Time Table", bg="green" ,command=timetable,font=('Times New Roman','20'),width='15')
    submitt.place(x=10,y=450)
    submite = Button(firstw, text="Enquiry", bg="grey" ,command=enquiryadmin,font=('Times New Roman','20'),width='15')
    submite.place(x=580,y=150)
    submitvf = Button(firstw, text="Viewfees", bg="orchid" ,command=viewfees,font=('Times New Roman','20'),width='15')
    submitvf.place(x=580,y=250)
def password():
    p=Tk()
    p.title("Kendriya Vidyalaya Ambernath")
    p.geometry("500x500")
    label=Label(text="Kendriya Vidyalaya Ambernath",font=("times new roman",20),bg="blue")
    label.pack(side=TOP ,fill=X)
    user1=Label(text="USERNAME",font="arial")
    user1.place(x=80,y=50)
    user=Entry(font="arial")
    user.place(x=200,y=50)
    user2=Label(text="PASSWORD",font="arial")
    user2.place(x=80,y=100)
    user3=Entry(show="*",font="arial")
    user3.place(x=200,y=100)

    def destroy():
        p.destroy()
    def login():
        if user.get()==NEWUSERNAME and user3.get()==NEWPASSWORD:
            destroy()
            runadmin()

        else:
            t=tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ", "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
            user.delete(0,END)
            user3.delete(0,END)
    INQUIRY=Button(text="LOGIN",font=("arial"),bg="Lightpink",command=login )
    INQUIRY.place(x=80,y=150)
print ('software is runing......')    
start = Tk()
start.title("ENTER")
start.geometry('275x200')
start.configure(background = "pink")
btn1=Button(start, text="ADMIN", command=welcome1,font=('Arial','30'))
btn2=Button(start, text="STUDENTS", command=welcome2,font=('Arial','30'))
btn1.place(x=10,y=10)
btn2.place(x=10,y=100)                                                                                 



    
    
    


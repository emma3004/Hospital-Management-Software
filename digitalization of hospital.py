from tkinter import *
import pymysql as mysql
import tkinter.messagebox as Messagebox
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

def adminmodewindow():
    rootadminmode=Tk()
    rootadminmode.geometry("720x480")
    rootadminmode.title("ADMIN")
    rootadminmode.configure(bg='cadetblue2')
    title=Label(rootadminmode,text="ADMIN",font=('bold',30),bg='cadetblue2')
    title.pack()  

    managepatients=Button(rootadminmode, text="MANAGE PATIENTS", font=('times new roman',23),command=managepatientswindow)
    managepatients.place(x=200,y=100)
    managedoctors=Button(rootadminmode, text="MANAGE DOCTORS", font=('times new roman',23), command=managedoctorswindow)
    managedoctors.place(x=200,y=200)
    manageappointments=Button(rootadminmode, text="MANAGE APPOINTMENTS", font=('times new roman',23), command=manageappointmentswindow)
    manageappointments.place(x=160,y=300)
    backadmin=Button(rootadminmode, text="BACK",font=('times new roman',22), command=rootadminmode.destroy)
    backadmin.place(x=295,y=400)
    
def managepatientswindow():
    rootmanagepatients=Tk()
    rootmanagepatients.geometry("720x480")
    rootmanagepatients.configure(bg='cadetblue2')
    rootmanagepatients.title("MANAGE PATIENT DATA")
    title=Label(rootmanagepatients, text="MANAGE PATIENT DATA", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    addpatient=Button(rootmanagepatients, text="ADD NEW PATIENT DATA",font=('times new roman',21),command=addpatientswindow)
    addpatient.place(x=180,y=80)
    editpatient=Button(rootmanagepatients,text="EDIT PATIENT DATA",font=('times new roman',21),command=editpatientwindow)
    editpatient.place(x=210,y=160)
    displaypatient=Button(rootmanagepatients, text="DISPLAY PATIENT DATA",font=('times new roman',21),command=displaypatientwindow)
    displaypatient.place(x=180,y=240)
    deletepatient=Button(rootmanagepatients, text="DELETE PATIENT DATA",font=('times new roman',21),command=deletepatientwindow)
    deletepatient.place(x=180,y=320)
    backpatient=Button(rootmanagepatients, text="BACK",font=('times new roman',21),command=rootmanagepatients.destroy)
    backpatient.place(x=300,y=400)
        
def managedoctorswindow():
    rootmanagedoctors=Tk()
    rootmanagedoctors.geometry("720x480")
    rootmanagedoctors.configure(bg='cadetblue2')
    rootmanagedoctors.title("MANAGE DOCTORS DATA")
    title=Label(rootmanagedoctors, text="MANAGE DOCTORS DATA", font=('bold',30),bg='cadetblue2')
    title.pack()    
    
    adddoctor=Button(rootmanagedoctors, text="ADD NEW DOCTOR DATA",font=('times new roman',21),command=adddoctorswindow)
    adddoctor.place(x=180,y=80)
    editdoctor=Button(rootmanagedoctors,text="EDIT DOCTOR DATA",font=('times new roman',21),command=editdoctorwindow)
    editdoctor.place(x=210,y=160)
    displaydoctor=Button(rootmanagedoctors, text="DISPLAY DOCTOR DATA",font=('times new roman',21),command=displaydoctorwindow)
    displaydoctor.place(x=180,y=240)
    deletedoctor=Button(rootmanagedoctors, text="DELETE DOCTOR DATA",font=('times new roman',21),command=deletedoctorwindow)
    deletedoctor.place(x=180,y=320)
    backdoctor=Button(rootmanagedoctors, text="BACK",font=('times new roman',21),command=rootmanagedoctors.destroy)
    backdoctor.place(x=300,y=400)
    
def manageappointmentswindow():
    rootmanageappointments=Tk()
    rootmanageappointments.geometry("720x480")
    rootmanageappointments.configure(bg='cadetblue2')
    rootmanageappointments.title("MANAGE APPPOINTMENTS DATA")
    title=Label(rootmanageappointments, text="MANAGE APPOINTMENTS DATA", font=('bold',30),bg='cadetblue2')
    title.pack()

    bookappointment=Button(rootmanageappointments, text="BOOK AN APPOINTMENT",font=('times new roman',23),command=bookappointmentwindow)
    bookappointment.place(x=155,y=80)
    cancelappointment=Button(rootmanageappointments, text="DISPLAY APPOINTMENTS",font=('times new roman',23),command=displayappointment)
    cancelappointment.place(x=155,y=160)
    listofdoctors=Button(rootmanageappointments,text="LIST OF DOCTORS",font=('times new roman',23),command=listofdoctorswindow)
    listofdoctors.place(x=200,y=240)
    servicesavailable=Button(rootmanageappointments,text="SERVICES AVAILABLE",font=('times new roman',23),command=servicesavailablewindow)
    servicesavailable.place(x=170,y=320)
    backappointment=Button(rootmanageappointments, text="BACK",font=('times new roman',23),command=rootmanageappointments.destroy)
    backappointment.place(x=290,y=400)

def addpatientswindow():
    rootaddpatients=Tk()
    rootaddpatients.geometry("720x480")
    rootaddpatients.configure(bg='cadetblue2')
    rootaddpatients.title("ADD PATIENTS")
    title=Label(rootaddpatients, text="ADD PATIENTS", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def insert():
        patientdepartment=entry_patientdepartment.get();
        doctorname=entry_doctorname.get();
        patientname=entry_patientname.get();
        patientage=entry_patientage.get();
        patientgender=entry_patientgender.get();
        patientaddress=entry_patientaddress.get();
        patientid=entry_patientid.get();
        
        if (patientdepartment=="" or doctorname=="" or patientname=="" or patientage=="" or patientgender=="" or patientaddress=="" or patientid==""):
            Messagebox.showinfo("Insert status","All the fields must be filled")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("insert into addpatients values ('"+ patientdepartment +"','"+ doctorname +"','"+ patientname +"','"+ patientage +"','"+ patientgender +"','"+ patientaddress +"','"+ patientid +"')")
            cursor.execute("commit");
        
            entry_patientdepartment.delete(0, 'end')
            entry_doctorname.delete(0, 'end')
            entry_patientname.delete(0, 'end')
            entry_patientage.delete(0, 'end')
            entry_patientgender.delete(0, 'end')
            entry_patientaddress.delete(0, 'end')
            entry_patientid.delete(0, 'end')
        
            Messagebox.showinfo("Insert Status","Inserted Successfully");
            con.close();
        
    patientid=Label(rootaddpatients, text="PATIENT ID",font=('times new roman',17),bg='cadetblue2')
    patientid.place(x=70,y=80)
    patientname=Label(rootaddpatients, text="PATIENT NAME",font=('times new roman',17),bg='cadetblue2')
    patientname.place(x=70,y=127)
    patientage=Label(rootaddpatients, text="PATIENT AGE",font=('times new roman',17),bg='cadetblue2')
    patientage.place(x=70,y=180)
    patientgender=Label(rootaddpatients, text="PATIENT GENDER",font=('times new roman',17),bg='cadetblue2')
    patientgender.place(x=70,y=227)
    doctorname=Label(rootaddpatients, text="NAME OF DOCTOR",font=('times new roman',17),bg='cadetblue2')
    doctorname.place(x=70,y=280)    
    patientdepartment=Label(rootaddpatients, text="PATIENT DEPARTMENT",font=('times new roman',17),bg='cadetblue2')
    patientdepartment.place(x=70,y=327)
    patientaddress=Label(rootaddpatients, text="PATIENT ADDRESS",font=('times new roman',17),bg='cadetblue2')
    patientaddress.place(x=70,y=380)
        
    entry_patientid=Entry(rootaddpatients, textvariable=patientroomnumber_var,font=('times new roman',17))
    entry_patientid.place(x=400,y=80)
    entry_patientname=Entry(rootaddpatients, textvariable=patientname_var,font=('times new roman',17))
    entry_patientname.place(x=400,y=127)
    entry_patientage=Entry(rootaddpatients, textvariable=patientage_var,font=('times new roman',17))
    entry_patientage.place(x=400,y=180)
    entry_patientgender=Entry(rootaddpatients, textvariable=patientgender_var,font=('times new roman',17))
    entry_patientgender.place(x=400,y=227)
    entry_doctorname=Entry(rootaddpatients, textvariable=nameofdoctor_var,font=('times new roman',17))
    entry_doctorname.place(x=400,y=280)
    entry_patientdepartment=Entry(rootaddpatients, textvariable=patientdepartment_var,font=('times new roman',17))
    entry_patientdepartment.place(x=400,y=327)
    entry_patientaddress=Entry(rootaddpatients, textvariable=patientaddress_var,font=('times new roman',17))
    entry_patientaddress.place(x=400,y=380)
    
    insert1=Button(rootaddpatients,text="INSERT",font=('times new roman',17),command=insert)
    insert1.place(x=200,y=420)
    backaddpatient=Button(rootaddpatients,text="BACK",font=('times new roman',17),command=rootaddpatients.destroy)
    backaddpatient.place(x=400,y=420)
    
def deletepatientwindow():
    rootdeletepatient=Tk()
    rootdeletepatient.geometry("720x480")
    rootdeletepatient.configure(bg='cadetblue2')
    rootdeletepatient.title("DELETE PATIENTS")
    title=Label(rootdeletepatient, text="DELETE PATIENTS", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def delete():
        
        if (entry_patientid.get() ==""):
            Messagebox.showinfo("Delete status","Patient ID column is mandatory for delete option")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("delete from addpatients where pid= '"+ entry_patientid.get() +"'")
            cursor.execute("commit");
            entry_patientid.delete(0, 'end')
            
            Messagebox.showinfo("Delete Status","Deleted Successfully");
            con.close();   
        
    patientname=Label(rootdeletepatient, text="PATIENT NAME",font=('times new roman',23),bg='cadetblue2')
    patientname.place(x=50,y=150)
    patientid=Label(rootdeletepatient, text="PATIENT ID",font=('times new roman',23),bg='cadetblue2')
    patientid.place(x=70,y=250)
     
    entry_patientname=Entry(rootdeletepatient, textvariable=patientname_var,font=('times new roman',23))
    entry_patientname.place(x=310,y=150)
    entry_patientid=Entry(rootdeletepatient, textvariable=patientroomnumber_var,font=('times new roman',23))
    entry_patientid.place(x=310,y=250)
    
    delete=Button(rootdeletepatient,text="DELETE",font=('times new roman',23),command=delete)
    delete.place(x=180,y=380)
    backdeletepatient=Button(rootdeletepatient, text="BACK",font=('times new roman',23), command=rootdeletepatient.destroy)
    backdeletepatient.place(x=400,y=380)
    
def displaypatientwindow():
    rootdisplaywindow = Tk()
    rootdisplaywindow.geometry("720x480")
    rootdisplaywindow.configure(bg='cadetblue2')    
    rootdisplaywindow.title(" PATIENTS DATA ")
    title=Label(rootdisplaywindow, text="PATIENTS DATA", font=('bold',30),bg='cadetblue2')
    title.pack()

    con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
    cursor=con.cursor()
    cursor.execute("select * from addpatients")
    rows=cursor.fetchall();


    frm=Frame(rootdisplaywindow)
    frm.pack(side=tk.LEFT,padx=20)
    
    tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6,7),show="headings",height="5")
    tv.pack()
    
    tv.heading(1, text="Patient_Department")
    tv.heading(2, text="DoctorName")
    tv.heading(3, text="PatientName")
    tv.heading(4, text="PatientAge")
    tv.heading(5, text="PatientGender")
    tv.heading(6, text="PatientAddress")
    tv.heading(7, text="PatientID")

    for i in rows:
       tv.insert('',  'end',values=i)
        
def adddoctorswindow():
    
    rootadddoctors=Tk()
    rootadddoctors.geometry("720x480")
    rootadddoctors.configure(bg='cadetblue2')
    rootadddoctors.title("ADD DOCTORS")
    title=Label(rootadddoctors, text="ADD DOCTORS DATA", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def entry():
        doctordepartment=entry_doctordepartment.get();
        doctorname=entry_doctorname.get();
        doctoraddress=entry_doctoraddress.get();
        doctorid=entry_doctorid.get();
        
        if (doctordepartment=="" or doctorname=="" or doctoraddress==""or doctorid==""):
            Messagebox.showinfo("Insert status","All the fields must be filled")
        
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("insert into add_doctors values ('"+ doctordepartment +"','"+ doctorname +"','"+ doctoraddress +"','"+ doctorid +"')")
            cursor.execute("commit");
        
            entry_doctordepartment.delete(0, 'end')
            entry_doctorname.delete(0, 'end')
            entry_doctoraddress.delete(0, 'end')
            entry_doctorid.delete(0, 'end')
        
            Messagebox.showinfo("Insert Status","Inserted Successfully");
            con.close();   
    
    doctordepartment=Label(rootadddoctors, text="DOCTOR DEPARTMENT",font=('times new roman',20),bg='cadetblue2')
    doctordepartment.place(x=50,y=110)
    doctorname=Label(rootadddoctors, text="NAME OF DOCTOR",font=('times new roman',20),bg='cadetblue2')
    doctorname.place(x=70,y=180)
    doctoraddress=Label(rootadddoctors, text="DOCTOR ADDRESS",font=('times new roman',20),bg='cadetblue2')
    doctoraddress.place(x=70,y=250)
    doctorid=Label(rootadddoctors, text="DOCTOR ID",font=('times new roman',20),bg='cadetblue2')
    doctorid.place(x=110,y=320)
    
    entry_doctordepartment=Entry(rootadddoctors, textvariable=doctordepartment_var,font=('times new roman',20))
    entry_doctordepartment.place(x=360,y=110)
    entry_doctorname=Entry(rootadddoctors, textvariable=nameofdoctor_var,font=('times new roman',20))
    entry_doctorname.place(x=360,y=180)
    entry_doctoraddress=Entry(rootadddoctors, textvariable=doctoraddress_var,font=('times new roman',20))
    entry_doctoraddress.place(x=360,y=250)
    entry_doctorid=Entry(rootadddoctors , font=('times new roman',20))
    entry_doctorid.place(x=360,y=320)
    
    insert2= Button(rootadddoctors,text="INSERT" ,font=('times new roman',20),command=entry)
    insert2.place(x=200,y=400)
    backadddoctors=Button(rootadddoctors,text="BACK",font=('times new roman',20),command=rootadddoctors.destroy)
    backadddoctors.place(x=400,y=400)
    
def deletedoctorwindow():
    rootdeletedoctor=Tk()
    rootdeletedoctor.geometry("720x480")
    rootdeletedoctor.configure(bg='cadetblue2')
    rootdeletedoctor.title("DELETE DOCTORS")
    title=Label(rootdeletedoctor, text="DELETE DOCTOR DATA", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def delete1():
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("delete from add_doctors where doctorid= '"+ entry_doctorid.get() +"'")
            cursor.execute("commit");
        
            entry_doctorname.delete(0, 'end')
            entry_doctorid.delete(0, 'end')
            Messagebox.showinfo("Delete Status","Deleted Successfully");
            con.close();  
    
    myLabel1 = Label(rootdeletedoctor, text = " NOTE : DoctorID entry is mandatory for delete",font=('Times New Roman',20),bg='cadetblue2')        
    myLabel1.place(x=70,y=100)
    
    doctorname=Label(rootdeletedoctor, text="NAME OF DOCTOR",font=('times new roman',20),bg='cadetblue2')
    doctorname.place(x=60,y=170)
    doctorid=Label(rootdeletedoctor, text="DOCTOR ID",font=('times new roman',20),bg='cadetblue2')
    doctorid.place(x=100,y=280)
        
    entry_doctorname=Entry(rootdeletedoctor, textvariable=nameofdoctor_var,font=('times new roman',20))
    entry_doctorname.place(x=327,y=170)
    entry_doctorid=Entry(rootdeletedoctor , font=('times new roman',20))
    entry_doctorid.place(x=327,y=280)
        
    delete1=Button(rootdeletedoctor,text="DELETE",font=('times new roman',23),command=delete1)
    delete1.place(x=180,y=370)
    backdeletedoctor=Button(rootdeletedoctor, text="BACK",font=('times new roman',23), command=rootdeletedoctor.destroy)
    backdeletedoctor.place(x=400,y=380)

def displaydoctorwindow():
    rootdisplaydoctor=Tk()
    rootdisplaydoctor.geometry("820x480")
    rootdisplaydoctor.configure(bg='cadetblue2')    
    rootdisplaydoctor.title(" PATIENTS DATA ")
    title=Label(rootdisplaydoctor, text="DOCTORS DATA", font=('bold',30),bg='cadetblue2')
    title.pack()

    con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
    cursor=con.cursor()
    cursor.execute("select * from add_doctors")
    rows=cursor.fetchall();

    frm1=Frame(rootdisplaydoctor)
    frm1.pack(side=tk.LEFT,padx=20)
    
    tv1=ttk.Treeview(frm1,columns=(1,2,3,4),show="headings",height="5")
    tv1.pack()
    
    tv1.heading(1, text="Doctor_Department")
    tv1.heading(2, text="DoctorName")
    tv1.heading(3, text="DoctorAddress")
    tv1.heading(4, text="DoctorID")    

    for i in rows:
       tv1.insert('',  'end',values=i)
    
def bookappointmentwindow():
    rootbookappointment=Tk()
    rootbookappointment.geometry("720x480")
    rootbookappointment.configure(bg='cadetblue2')
    rootbookappointment.title("BOOK AN APPOINTMENT")
    title=Label(rootbookappointment, text="BOOK AN APPOINTMENT", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def entry1():
        
        patientname=entry_patientname.get();
        patientage=entry_patientage.get();
        patientgender=entry_patientgender.get();
        patientaddress=entry_patientaddress.get();
        
        if (patientname=="" or patientage=="" or patientgender=="" or patientaddress==""):
            Messagebox.showinfo("Insert status","All the fields must be filled")
            
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("insert into bookappointment values ('"+ patientname +"','"+ patientage +"','"+ patientgender +"','"+ patientaddress +"')")
            cursor.execute("commit");
                        
            entry_patientname.delete(0, 'end')
            entry_patientage.delete(0, 'end')
            entry_patientgender.delete(0, 'end')
            entry_patientaddress.delete(0, 'end')
        
            Messagebox.showinfo("Insert Status","Inserted Successfully");
            con.close();   
    
    patientname=Label(rootbookappointment, text="PATIENT NAME",font=('times new roman',20),bg='cadetblue2')
    patientname.place(x=70,y=110)
    patientage=Label(rootbookappointment, text="PATIENT AGE",font=('times new roman',20),bg='cadetblue2')
    patientage.place(x=80,y=180)
    patientgender=Label(rootbookappointment, text="PATIENT GENDER",font=('times new roman',20),bg='cadetblue2')
    patientgender.place(x=55,y=250)
    patientaddress=Label(rootbookappointment, text="PATIENT ADDRESS",font=('times new roman',20),bg='cadetblue2')
    patientaddress.place(x=50,y=320)

    entry_patientname=Entry(rootbookappointment, textvariable=patientname_var,font=('times new roman',20))
    entry_patientname.place(x=320,y=110)
    entry_patientage=Entry(rootbookappointment, textvariable=patientage_var,font=('times new roman',20))
    entry_patientage.place(x=320,y=180)
    entry_patientgender=Entry(rootbookappointment, textvariable=patientgender_var,font=('times new roman',20))
    entry_patientgender.place(x=320,y=250)
    entry_patientaddress=Entry(rootbookappointment, textvariable=patientaddress_var,font=('times new roman',20))
    entry_patientaddress.place(x=320,y=320)
    
    insert3= Button(rootbookappointment,text="INSERT" ,font=('times new roman',20),command=entry1)
    insert3.place(x=200,y=400)
    backbookappointment=Button(rootbookappointment,text="BACK",font=('times new roman',20),command=rootbookappointment.destroy)
    backbookappointment.place(x=400,y=400)
    
def displayappointment():
    rootdisplayappointment=Tk()
    rootdisplayappointment.geometry("820x480")
    rootdisplayappointment.configure(bg='cadetblue2')   
    rootdisplayappointment.title(" BOOKED APPOINTMENTS ")
    title=Label(rootdisplayappointment, text="BOOKED APPOINTMENTS", font=('times new roman',30),bg='cadetblue2')
    title.pack()

    con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
    cursor=con.cursor()
    cursor.execute("select * from bookappointment")
    rows=cursor.fetchall();

    frm2=Frame(rootdisplayappointment)
    frm2.pack(side=tk.LEFT,padx=20)
    
    tv2=ttk.Treeview(frm2,columns=(1,2,3,4),show="headings",height="5")
    tv2.pack()
    
    tv2.heading(1, text="PatientName")
    tv2.heading(2, text="PatientAge")
    tv2.heading(3, text="PatientGender")
    tv2.heading(4, text="PatientAddress")    

    for i in rows:
       tv2.insert('',  'end',values=i)
    
def pharmacymodewindow():
    rootpharmacymode=Tk()
    rootpharmacymode.geometry("720x480")
    rootpharmacymode.configure(bg='cadetblue2')
    rootpharmacymode.title("PHARMACY")
    title=Label(rootpharmacymode, text="PHARMACY", font=('bold',40),bg='cadetblue2')
    title.pack()
    
    additem=Button(rootpharmacymode, text="ADD NEW ITEM",font=('times new roman',21), command=additemswindow)
    additem.place(x=250,y=80)
    edititem=Button(rootpharmacymode,text="EDIT ITEM",font=('times new roman',21),command=edititemwindow)
    edititem.place(x=275,y=160)
    displayitems=Button(rootpharmacymode, text="DISPLAY ITEMS",font=('times new roman',21),command=displayitemwindow)
    displayitems.place(x=245,y=240)
    deleteitem=Button(rootpharmacymode, text="DELETE ITEM",font=('times new roman',21),command=deleteitemwindow)
    deleteitem.place(x=250,y=320)
    backpharmacymode=Button(rootpharmacymode, text="BACK",font=('times new roman',21), command=rootpharmacymode.destroy)
    backpharmacymode.place(x=300,y=400)
    
def additemswindow():
    rootadditems=Tk()
    rootadditems.geometry("720x480")
    rootadditems.configure(bg='cadetblue2')
    rootadditems.title("ADD NEW ITEM")
    title=Label(rootadditems, text="ADD NEW ITEM", font=('times new roman',40),bg='cadetblue2')
    title.pack()
    
    def insertadditems():
        itemname=entry_itemname.get();
        itemprice=entry_itemprice.get();
        itemquantity=entry_itemquantity.get();
        itemcategory=entry_itemcategory.get();
        
        if (itemname=="" or itemprice=="" or itemquantity=="" or itemcategory=="" ):
            Messagebox.showinfo("Insert status","All the fields must be filled")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("insert into additems values ('"+ itemname +"','"+ itemprice +"','"+ itemquantity +"','"+ itemcategory +"')")
            cursor.execute("commit");
        
            entry_itemname.delete(0, 'end')
            entry_itemprice.delete(0, 'end')
            entry_itemquantity.delete(0, 'end')
            entry_itemcategory.delete(0, 'end')
                        
            Messagebox.showinfo("Insert Status","Inserted Successfully");
            con.close();     
        
    itemname=Label(rootadditems, text="ITEM NAME",font=('times new roman',20),bg='cadetblue2')
    itemname.place(x=80,y=80)
    itemprice=Label(rootadditems, text="ITEM PRICE",font=('times new roman',20),bg='cadetblue2')
    itemprice.place(x=80,y=160)
    itemquantity=Label(rootadditems, text="ITEM QUANTITY",font=('times new roman',20),bg='cadetblue2')
    itemquantity.place(x=55,y=240)
    itemcategory=Label(rootadditems, text="ITEM CATEGORY",font=('times new roman',20),bg='cadetblue2')
    itemcategory.place(x=50,y=320)    
    
    entry_itemname=Entry(rootadditems,  font=('times new roman',20))
    entry_itemname.place(x=330,y=80)
    entry_itemprice=Entry(rootadditems,  font=('times new roman',20))
    entry_itemprice.place(x=330,y=160)
    entry_itemquantity=Entry(rootadditems,  font=('times new roman',20))
    entry_itemquantity.place(x=330,y=240)
    entry_itemcategory=Entry(rootadditems,  font=('times new roman',20))
    entry_itemcategory.place(x=330,y=320)    
   
    insertadditems=Button(rootadditems,text="INSERT", font=("times new roman",20) , command=insertadditems)
    insertadditems.place(x=200,y=400)
    backadditems=Button(rootadditems, text="BACK",font=('times new roman',20), command=rootadditems.destroy)
    backadditems.place(x=400,y=400)
    
def displayitemwindow():
    rootdisplayitem=Tk()
    rootdisplayitem.geometry("820x480")
    rootdisplayitem.configure(bg='cadetblue2')
    rootdisplayitem.title("DISPLAY ITEMS")
    title=Label(rootdisplayitem, text="RECORDS OF ITEMS", font=('times new roman',40),bg='cadetblue2')
    title.pack()
    
    con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
    cursor=con.cursor()
    cursor.execute("select * from additems")
    rows=cursor.fetchall();

    frm1=Frame(rootdisplayitem)
    frm1.pack(side=tk.LEFT,padx=20)
    
    tv1=ttk.Treeview(frm1,columns=(1,2,3,4),show="headings",height="5")
    tv1.pack()
    
    tv1.heading(1, text="Item_Name")
    tv1.heading(2, text="Item_Price")
    tv1.heading(3, text="Item_Quantity")
    tv1.heading(4, text="Item_Category")    

    for i in rows:
       tv1.insert('',  'end',values=i)

def deleteitemwindow():
    rootdeleteitem=Tk()
    rootdeleteitem.geometry("720x480")
    rootdeleteitem.configure(bg='cadetblue2')
    rootdeleteitem.title("DELETE ITEMS")
    title=Label(rootdeleteitem,text="DELETE ITEMS", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def delete():
        
        if (entry_itemname.get() ==""):
            Messagebox.showinfo("Delete status","Itemname column is mandatory for delete option")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("delete from additems where itemname= '"+ entry_itemname.get() +"'")
            cursor.execute("commit");
            entry_itemname.delete(0, 'end')
            
            Messagebox.showinfo("Delete Status","Deleted Successfully");
            con.close();
                    
    itemcategory=Label( rootdeleteitem, text="ITEM NAME",font=('times new roman',22))
    itemcategory.place(x=80,y=100)
    itemname=Label( rootdeleteitem, text="ITEM CATEGORY",font=('times new roman',22))
    itemname.place(x=50,y=250)
     
    entry_itemname=Entry( rootdeleteitem, font=('times new roman',22))
    entry_itemname.place(x=340,y=100)
    entry_itemcategory=Entry( rootdeleteitem, font=('times new roman',22))
    entry_itemcategory.place(x=340,y=250)
    
    delete=Button( rootdeleteitem,text="DELETE",font=('times new roman',23),command=delete)
    delete.place(x=200,y=350) 
    backdeleteitem=Button(rootdeleteitem, text="BACK",font=('times new roman',23),command=rootdeleteitem.destroy)
    backdeleteitem.place(x=400,y=350)
    
def editpatientwindow():
    rooteditpatient=Tk()
    
    def update():
        patientid=entry_patientid.get();
        patientname=entry_patientname.get();
        patientage=entry_patientage.get();
        patientgender=entry_patientgender.get();
        doctorname=entry_doctorname.get();
        patientdepartment=entry_patientdepartment.get();
        patientaddress=entry_patientaddress.get();                    
    
        con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
        cursor=con.cursor()
        cursor.execute("update addpatients set patdep='"+ patientdepartment +"',docname='"+ doctorname +"',pname='"+ patientname +"',page='"+ patientage +"',pgen='"+ patientgender +"',padd='"+ patientaddress +"' where pid='"+ patientid +"'")
        cursor.execute("commit");
        
        entry_patientdepartment.delete(0, 'end')
        entry_doctorname.delete(0, 'end')
        entry_patientname.delete(0, 'end')
        entry_patientage.delete(0, 'end')
        entry_patientgender.delete(0, 'end')
        entry_patientaddress.delete(0, 'end')
        entry_patientid.delete(0, 'end')
        
        Messagebox.showinfo("update Status","updated Successfully");
        con.close();
        
    def get():
            if (entry_patientid.get()==""):
                Messagebox.showinfo("Fetch status","Patient Id column should be filled")
            else:
                con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
                cursor=con.cursor()
                cursor.execute("select * from addpatients where pid='"+ entry_patientid.get() +"'")
                rows=cursor.fetchall()
            
                for row in rows:
                    entry_patientname.insert(0, row[2])
                    entry_patientage.insert(0, row[3])
                    entry_patientgender.insert(0, row[4])
                    entry_doctorname.insert(0, row[1])
                    entry_patientdepartment.insert(0, row[0])
                    entry_patientaddress.insert(0, row[5])
                    
            con.close();
        
        
    rooteditpatient.geometry("720x480")
    rooteditpatient.configure(bg='cadetblue2')
    rooteditpatient.title("EDIT PATIENT DATA")
    title=Label(rooteditpatient,text="EDIT PATIENT DATA", font=('bold',30),bg='cadetblue2')
    title.pack()

    patientid=Label(rooteditpatient, text="PATIENT ID",font=('times new roman',17))
    patientid.place(x=70,y=80)
    patientname=Label(rooteditpatient, text="PATIENT NAME",font=('times new roman',17))
    patientname.place(x=70,y=127)
    patientage=Label(rooteditpatient, text="PATIENT AGE",font=('times new roman',17))
    patientage.place(x=70,y=180)
    patientgender=Label(rooteditpatient, text="PATIENT GENDER",font=('times new roman',17))
    patientgender.place(x=70,y=227)
    doctorname=Label(rooteditpatient, text="NAME OF DOCTOR",font=('times new roman',17))
    doctorname.place(x=70,y=280)    
    patientdepartment=Label(rooteditpatient, text="PATIENT DEPARTMENT",font=('times new roman',17))
    patientdepartment.place(x=70,y=327)
    patientaddress=Label(rooteditpatient, text="PATIENT ADDRESS",font=('times new roman',17))
    patientaddress.place(x=70,y=380)
        
    entry_patientid=Entry(rooteditpatient, textvariable=patientroomnumber_var,font=('times new roman',17))
    entry_patientid.place(x=400,y=80)
    entry_patientname=Entry(rooteditpatient, textvariable=patientname_var,font=('times new roman',17))
    entry_patientname.place(x=400,y=127)
    entry_patientage=Entry(rooteditpatient, textvariable=patientage_var,font=('times new roman',17))
    entry_patientage.place(x=400,y=180)
    entry_patientgender=Entry(rooteditpatient, textvariable=patientgender_var,font=('times new roman',17))
    entry_patientgender.place(x=400,y=227)
    entry_doctorname=Entry(rooteditpatient, textvariable=nameofdoctor_var,font=('times new roman',17))
    entry_doctorname.place(x=400,y=280)
    entry_patientdepartment=Entry(rooteditpatient, textvariable=patientdepartment_var,font=('times new roman',17))
    entry_patientdepartment.place(x=400,y=327)
    entry_patientaddress=Entry(rooteditpatient, textvariable=patientaddress_var,font=('times new roman',17))
    entry_patientaddress.place(x=400,y=380)
    
    edit=Button(rooteditpatient,text="EDIT",font=('times new roman',17),command=update)
    edit.place(x=200,y=420)
    get1=Button(rooteditpatient,text="GET",font=('times new roman',17),command=get)
    get1.place(x=300,y=420)
    backeditpatient=Button(rooteditpatient,text="BACK",font=('times new roman',17),command=rooteditpatient.destroy)
    backeditpatient.place(x=400,y=420)

    
def editdoctorwindow():
    rooteditdoctor=Tk()
    rooteditdoctor.geometry("720x480")
    rooteditdoctor.configure(bg='cadetblue2')
    rooteditdoctor.title("EDIT DOCTOR DATA")
    title=Label(rooteditdoctor,text="EDIT DOCTOR DATA", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def update1():
        doctordepartment=entry_doctordepartment.get();
        doctorname=entry_doctorname.get();
        doctoraddress=entry_doctoraddress.get();
        doctorid=entry_doctorid.get();
        
        if (doctorid==""):
            Messagebox.showinfo("Update status","DoctorID column must be filled")
        
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("update add_doctors set doctordepartment='"+ doctordepartment +"',doctorname='"+ doctorname +"',doctoraddress='"+ doctoraddress +"' where doctorid='"+ doctorid +"'")
            cursor.execute("commit");
        
            entry_doctordepartment.delete(0, 'end')
            entry_doctorname.delete(0, 'end')
            entry_doctoraddress.delete(0, 'end')
            entry_doctorid.delete(0, 'end')
          
            Messagebox.showinfo("Update Status","Updated Successfully");
            con.close();
     
    def get1():
        if (entry_doctorid.get()==""):
                Messagebox.showinfo("Fetch status","Doctor Id column should be filled")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("select * from add_doctors where doctorid= '"+ entry_doctorid.get() +"'")
            rows=cursor.fetchall()
            
            for row in rows:
                    entry_doctordepartment.insert(0, row[0])
                    entry_doctoraddress.insert(0, row[2])
                    entry_doctorname.insert(0, row[1])                   
                    
            con.close();  
    
    doctordepartment=Label(rooteditdoctor, text="DOCTOR DEPARTMENT",font=('times new roman',20))
    doctordepartment.place(x=50,y=110)
    doctorname=Label(rooteditdoctor, text="NAME OF DOCTOR",font=('times new roman',20))
    doctorname.place(x=70,y=180)
    doctoraddress=Label(rooteditdoctor, text="DOCTOR ADDRESS",font=('times new roman',20))
    doctoraddress.place(x=70,y=250)
    doctorid=Label(rooteditdoctor, text="DOCTOR ID",font=('times new roman',20))
    doctorid.place(x=110,y=320)
    
    entry_doctordepartment=Entry(rooteditdoctor, textvariable=doctordepartment_var,font=('times new roman',20))
    entry_doctordepartment.place(x=360,y=110)
    entry_doctorname=Entry(rooteditdoctor, textvariable=nameofdoctor_var,font=('times new roman',20))
    entry_doctorname.place(x=360,y=180)
    entry_doctoraddress=Entry(rooteditdoctor, textvariable=doctoraddress_var,font=('times new roman',20))
    entry_doctoraddress.place(x=360,y=250)
    entry_doctorid=Entry(rooteditdoctor , font=('times new roman',20))
    entry_doctorid.place(x=360,y=320)
    
    insert5= Button(rooteditdoctor,text="EDIT" ,font=('times new roman',20),command=update1)
    insert5.place(x=200,y=400)
    get2=Button(rooteditdoctor,text="GET",font=('times new roman',20),command=get1)
    get2.place(x=300,y=400)
    backeditdoctor=Button(rooteditdoctor,text="BACK",font=('times new roman',20),command=rooteditdoctor.destroy)
    backeditdoctor.place(x=400,y=400)    
    
def edititemwindow():
    rootedititem=Tk()
    rootedititem.geometry("720x480")
    rootedititem.configure(bg='cadetblue2')
    rootedititem.title("EDIT ITEM DATA")
    title=Label(rootedititem,text="EDIT ITEM DATA", font=('bold',30),bg='cadetblue2')
    title.pack()
    
    def update3():
        itemname=entry_itemname.get();
        itemprice=entry_itemprice.get();
        itemquantity=entry_itemquantity.get();
        itemcategory=entry_itemcategory.get();
        
        if (itemname==""):
            Messagebox.showinfo("Update status","Itemname must be filled")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("update additems set itemcategory='"+ itemcategory +"',itemprice='"+ itemprice +"',itemquantity='"+ itemquantity +"' where itemname='"+ itemname +"'")
            cursor.execute("commit");
        
            entry_itemname.delete(0, 'end')
            entry_itemprice.delete(0, 'end')
            entry_itemquantity.delete(0, 'end')
            entry_itemcategory.delete(0, 'end')
                        
            Messagebox.showinfo("Update Status","Updated Successfully");
            con.close();
            
    def get4():
        
        if (entry_itemname.get() ==""):
            Messagebox.showinfo("Update status","Itemname column is mandatory for edit option")
        else:
            con=mysql.connect(host="localhost", user="root", password="root", database="projhm")
            cursor=con.cursor()
            cursor.execute("select * from additems where itemname= '"+ entry_itemname.get() +"'")
            rows=cursor.fetchall()
            
            for row in rows:
                entry_itemprice.insert(0, row[1])
                entry_itemcategory.insert(0, row[3])
                entry_itemquantity.insert(0, row[2])
                    
            con.close();        
            
    itemname=Label(rootedititem, text="ITEM NAME",font=('times new roman',20))
    itemname.place(x=80,y=80)
    itemprice=Label(rootedititem, text="ITEM PRICE",font=('times new roman',20))
    itemprice.place(x=80,y=160)
    itemquantity=Label(rootedititem, text="ITEM QUANTITY",font=('times new roman',20))
    itemquantity.place(x=55,y=240)
    itemcategory=Label(rootedititem, text="ITEM CATEGORY",font=('times new roman',20))
    itemcategory.place(x=50,y=320)    
    
    entry_itemname=Entry(rootedititem,font=('times new roman',20))
    entry_itemname.place(x=330,y=80)
    entry_itemprice=Entry(rootedititem,font=('times new roman',20))
    entry_itemprice.place(x=330,y=160)
    entry_itemquantity=Entry(rootedititem,font=('times new roman',20))
    entry_itemquantity.place(x=330,y=240)
    entry_itemcategory=Entry(rootedititem,font=('times new roman',20))
    entry_itemcategory.place(x=330,y=320)
    
    edititem=Button(rootedititem,text="EDIT", font=("times new roman",20),command=update3)
    edititem.place(x=200,y=400)
    get3=Button(rootedititem,text="GET",font=('times new roman',20),command=get4)
    get3.place(x=300,y=400)
    backedititem=Button(rootedititem, text="BACK",font=('times new roman',20), command=rootedititem.destroy)
    backedititem.place(x=400,y=400)
      
def listofdoctorswindow():
    rootlistofdoctors=Tk()
    
    frame=Frame(rootlistofdoctors,height=500,width=500,bg='cadetblue2')
    frame.pack()
    
    l=["Dr. sharma","Dr. Verma","Dr. Kumar","Dr. Khan","Dr. Kohli","Dr. singh","Dr. Sidharth","Dr. tendulkar","Dr. Virat","Dr. Leo",'Dr. Irfan','Dr. John',
       'Dr. Sanjay','Dr. Shahid']
    m=["Orthopaedic surgeon","Orthopaedic surgeon","Nephrologist","Nephrologist","Gynaecologist","Gynaecologist","Physician","Physician","Neurologist",
       "Neurologist",'X-ray','X-ray','X-ray','X-ray']
    n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    l1=Label(rootlistofdoctors,text='NAME OF DOCTORS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(rootlistofdoctors,text=i)
       l.place(x=20,y=count)

    l2=Label(rootlistofdoctors,text='DEPARTMENT')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(rootlistofdoctors,text=i)
       l3.place(x=140,y=count1)

    l4=Label(rootlistofdoctors,text='ROOM NO')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(rootlistofdoctors,text=i)
       l5.place(x=260,y=count2)
    rootlistofdoctors.resizable(False,False)
    rootlistofdoctors.mainloop()

def servicesavailablewindow():    
    rootservicesavailable=Tk()
    frame=Frame(rootservicesavailable,height=500,width=500,bg='cadetblue2')
    frame.pack()
    l1=Label(rootservicesavailable,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    f=["ULTRASOUND","X-RAY","CT Scan","MRI","BLOOD COLLECTION","DIALYSIS","ECG","CHEMIST","LAB"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(rootservicesavailable,text=i)
       l3.place(x=20,y=count1)
    l2=Label(rootservicesavailable,text='ROOM NO.')
    l2.place(x=140,y=10)
    g=[1,2,3,4,5,6,7,8,9]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(rootservicesavailable,text=i)
       l4.place(x=140,y=count2)
    l5=Label(rootservicesavailable,text='To avail any of these please contact on our no.:- 7042****55')
    l5.place(x=20,y=240)
    rootservicesavailable.resizable(False,False)
    rootservicesavailable.mainloop()    
    

root=Tk()
root.geometry("720x480")
root.title("COMPUTER SCIENCE PROJECT")
title=Label(root,text = "HOSPITAL DIGITALIZATION",font=('times new roman',38))
title.pack()
backgroundimage=ImageTk.PhotoImage(Image.open("C:\\Users\\admin\\Desktop\\project image.jpeg"))
imagelabel=Label(image=backgroundimage)
imagelabel.pack()
  
admin=Button(root, text="ADMIN", font=('times new roman',23),bg='cadetblue2', command=adminmodewindow)
admin.place(x=510,y=100)
pharmacy=Button(root, text="PHARMACY", font=('times new roman',23),bg='cadetblue2', command=pharmacymodewindow)
pharmacy.place(x=470,y=220) 
quitmodes=Button(root, text="QUIT", font=('times new roman',23),bg='cadetblue2', command=root.destroy)
quitmodes.place(x=520,y=350) 

patientdepartment_var=StringVar()
nameofdoctor_var=StringVar()
patientname_var=StringVar()
patientage_var=StringVar()
patientgender_var=StringVar()
patientaddress_var=StringVar()
patientroomnumber_var=StringVar()
doctordepartment_var=StringVar()
doctoraddress_var=StringVar()
itemprice_var=StringVar()
itemquatity_var=StringVar()
itemcategory_var=StringVar() 
itemname_var=StringVar() 
itemcategory_var=StringVar()
doctorname_var=StringVar()
doctorid_var=StringVar()

root.mainloop()
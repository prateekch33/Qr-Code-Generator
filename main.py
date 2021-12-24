from tkinter import*
import qrcode as qc
from PIL import Image,ImageTk
from resizeimage import resizeimage as rimg

class QR_Generator:
    def __init__(self,root):
        # Top Header
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed by Prateek")
        self.root.resizable(False,False)

        # Heading Panel
        title=Label(self.root,text="Qr Code Generator", font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

        # Variables
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        # Frame 1
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Employee Details", font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        # Labels
        lbl_emp_code=Label(emp_Frame,text="Employee ID", font=("goudy old style",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Name", font=("goudy old style",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(emp_Frame,text="Department", font=("goudy old style",15,'bold'),bg='white').place(x=20,y=140)
        lbl_designation=Label(emp_Frame,text="Designation", font=("goudy old style",15,'bold'),bg='white').place(x=20,y=180)


        # Inputs
        txt_emp_code=Entry(emp_Frame,text="Employee ID", font=("goudy old style",15),bg='lightyellow',textvariable=self.var_emp_code).place(x=200,y=60)
        txt_name=Entry(emp_Frame,text="Name", font=("goudy old style",15),bg='lightyellow',textvariable=self.var_name).place(x=200,y=100)
        txt_department=Entry(emp_Frame,text="Department", font=("goudy old style",15),bg='lightyellow',textvariable=self.var_department).place(x=200,y=140)
        txt_designation=Entry(emp_Frame,text="Designation", font=("goudy old style",15),bg='lightyellow',textvariable=self.var_designation).place(x=200,y=180)

        # Buttons
        btn_generate=Button(emp_Frame,text="Generate",command=self.generate,font=("time new roman",18,'bold'),bg='#2196f3',fg='white').place(x=60,y=240,width=200,height=30)
        btn_clear=Button(emp_Frame,text="Clear",font=("time new roman",18,'bold'),bg='#607d8b',fg='white',command=self.clear).place(x=286,y=240,width=120,height=30)

        # Answer Field
        self.msg=''
        self.label_msg=Label(emp_Frame,text=self.msg, font=("goudy old style",15),bg='white',fg='green')
        self.label_msg.place(x=0,y=320,relwidth=1)

        # Field 2
        QR_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        QR_Frame.place(x=600,y=100,width=250,height=380)
        QR_title=Label(QR_Frame,text="Employee QR Code", font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        # QR Code Image Part
        self.qr_code=Label(QR_Frame,text='QR Code\nNot Available', font=('times new roman',15),bg='#3f51b5',fg='white')
        self.qr_code.place(x=35,y=100,width=180,height=180)

    # CLear Button Backend
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.label_msg.config(text=self.msg)
        self.qr_code.config(image='')

    # Generate Button Backend
    def generate(self):
        if(self.var_designation.get()=='' or self.var_department.get()=='' or self.var_emp_code.get()=='' or self.var_name.get()==''):
            self.msg='All Filds are Required!!'
            self.label_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEnployee Name: {self.var_name.get()}\nDesignation: {self.var_designation.get()}\nDepartment: {self.var_department.get()}")
            qr_code=qc.make(qr_data)
            # print(qr_code)
            qr_code=rimg.resize_cover(qr_code,[180,180])
            qr_code.save('QR Code/Emp_'+str(self.var_emp_code.get())+'.png')
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            self.msg='QR Generated Successfully!!'
            self.label_msg.config(text=self.msg,fg='green')
            

root=Tk()
obj=QR_Generator(root)
root.mainloop()
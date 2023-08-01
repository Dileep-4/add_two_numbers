from tkinter import*
import tkinter.messagebox
top=Tk()
top.title("Entry Widget Validation")
top.geometry("125x325+100+50")
top.configure(bg="#c0ded9")
Mainframe=Frame(top,bd=10)
Mainframe.grid()
Tops=Frame(Mainframe,bd=10,width=100,height=350,relief=RIDGE)
Tops.pack(side=TOP)
top.lblInfo=Label(Tops,font=("helvetica",31,"bold"),text="Validate Entry Widget",justify=CENTER,bg="white")
top.lblInfo.grid(padx=2)
MembersName_F=LabelFrame(Mainframe,bd=10,width=466,height=200,font=("Helvetica",12,"bold"),text="Customer Name",relief=RIDGE)
MembersName_F.pack(side=TOP)
Reciept_ButtonFrame=LabelFrame(Mainframe,bd=10,width=466,height=80,font=("Helvetica",12,"bold"),text="Details",relief=RIDGE)
Reciept_ButtonFrame.pack(side=BOTTOM)
NumOne=StringVar()
NumTwo=StringVar()
Answer=StringVar()
top.lblNumOne=Label(MembersName_F,font=("Helvetica",16,"bold"),text="Number One",bd=7)
top.lblNumOne.grid(row=0,column=0,sticky=W)
top.txtNumOne=Entry(MembersName_F,font=("Helvetica",13,"bold"),bd=7,textvariable=NumOne,width=34)
top.txtNumOne.grid(row=0,column=1)
top.lblNumTwo=Label(MembersName_F,font=("Helvetica",16,"bold"),text="Number Two",bd=7)
top.lblNumTwo.grid(row=1,column=0,sticky=W)
top.txtNumTwo=Entry(MembersName_F,font=("Helvetica",13,"bold"),bd=7,textvariable=NumTwo,width=34)
top.txtNumTwo.grid(row=1,column=1)
top.lblAnswer=Label(MembersName_F,font=("Helvetica",16,"bold"),text="Answer",bd=7)
top.lblAnswer.grid(row=2,column=0,sticky=W)
top.txtAnswer=Entry(MembersName_F,font=("Helvetica",13,"bold"),bd=7,textvariable=Answer,width=34,state=DISABLED)
top.txtAnswer.grid(row=2,column=1)
def Reset():
    NumOne.set("")
    NumTwo.set("")
    Answer.set("")
    return
def iExit():
    iExit=tkinter.messagebox.askyesno("Validate Entry Widget","Confirm if you want to exit")
    if iExit>0:
        top.destroy()
        return
def numberOnly():
        Item1=(NumOne.get())
        Item2=(NumTwo.get())
        if (Item1.isdigit() or Item2.isdigit()):
            Item3=int(Item1) +int(Item2)
            Answer.set(Item3)
            tkinter.messagebox.showinfo("correct Data","Well done")
            return True
        else:
            tkinter.messagebox.showwarning("wrong Data","invalid data,Please enter Numbers only")
            NumOne.set("")
            NumTwo.set("")
            Answer.set("")
            return False
top.btnValidate=Button(Reciept_ButtonFrame,padx=18,bd=7,font=("helvetica",16,"bold"),width=7,text="Validate",command=numberOnly,bg="grey").grid(row=2,column=0,pady=12)
top.btnReset=Button(Reciept_ButtonFrame,padx=18,bd=7,font=("helvetica",16,"bold"),width=7,text="Reset",command=Reset,bg="grey").grid(row=2,column=1,pady=12)
top.btnExit=Button(Reciept_ButtonFrame,padx=18,bd=7,font=("helvetica",16,"bold"),width=7,text="Exit",command=iExit,bg="grey").grid(row=2,column=3,pady=12)
top.mainloop()

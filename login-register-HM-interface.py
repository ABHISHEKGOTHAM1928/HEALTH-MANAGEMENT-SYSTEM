from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tempfile
import os
#1.IMPORTED ALL NECESSARY MODULES:
#pip install pillow
#pip install mysql-connector-python

#2. at last of the code i have called main
#3.creating main by making login class as main
def main():
    win=Tk()
    app=login(win)
    win.mainloop()
#=======================================================================================================================
#====================================REGISTER AND LOGIN INTO MAIN PROJECT===============================================
#=======================================================================================================================

#===============================================LOGIN WINDOW============================================================
#created ------>class login
class login:                         #WE HAVE CREATED AN OBJECT "CLASS"
    def __init__(self,root):         #DEF---FUNCTION
        self.root=root
        self.root.title("LOGIN AND REGISTRATION WINDOW")
        self.root.geometry("1550x800+0+0")
        #self.root.resizable(False,False)
        self.loginform()
# defined----->loginform for creating login module
    def loginform(self):
        self.bg = ImageTk.PhotoImage(Image.open("pencil5.png"))
        bg_label = Label(self.root, image=self.bg)
        bg_label.image = self.bg
        bg_label.pack(side=TOP, fill=X)

        # for black frame for bg:
        frame = Frame(self.root, bg="black", bd=6, relief=RIDGE)
        frame.place(x=600, y=200, width=360, height=450)
        # for icon on top
        bg2 = ImageTk.PhotoImage(Image.open("LoginIconAppl1.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label1 = Label(frame, image=bg2, bg="black", padx=5)
        bg_label1.image = bg2
        bg_label1.place(x=130, y=15)
        # for subtitle:

        welcome = Label(frame, text="LETS BEGIN", font=("times new roman", 15, "bold"), fg="white", bg="black")
        welcome.place(x=115, y=90)
        # for username:
        username = Label(frame, text="USER NAME", font=("Franklin Gothic Heavy", 12), fg="white", bg="black")
        username.place(x=76, y=130)
        # for username field:
        self.txtuser = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtuser.place(x=50, y=160, width=250)
        # for password:
        password = Label(frame, text="PASS WORD", font=("Franklin Gothic Heavy", 12), fg="white", bg="black")
        password.place(x=80, y=200)
        # for password field:
        self.txtpassword = ttk.Entry(frame, show="*", font=("times new roman", 12, "bold"))
        self.txtpassword.place(x=50, y=230, width=250)
        # for username icon:
        bg3 = ImageTk.PhotoImage(Image.open("login2.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label3 = Label(frame, image=bg3, bg="black")
        bg_label3.image = bg3
        bg_label3.place(x=45, y=125)
        # for password icon:
        bg4 = ImageTk.PhotoImage(Image.open("password1.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label4 = Label(frame, image=bg4, bg="black")
        bg_label4.image = bg4
        bg_label4.place(x=48, y=190)
        # for login button:
        loginbutton = Button(frame, text="LOGIN",command=self.login ,font=("times new roman", 15, "bold"), bd=3,
                             relief=FLAT, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbutton.place(x=120, y=270, height=30)
        # for register button:
        registerbutton = Button(frame, text="NEW USER REGISTER",command=self.register
                                ,font=("times new roman", 13, "bold"), bd=3, relief=FLAT, fg="white",
                                bg="black", activeforeground="white", activebackground="black")
        registerbutton.place(x=70, y=310, height=20)
#=====================================FUNCTIONS FOR LOGIN BUTTON========================================================
    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get == "":
            messagebox.showerror("Error", "all fields required")
        else:

            conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@99499", database="sakila")
            my_cursor = conn.cursor()
            my_cursor.execute('select * from register where username=%s and password=%s',(
                    self.txtuser.get(),self.txtpassword.get()
                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access for only owners")
                if open_main > 0:
                    self.hospital_window()
                else:
                    if not open_main:
                        return


            conn.commit()
            conn.close()
# CREATING FUNCTION FOR CALLING CLASS HOSPITAL FROM LOGIN BUTTON
    def hospital_window(self):
        self.new_window=Toplevel(self.root)

        self.app = hospital(self.new_window)

#======================================FOR REGISTER WINDOW==============================================================
    def register(self):
        # for REGISTER background
        self.bg = ImageTk.PhotoImage(Image.open("pencil5.png"))
        bg_label = Label(self.root, image=self.bg)
        bg_label.image = self.bg
        bg_label.pack(side=TOP, fill=X)
        # for black frame for bg:
        frame = Frame(self.root, bg="black", bd=6, relief=RIDGE)
        frame.place(x=600, y=200, width=360, height=450)
        # for icon on top
        bg2 = ImageTk.PhotoImage(Image.open("reggg1.png"))
        bg_label1 = Label(frame, image=bg2, bg="black", padx=5)
        bg_label1.image = bg2
        bg_label1.place(x=100, y=0)
        # for username:
        username = Label(frame, text="NEW USER NAME", font=("Franklin Gothic Heavy", 12), fg="white", bg="black")
        username.place(x=76, y=110)
        # for username field:
        self.txtuser = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtuser.place(x=50, y=140, width=250)
        # for password:
        password = Label(frame, text="PASS WORD", font=("Franklin Gothic Heavy", 12), fg="white", bg="black")
        password.place(x=80, y=180)
        # for password field:
        self.txtpassword = ttk.Entry(frame,
                                     font=("times new roman", 12, "bold"))
        self.txtpassword.place(x=50, y=210, width=250)
        # for username icon:
        bg3 = ImageTk.PhotoImage(Image.open("login2.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label3 = Label(frame, image=bg3, bg="black")
        bg_label3.image = bg3
        bg_label3.place(x=45, y=105)
        # for password icon:
        bg4 = ImageTk.PhotoImage(Image.open("password1.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label4 = Label(frame, image=bg4, bg="black")
        bg_label4.image = bg4
        bg_label4.place(x=48, y=175)
        # for confirm password icon:
        bg4 = ImageTk.PhotoImage(Image.open("password1.png"))
        # bg2=bg2.Resize((100,100),Image.ANTIALIAS)
        bg_label4 = Label(frame, image=bg4, bg="black")
        bg_label4.image = bg4
        bg_label4.place(x=48, y=245)
        # for confirm password:
        password = Label(frame, text="CONFIRM PASS WORD", font=("Franklin Gothic Heavy", 12), fg="white", bg="black")
        password.place(x=80, y=250)
        # for confirm password field:
        self.txtpassword2 = ttk.Entry(frame, show="*",
                                      font=("times new roman", 12, "bold"))
        self.txtpassword2.place(x=50, y=280, width=250)
        # for checkbutton
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I AGREE TO YOUR TERMS &CONDITIONS",
                                    font=("times new roman", 10, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=325)
        # ========================BUTTONS==========================
        # for login button:
        loginbutton = Button(frame, text="LOGIN",command=self.loginform ,font=("times new roman", 15, "bold"), bd=3, relief=FLAT,
                             fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbutton.place(x=180, y=370, height=30)
        # for register button:
        registerbutton = Button(frame, command=self.Register, text="REGISTER",
                                font=("times new roman", 13, "bold"), bd=3, relief=FLAT,
                                fg="white",
                                bg="red", activeforeground="white", activebackground="red")
        registerbutton.place(x=70, y=370, height=30)


#CREATING FUNCTION FOR REGISTER BUTTON
    def Register(self):
        if self.txtpassword.get() == "" or self.txtpassword2.get() == "" or self.txtuser.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED")
        elif self.txtpassword.get() != self.txtpassword2.get():
            messagebox.showerror("Error", "PASSWORD AND CONFIRM PASSWORD SHOULD BE SAME")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@99499", database="sakila")
            my_cursor = conn.cursor()
            query = ("select * from register where username=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "USERNAME ALREADY EXISTS,PLEASE TRY SOME DIFFERENT ONE")
            else:
                my_cursor.execute("insert into register values(%s,%s)", (
                    self.txtuser.get(),
                    self.txtpassword.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "REGISTER SUCCESSFULLY")


#creating function for next button
    

# ======================================================================================================================
# ==========================================MAIN PROJECT================================================================
# ======================================================================================================================

class hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("DESIGN_PROJECT_LAB")
        self.root.geometry("1540x800+0+0")
        self.root.iconbitmap('favicon.ico')
        self.PROBLEM1=StringVar()
        self.PROBLEM2=StringVar()
        self.PROBLEM3=StringVar()
        self.PROBLEM4=StringVar()
        self.PROBLEM5=StringVar()
        self.PROBLEM6=StringVar()
        self.PROBLEM7=StringVar()
        self.symptom1=StringVar()
        self.symptom2=StringVar()
        self.symptom3=StringVar()
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HEALTH MANAGEMENT SYSTEM",fg="black",bg="cyan2",font=("Eras Bold ITC",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)




        # from "class hospital: to here is for headings and title


#=======================================================================================================================
#                                          FROT END CODE
#=======================================================================================================================


# ============================FOR TOP FRAME=================================================

#for whole window
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,bg="cyan2")
        Dataframe.place(x=0,y=120,width=1530,height=400)
# for top first section
        Dataframefirst = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                   font=("times new roman", 12, "bold"), text="info")
        Dataframefirst.place(x=15, y=5, width=90, height=350)

#for top second  section
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("times new roman",12,"bold"),text="YOUR SYMPTOMS")
        DataframeLeft.place(x=110,y=5,width=500,height=350   )

#for top third section
        Dataframemiddle= LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                   font=("times new roman", 12, "bold"), text="DO YOU FEEL ANY OF THESE?")
        Dataframemiddle.place(x=620, y=5, width=500, height=350)
#for top fourth section:

        Dataframeright = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                    font=("times new roman", 12, "bold"), text="PRESCRIPTION")
        Dataframeright.place(x=1130, y=5, width=350, height=350)


        # up to here it is for all the sections in top- left,middle and right
# ===============================FOR MIDDLE FRAME===============================================
#for middle left button section
        Buttonframeleft=Frame(self.root,bd=20,relief=RIDGE)

        Buttonframeleft.place(x=0,y=530,width=810,height=70)

# for middle right button section
        Buttonframeright= Frame(self.root, bd=20, relief=RIDGE)
        Buttonframeright.place(x=810, y=530, width=710, height=70)


# ===============================FOR LAST FRAME===============================================

# for down section left
        DetailsframeLeft = Frame(self.root, bd=20, relief=RIDGE)
        DetailsframeLeft.place(x=0, y=600, width=810, height=190)
# for down section right
        DetailsframeRight = Frame(self.root, bd=20, relief=RIDGE)
        DetailsframeRight.place(x=810, y=600, width=710, height=190)

# ================================FOR BUTTONS IN "YOUR PROBLEMS-LABEL"=============================================
        #for problem 1
        lblNameProblem1=Label(DataframeLeft,font=("arial",12,"bold"),text="PROBLEM1:",padx=2,pady=6)
        lblNameProblem1.grid(row=0,column=0,sticky=W)

        comNameProblem1=ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM1,state="readonly",
                                    font=("arial",12,"bold"), width=33)
        comNameProblem1["values"]=(" ","RUNNING NOSE","COUGH","HEADACHE","LIGHT TEMPERATURE","BODY PAINS","STOMACH ACHE","OVER SWEATING")

        comNameProblem1.current(0)
        comNameProblem1.grid(row=0,column=1)
        # for problem 2
        lblNameProblem2 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM2:", padx=2, pady=6)
        lblNameProblem2.grid(row=1, column=0, sticky=W)

        comNameProblem2 = ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM2 ,state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem2["values"] = (" ","RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS", "STOMACH ACHE", "OVER SWEATING")
        comNameProblem2.current(0)
        comNameProblem2.grid(row=1, column=1)
        # for problem 3
        lblNameProblem3 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM3:", padx=2, pady=6)
        lblNameProblem3.grid(row=2, column=0, sticky=W)

        comNameProblem3 = ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM3 ,state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem3["values"] = (" ",
        "RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS", "STOMACH ACHE", "OVER SWEATING")
        comNameProblem3.current(0)
        comNameProblem3.grid(row=2, column=1)
        # for problem 4
        lblNameProblem4 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM4:", padx=2, pady=6)
        lblNameProblem4.grid(row=3, column=0, sticky=W)

        comNameProblem4 = ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM4 ,state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem4["values"] = (" ",
            "RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS", "STOMACH ACHE", "OVER SWEATING")
        comNameProblem4.current(0)
        comNameProblem4.grid(row=3, column=1)
        # for problem 5
        lblNameProblem5 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM5:", padx=2, pady=6)
        lblNameProblem5.grid(row=4, column=0, sticky=W)

        comNameProblem5 = ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM5 ,state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem5["values"] = (" ",
            "RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS", "STOMACH ACHE", "OVER SWEATING")
        comNameProblem5.current(0)
        comNameProblem5.grid(row=4, column=1)
        # for problem 6
        lblNameProblem6 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM6:", padx=2, pady=6)
        lblNameProblem6.grid(row=5, column=0, sticky=W)

        comNameProblem6 = ttk.Combobox(DataframeLeft,textvariable=self.PROBLEM6 ,state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem6["values"] = (" ",
            "RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS", "STOMACH ACHE", "OVER SWEATING")
        comNameProblem6.current(0)
        comNameProblem6.grid(row=5, column=1)
        # for problem 7
        lblNameProblem7 = Label(DataframeLeft, font=("arial", 12, "bold"), text="PROBLEM7:", padx=2, pady=6)
        lblNameProblem7.grid(row=6, column=0, sticky=W)

        comNameProblem7 = ttk.Combobox(DataframeLeft, textvariable=self.PROBLEM7, state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem7["values"] = (" ",
                                    "RUNNING NOSE", "COUGH", "HEADACHE", "LIGHT TEMPERATURE", "BODY PAINS",
                                    "STOMACH ACHE", "OVER SWEATING")
        comNameProblem7.current(0)
        comNameProblem7.grid(row=6, column=1)

        #=================================FOR BUTTONS IN TOP-3==================================================================

        #for symptom1
        lblNamesymptom1= Label(Dataframemiddle, font=("arial", 12, "bold"), text="symptom1:", padx=2, pady=6)
        lblNamesymptom1.grid(row=0, column=0, sticky=W)

        comNameProblem1 = ttk.Combobox(Dataframemiddle, textvariable=self.symptom1, state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem1["values"] = (" ",
                                    "B", "C", "A", " ", "     ",
                                    "   ", "  ")
        comNameProblem1.current(0)
        comNameProblem1.grid(row=0, column=1)
        #for symptom2
        lblNamesymptom2 = Label(Dataframemiddle, font=("arial", 12, "bold"), text="symptom2:", padx=2, pady=6)
        lblNamesymptom2.grid(row=1, column=0, sticky=W)

        comNameProblem2 = ttk.Combobox(Dataframemiddle, textvariable=self.symptom2, state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem2["values"] = (" ",
                                    "B", "C", "A", "   ", "   ",
                                    "   ", "   ", " ", " ", " ")
        comNameProblem2.current(0)
        comNameProblem2.grid(row=1, column=1)
        #for symptom3
        lblNamesymptom3 = Label(Dataframemiddle, font=("arial", 12, "bold"), text="symptom3:", padx=2, pady=6)
        lblNamesymptom3.grid(row=2, column=0, sticky=W)

        comNameProblem3 = ttk.Combobox(Dataframemiddle, textvariable=self.symptom3, state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        comNameProblem3["values"] = (" ",
                                    "B", "C", "A", "   ", "   ",
                                    "   ", "   ")
        comNameProblem3.current(0)
        comNameProblem3.grid(row=2, column=1)




        # up to here it is for buttons in left top section
#=====================================TEXT BOXES FOR DOWN SECTION AND TOP-4==================================================
#=====================================FOR "YOUR PROBLEM"================================================================
        self.txtproblem=Text(DetailsframeLeft,font=("arial", 12, "bold"), width=85,height=8,padx=2,pady=2)
        self.txtproblem.grid(row=0,column=0)
#====================================FOR MEDICINES======================================================================
        self.txtproblem2= Text(DetailsframeRight, font=("arial", 12, "bold"), width=74, height=8, padx=2, pady=2)
        self.txtproblem2.grid(row=0, column=0)
#====================================FOR PRESCRIPTION===================================================================
        self.txtproblem3 = Text(Dataframeright, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=2)
        self.txtproblem3.grid(row=0, column=0)
#===========================================for print button===============================================================
        def iprint():

            q = self.txtproblem3.get("1.0", "end-1c")

            filename = tempfile.mktemp(".txt")

            open(filename, "w").write(q)

            os.startfile(filename, "print")
#==============================for clear button=============================================================================
        def reset():
            self.txtproblem.delete("1.0",END)
            self.txtproblem2.delete("1.0", END)
            self.txtproblem3.delete("1.0", END)
            self.PROBLEM1.set("")
            self.PROBLEM2.set("")
            self.PROBLEM3.set("")
            self.PROBLEM4.set("")
            self.PROBLEM5.set("")
            self.PROBLEM6.set("")
            self.PROBLEM7.set("")
            self.symptom1.set("")
            self.symptom2.set("")
            self.symptom3.set("")

#=======================================FOR PREAUTOMATED TEXT IN PRESCRIPTION TAB==================================================
        def iprescription():
            self.txtproblem3.insert(END,"    HEALTH MANAGEMENT SYSTEM"+"\n"+"               PRESCRIPTION"+"\n")
            self.txtproblem3.insert(END,"# YOUR PROBLEMS ARE:\n" + self.PROBLEM1.get() +"\n" + self.PROBLEM2.get()+"\n"
                                    + self.PROBLEM3.get()+"\n" + self.PROBLEM4.get()+"\n" + self.PROBLEM5.get()+"\n"
                                    + self.PROBLEM6.get()+"\n" + self.PROBLEM7.get()+ "\n"+"\n")
            self.txtproblem3.insert(END, "# ALSO YOU HAVE:\n" + self.symptom1.get() + "\n" + self.symptom2.get() + "\n"
                                    + self.symptom3.get()+ "\n"+"\n")

        #=====================================COMMAND BUTTONS================================================================================
#FOR PRINT BUTTON:
        btnhealthproblem = Button(self.txtproblem3, text="print",command=iprint ,fg="black", bg="goldenrod",
                                  font=("Eras Bold ITC",12, "bold"), width=8,activeforeground="black",activebackground="goldenrod")
        btnhealthproblem.place(x=90,y=266)
#FOR MY PROBLEM:
        btnhealthproblem=Button(Buttonframeleft,text="MY PROBLEM",fg="black",bg="cyan",font=("Eras Bold ITC", 10, "bold"),width=76
                                ,activeforeground="black",activebackground="cyan")
        btnhealthproblem.grid(row=0,column=0)
#FOR MEDICINES BUTTON
        btnhealthproblem2 = Button(Buttonframeright, text="MEDICINES  +", fg="black", bg="cyan", font=("Eras Bold ITC", 10, "bold"),
                                  width=22,activeforeground="black",activebackground="cyan")

        btnhealthproblem2.grid(row=0, column=0)
#FOR UPDATE BUTTON
        btnhealthproblem3 = Button(Buttonframeright,text="UPDATE",command=iprescription,fg="black", bg="cyan", font=("Eras Bold ITC", 10, "bold"),
                                  width=22,activeforeground="black",activebackground="cyan")
        btnhealthproblem3.grid(row=0, column=1)
#FOR CLEAR BUTTON
        btnhealthproblem4 = Button(Buttonframeright, text="CLEAR",command=reset ,fg="black", bg="cyan",
                                   font=("Eras Bold ITC", 10, "bold"),
                                   width=20,activeforeground="black",activebackground="cyan")
        btnhealthproblem4.grid(row=0, column=2)
#FOR NEXT BUTTON
        btnhealthproblem5 = Button(DataframeLeft,text="NEXT >>",fg="black", bg="goldenrod",
                                   font=("Eras Bold ITC", 12, "bold"),
                                   width=10,activeforeground="black",activebackground="goldenrod")
        btnhealthproblem5.place(x=150,y=280)



#=========================================================pop up boxes for INFO LABEL=====================================================
#================================ for "RULES" button===========================================

        def clicker():
            global pop
            pop= Toplevel(root)
            pop.title("QUICK GUIDE TO THIS MODULE")
            pop.geometry("450x350")
            pop.config(bg="red")

            global me
            me=PhotoImage(file="rule.png")

            my_frame=Frame(pop, bg="green")
            my_frame.pack(pady=10)

            me_pic=Label(my_frame, image=me,borderwidth=0,bd=10, padx=20, relief=RIDGE,height=300,width=380)
            me_pic.pack()

        b3 = Button(Dataframefirst, text="R\nU\nL\nE\nS",command=clicker ,fg="black", bg="cyan",
                    font=("Cooper Std Black", 10),
                    height=9,width=5,activeforeground="black",activebackground="cyan")
        b3.place(x=-13, y=0)
#=============================== for developers button=============================================

        def clicker():
            global popp
            pop= Toplevel(root)
            pop.title("DEVELOPERS FOR THIS PROJECT")
            pop.geometry("600x650")
            pop.config(bg="grey2")

            global me2
            me2=PhotoImage(file="developersss.png")

            my_frame2=Frame(pop, bg="green")
            my_frame2.pack(pady=10)

            me_pic2=Label(my_frame2, image=me2,borderwidth=0,bd=10, padx=20, relief=RIDGE,height=700,width=650)
            me_pic2.pack()



        b4 = Button(Dataframefirst, text="D\nE\nV\nL\nO\nP\nE\nR\nS",command=clicker ,fg="black", bg="cyan",
                    font=("Cooper Std Black", 10),
                    height=9,width=5,activeforeground="black",activebackground="cyan")
        b4.place(x=-13, y=160)



if __name__ == '__main__':
    main()

# THIS IS ALL ABOUT OUR CODE WHICH WE HAVE COVERED UPTO NOW.......
#NOW LET US SEE THE ACTUAL WORK AS AN OUTPUT FOR OUR WORK.........



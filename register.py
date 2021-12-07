from tkinter import *
from tkinter import ttk

class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("Registration for Students Associations in LPU ")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")
		
		
		# register frame
		frame1 = Frame(self.root, bg="white").place(width=700,height=500)
		title = Label(frame1,text="Student Association's LPU", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
		
		
		#-----------------------------------------Row 1
		f_name = Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
		txt_fname =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=50, y=130,width=250)

		l_name = Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
		txt_lname =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=370, y=130,width=250)

		
		#-----------------------------------------Row 2
		reg_no = Label(frame1,text="Registration no", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
		txt_regno =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=50, y=200,width=250)

		course = Label(frame1,text="Branch", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
		txt_course =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=370, y=200,width=250)
		
		
		#------------------------------------------Row 3
		contact = Label(frame1,text="Contact No", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
		txt_contact =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=50, y=270,width=250)

		email = Label(frame1,text="Email", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
		txt_email =  Entry(frame1,font=('times new roman',15),bg="lightgray").place(x=370, y=270,width=300)
		
		
		#------------------------------------------Row 4
		question = Label(frame1,text="In which association you are intrested in?", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
		
		cmb_quest =  ttk.Combobox(frame1,font=('times new roman',13),state="readonly",justify=CENTER)
		cmb_quest['values']=('Select',"Academic & Technical","Artisan","Ayurveda & Yoga","Disaster Management","Event Management","Fitness","Education Initiation")
		cmb_quest.place(x=50, y=340,width=250)
		cmb_quest.current(0)

		
		# terms and conditions ---------------------------
		chk = Checkbutton(frame1,text="I Agree, The Terms & Conditions",onvalue=1,offvalue=0,bg="white",fg="blue",font=("times new roman",12)).place(x=50,y=380)

		
		def submit_value():
			print("Your information has been saved successfully")

		Button(text="Submit", command=submit_value,bg="white",fg="green",font=('times new roman',20,"bold")).place(x=370,y=380,height=30,width=120)



root = Tk()
obj = Register(root)
root.mainloop()


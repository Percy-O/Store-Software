from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from customtkinter import *
import customtkinter

import requests
import json


host = 'http://127.0.0.1:8000/'


class Homepage(CTkFrame):
	def __init__(self,parent,*args,**kwargs):
		CTkFrame.__init__(self,parent,*args,**kwargs)
		self.parent = parent
		self.pack(fill=BOTH,expand=True)

		self.main_menu = MainMenu(self)
		# self.log_reg = LogReg(self)


		# Parent Menu Configuration
		self.parent.config(menu=self.main_menu)


	def loginuser(self,*args):
		self.login = Login(parent=self)

	def registeruser(self,*args):
		self.register = Register(parent=self)


class MainMenu(Menu):
	def __init__(self,parent,*args,**kwargs):
		Menu.__init__(self,parent,*args,**kwargs)
		self.parent=parent

		print(self.parent)

		self.home_icon = PhotoImage(file='Store_Software/icons/home1.png')
		self.home = Menu(self,tearoff=0)
		self.add_cascade(image=self.home_icon,compound=LEFT) 
		# self.add_cascade(label=' Home ',image=self.home_icon,compound=LEFT) 

		self.user = Menu(self,tearoff=0)
		self.user.add_command(label='Register',command=self.parent.registeruser)

		self.user.add_command(label='Login',command=self.parent.loginuser)
		self.register = Menu(self,tearoff=0)
		self.add_cascade(label='User',menu=self.user) 

		# self.login = Menu(self,tearoff=0)
		# self.add_cascade(label='Login',) 

		# self.home = Menu(self,tearoff=0)
		# self.add_cascade(label='Home',) 

		# self.home = Menu(self,tearoff=0)
		# self.add_cascade(label='Home',) 

class Login(CTkToplevel):
	def __init__(self,parent,*args,**kwargs):
		CTkToplevel.__init__(self,parent,*args,**kwargs)
		self.parent = parent
		self.title('Login User')
		self.geometry("600x500+500+200")
		self.resizable(False,False)

		# Frame
		self.frame = CTkFrame(self,width=500,height=400)
		self.frame.pack(pady=70)


		# Login

		# login
		# topimage = PhotoImage(file='../icons/download.png')
		# lblimage = Label(self.frame,image=topimage)
		# lblimage.grid(columnspan=2,row=0)

		top = Frame(self.frame,bg='#05b',relief=SUNKEN,width=400,height=50)
		top.grid(row=0,pady=0,columnspan=2,sticky=W+E)
		CTkLabel(top,text='User Login').pack()
		CTkLabel(top,text='MyStore',).pack()


		labeluser = CTkLabel(self.frame,text='Username:',anchor=W)
		labeluser.grid(row=1,column=0,sticky=W,pady=30,padx=(30,0))

		self.entryuser = CTkEntry(self.frame,placeholder_text='Please Your Username',width=200,border_color="")
		self.entryuser.grid(row=1,column=1,sticky=W,padx=(0,10))


		labelpassword = CTkLabel(self.frame,text='Password:',anchor=W)
		labelpassword.grid(row=2,column=0,sticky=W,padx=(30,0))

		self.entrypassword = CTkEntry(self.frame,show='*',placeholder_text='Please Your Password',width=200,border_color="")
		self.entrypassword.grid(row=2,column=1,sticky=W)

		self.radiouser = CTkCheckBox(self.frame,text='Have you read our terms and condition?')
		self.radiouser.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=(30,0),pady=10)

		self.buttonuser = CTkButton(self.frame,text='Login Now',hover_color='#05b',corner_radius=2,command=self.authenticate)
		self.buttonuser.grid(row=4,column=1,sticky=W,pady=(10,20))

		labelask = CTkLabel(self.frame,text='You Dont Have an Account, Register Now!',anchor=CENTER)
		labelask.grid(row=5,columnspan=2,pady=(0,10))

	def authenticate(self):

		global host
		username = self.entryuser.get()
		password = self.entrypassword.get()


		# Getting the request host

		data = {
			'username':username,
			'password':password
		}

		endpoint = host + 'auth/jwt/create'
		response = requests.post(endpoint,data=data)
		response_dict = json.loads(response.text)
		print(response_dict)
		self.token = response_dict['access']






class Register(CTkToplevel):
	def __init__(self,parent,*args,**kwargs):
		CTkToplevel.__init__(self,parent,*args,**kwargs)
		self.parent = parent
		self.title('Register User')
		self.geometry("600x600+500+200")
		self.resizable(False,False)

		# Frame
		self.frame = CTkFrame(self,width=500,height=600)
		self.frame.pack(pady=70)


		# Login

		# login
		top = Frame(self.frame,bg='#05b',relief=SUNKEN,width=400,height=50)
		top.grid(row=0,pady=0,columnspan=2,sticky=W+E)
		CTkLabel(top,text='User Registration').pack()
		CTkLabel(top,text='MyStore',).pack()


		labelfname = CTkLabel(self.frame,text='Firstname:',anchor=W)
		labelfname.grid(row=1,column=0,sticky=W,pady=10,padx=(30,0))

		self.entryfname = CTkEntry(self.frame,placeholder_text='Please Your Firstname',width=200,border_color="")
		self.entryfname.grid(row=1,column=1,sticky=W,padx=(0,10))

		labellname = CTkLabel(self.frame,text='Lastname:',anchor=W)
		labellname.grid(row=2,column=0,sticky=W,pady=10,padx=(30,0))

		self.entrylname = CTkEntry(self.frame,placeholder_text='Please Your Lastname',width=200,border_color="")
		self.entrylname.grid(row=2,column=1,sticky=W)

		labeluser = CTkLabel(self.frame,text='Username:',anchor=W)
		labeluser.grid(row=3,column=0,sticky=W,pady=10,padx=(30,0))

		self.entryuser = CTkEntry(self.frame,placeholder_text='Please Your Username',width=200,border_color="")
		self.entryuser.grid(row=3,column=1,sticky=W)

		labelemail = CTkLabel(self.frame,text='Email:',anchor=W)
		labelemail.grid(row=4,column=0,sticky=W,pady=10,padx=(30,0))

		self.entryemail = CTkEntry(self.frame,placeholder_text='Please Your Email Address',width=200,border_color="")
		self.entryemail.grid(row=4,column=1,sticky=W)

		labelpassword = CTkLabel(self.frame,text='Password:',anchor=W)
		labelpassword.grid(row=6,column=0,sticky=W,padx=(30,0),pady=10)

		self.entrypassword = CTkEntry(self.frame,show='*',placeholder_text='Please Your Password',width=200,border_color="")
		self.entrypassword.grid(row=6,column=1,sticky=W)

		self.buttonuser = CTkButton(self.frame,text='Register',hover_color='#05b',corner_radius=2,command=self.register)
		self.buttonuser.grid(row=7,column=1,sticky=W,pady=(10,20))

		labelask = CTkLabel(self.frame,text='You Have an Account, Login Now!',anchor=CENTER)
		labelask.grid(row=8,columnspan=2,pady=(0,10))

	def register(self):

		firstname = self.entryfname.get()
		lastname = self.entrylname.get()
		username = self.entryuser.get()
		email = self.entryemail.get()
		password  = self.entrypassword.get()

		data = {
			'first_name':firstname,
			'last_name':lastname,
			'username':username,
			'email':email,
			'password':password
		}

		endpoint = host + 'auth/users/'
		response = requests.post(endpoint,json=data)
		messagebox.showinfo('Registration Success','Successfully Registered Account')
		print(response.status_code)
		# if response.status_code == 200:
			
		# else:
		# 	messagebox.showerror('Registration Fail','Registration Failed!')
		# response_dict = json.loads(response.text)




# class LogReg(CTkFrame):
# 	def __init__(self,parent,*args,**kwargs):
# 		CTkFrame.__init__(self,parent,*args,**kwargs)
# 		self.parent=parent


# 		self.pack(pady=200,padx=30)
# 		self.configure(width=500,height=400)

# 		# Label Frame

# 		# self.tabs = ttk.Notebook(self,width=400,height=250)
# 		# self.tabs.pack(expand=True,)

# 		# logintab = CTkFrame(self.tabs)
# 		# regtab = CTkFrame(self.tabs)

# 		# self.tabs.add(logintab,text='User Login')
# 		# self.tabs.add(regtab,text='User Registration',compound=LEFT)


# 		# login
# 		top = Frame(self,bg='#05b',relief=SUNKEN,width=400,height=50)
# 		top.grid(row=0,pady=0,columnspan=2,sticky=W+E)
# 		CTkLabel(top,text='User Login').pack()
# 		CTkLabel(top,text='MyStore',).pack()


# 		labeluser = CTkLabel(self,text='Username:',anchor=W)
# 		labeluser.grid(row=1,column=0,sticky=W,pady=30,padx=(30,0))

# 		entryuser = CTkEntry(self,placeholder_text='Please Your Username',width=200,border_color="")
# 		entryuser.grid(row=1,column=1,sticky=W)


# 		labelpassword = CTkLabel(self,text='Password:',anchor=W)
# 		labelpassword.grid(row=2,column=0,sticky=W,padx=(30,0))

# 		entrypassword = CTkEntry(self,show='*',placeholder_text='Please Your Password',width=200,border_color="")
# 		entrypassword.grid(row=2,column=1,sticky=W)

# 		radiouser = CTkCheckBox(self,text='Have you read our terms and condition?')
# 		radiouser.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=(30,0),pady=10)

# 		buttonuser = CTkButton(self,text='Login Now',hover_color='#05b',corner_radius=2)
# 		buttonuser.grid(row=4,column=1,sticky=W,pady=(10,20))

# 		labelask = CTkLabel(self,text='You Dont Have an Account, Register Now!',anchor=CENTER)
# 		labelask.grid(row=5,columnspan=2,pady=(0,10))


		









def main():

	customtkinter.set_appearance_mode('dark')
	customtkinter.set_default_color_theme('blue')
	root = CTk()
	root.title("MyStore")
	app = Homepage(root)

	app.pack(side=TOP,fill=BOTH,expand=True)
	# root.iconbitmap('../icons/1con.ico')
	root.geometry('1250x850')
	# root.resizable(False,False)
	root.mainloop()


if __name__=='__main__':
	main()

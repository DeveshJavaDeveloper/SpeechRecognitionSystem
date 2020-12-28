from tkinter import *
class about(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("600x400+400+150")
		self.title("About Us")
		Label(self,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		explaination=""" 
***********
To run this Application 
1. Install Python 3+ or 3.8.4
2. Install Some Libraries
pip install PyAudio
pip install speech_recognition
pip install pygame
pip install gtts
Run welcome.py
Now you Go......
*********** """
		Label(self,text=explaination,padx=20,font=('Times New Roman',14,'bold')).pack(side="left")
		Button(self,text="QUIT",fg='blue',width=10,bd=5,command=self.quit).place(x=400,y=100)
		Button(self,text="BACK",fg='blue',width=10,bd=5,command=self.back).place(x=400,y=150)
	def quit(self):
		self.master.destroy()
	def back(self):
		self.destroy()

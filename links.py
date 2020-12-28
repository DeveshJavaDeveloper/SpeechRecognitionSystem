from tkinter import *
from aboutus import *
from google import *
from youtube import *
from audios import *
class link(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.title("Main")
		self.geometry("600x400+400+150")
		Label(self,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		Button(self,text="REQUIREMENTS",width=20,fg='blue',bd=5,command=self.about).place(x=240,y=90)
		Button(self,text="GOOGLE SEARCH",width=20,bd=5,fg='blue',command=self.google_search).place(x=240,y=140)
		Button(self,text="YOUTUBE SEARCH",width=20,bd=5,fg='blue',command=self.youtube_search).place(x=240,y=190)
		Button(self,text="PLAY AUDIO",width=20,bd=5,fg='blue',command=self.play_audio).place(x=240,y=240)
	def about(self):
		root=about()
	def google_search(self):
		root=googlesearch()
	def youtube_search(self):
		root=youtubesearch()
	def play_audio(self):
		root=playaudio()
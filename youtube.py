from tkinter import *
import speech_recognition as sr
import webbrowser as wb
from respondaudio import *
import os
class youtubesearch(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("600x400+400+150")
		self.title("Youtube Search")
		Label(self,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		Label(self,text="Click Search and Please Speak....").place(x=100,y=200)
		Button(self,text="Search",bd=5,fg='blue',width=10,command=self.search).place(x=150,y=150)
		Button(self,text='QUIT',bd=5,fg='blue',width=10,command=self.quit).place(x=250,y=150)
		Button(self,text='BACK',bd=5,fg='blue',width=10,command=self.back).place(x=350,y=150)
		self.image=PhotoImage(file='voice.png')
		Label(self,image=self.image).place(x=100,y=150)
	def quit(self):
		self.master.quit()
	def back(self):
		try:
			os.remove("welcome.mp3")
		except:
			print("File not found....")
		self.destroy()
	def search(self):
		r1=sr.Recognizer()
		url="https://www.youtube.com/results?search_query="
		with sr.Microphone() as source:
			audio=r1.listen(source)
			text=r1.recognize_google(audio)
			playresponse(text)
			#obj=respond()
			print(text)
			wb.get().open_new(url+text)
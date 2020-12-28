from tkinter import *
import speech_recognition as sr
import webbrowser as wb
from respondaudio import * 
import os
class googlesearch(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("600x400+400+150")
		self.title("Google Search")
		Label(self,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		self.image=PhotoImage(file="voice.png")
		Label(self,text="Click Search and Please Speak.....").place(x=100,y=200)
		Label(self,image=self.image).place(x=100,y=150)
		Button(self,text="Search",width=10,bd=5,fg='blue',command=self.search).place(x=150,y=150)
		Button(self,text="QUIT",width=10,bd=5,fg='blue',command=self.quit).place(x=250,y=150)
		Button(self,text="BACK",width=10,bd=5,fg='blue',command=self.back).place(x=350,y=150)
	def quit(self):
		self.master.quit()
	def back(self):
		try:
			os.remove("welcome.mp3")
		except:
			print("file not found.....")
		self.destroy()
	def search(self):
		#import speech_recognition as sr
		#import webbrowser as wb
		url="https://www.google.com/search?q="
		r=sr.Recognizer()
		print("What do you want to search")
		with sr.Microphone() as source:
			try:
				audio=r.listen(source) #record(source,duration=5)
				print("Wait ....")
				text=r.recognize_google(audio)
				print(text)
				playresponse(text)
				wb.get().open_new(url+text)
			except Exception as e:
				print("Sorry Try again..")
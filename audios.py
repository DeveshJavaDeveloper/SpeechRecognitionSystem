from tkinter import *
from pygame import mixer as m
import speech_recognition as sr
from respondaudio import *
import os
class playaudio(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("600x400+400+150")
		self.title("Play Audio")
		self.image=PhotoImage(file='voice.png')
		Label(self,image=self.image).place(x=100,y=150)
		Label(self,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		Button(self,text="Search",bd=5,width=10,fg='blue',command=self.search).place(x=150,y=150)
		Button(self,text="STOP",bd=5,width=10,fg='blue',command=self.stopmusic).place(x=250,y=150)
		Button(self,text="BACK",bd=5,width=10,fg='blue',command=self.back).place(x=350,y=150)
		Button(self,text="QUIT",bd=5,width=10,fg='blue',command=self.quit).place(x=450,y=150)
		Label(self,text='Click Search and Please Speak.....').place(x=100,y=200)
		m.init()
	def back(self):
		try:
			os.remove("welcome.mp3")
		except:
			print("File not Found....")
		self.destroy()
	def quit(self):
		self.master.quit()
	def search(self):
		try:
			r1=sr.Recognizer()
			print("Speak Now.....")
			with sr.Microphone() as source:
				audio=r1.listen(source)
				print("Wait.....")
				text=r1.recognize_google(audio)
				print(text)
				playresponse(text)
				s="audios/"+text+".mp3"
				m.music.load(s)
				print("music load")
				m.music.play()
		except Exception as e:
			print("Failed".format(e))
	def stopmusic(self):
		try:
			os.remove("welcome.mp3")
		except:
			print("file Not Found....")
		m.music.stop()
		print("Thank You.....")
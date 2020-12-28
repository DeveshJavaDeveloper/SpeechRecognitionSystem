from tkinter import *
from links import *
class welcome:
	def __init__(self,master):
		self.master=master
		self.master.title("Welcome")
		self.master.geometry("600x400+400+150")
		Label(master,text="SPEECH RECOGNITION",font=('Times New Roman',20,'bold'),fg='green').place(x=145,y=15)
		Button(master,text="START",width=10,fg='Blue',bd=5,command =self.gotolinks).place(x=220,y=160)
		Button(master,text="QUIT",width=10,fg='Blue',bd=5,command=self.finishit).place(x=310,y=160)
	def gotolinks(self):
		root=link() 
	def finishit(self):
		self.master.destroy()
def main():
	root=Tk()
	wel=welcome(root)
	mainloop()
if __name__=='__main__':
	main()

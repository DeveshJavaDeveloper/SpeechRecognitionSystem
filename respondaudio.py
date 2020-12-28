from gtts import gTTS
from playsound import playsound
def playresponse(text):
	data=text
	mytext="You are searching for "+text
	language='en'
	def play(path):
		playsound(path)
	output=gTTS(text=mytext,lang=language,slow=False)
	output.save("welcome.mp3")
	play("welcome.mp3")
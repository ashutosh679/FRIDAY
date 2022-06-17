import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import numpy as np
import cv2
import pywhatkit
import sys
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from fridayUI import  Ui_fridayUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Friday your Virtual Assistant")
	speak("I am your Female Replacement Intelligent Digital Assistant Youth.")
	speak(assname)
	
	speak("How can i Help you Sir")


def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()

class MainThread(QThread):
	def __init__(self):
		super (MainThread,self).__init__()

	def run(self):
		self.TaskExecution()

		
	def takeCommand(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 0.6
			audio = r.listen(source)

		try:
			print("Recognizing...")
			self.query = r.recognize_google(audio, language ='en-in')
			print(f"User said: {self.query}\n")

		except Exception as e:
			print(e)
			print("Unable to Recognize your voice.")
			return "None"
		return self.query

				
	if __name__ == '__main__':
		clear = lambda: os.system('cls')
			
			# This Function will clean any
			# command before execution of this python file
		clear()

	def TaskExecution(self):
		wishMe()
		l = ["ashu", "sarvesh", "ritesh"]
		while True:
			self.query = self.takeCommand().lower()
			
			# All the commands said by user will be
			# stored here in 'query' and will be
			# converted to lower case for easily
			# recognition of command
			if 'wikipedia' in self.query:
				speak('Searching Wikipedia...')
				self.query = self.query.replace("wikipedia", "")
				results = wikipedia.summary(self.query, sentences = 3)
				speak("According to Wikipedia")
				print(results)
				speak(results)

			elif 'open youtube' in self.query:
				speak("Here you go to Youtube\n")
				webbrowser.open("youtube.com")

			elif 'open google' in self.query:
				speak("Here you go to Google\n")
				webbrowser.open("google.com")

			elif 'open stackoverflow' in self.query:
				speak("Here you go to Stack Over flow.Happy coding")
				webbrowser.open("stackoverflow.com")

			elif 'open facebook' in self.query:
				speak("Here you go to Google\n")
				webbrowser.open("facebook.com")	

			
			elif 'open code' in self.query:
				path =""
				os.startfile(path)		
				

			elif 'play music' in self.query or "play song" in self.query:
				speak("Here you go with music")
				music_dir = "C:\\Users\\GAURAV\\Music"
				songs = os.listdir(music_dir)
				print(songs)
				random = os.startfile(os.path.join(music_dir, songs[0]))


			elif 'the time' in self.query:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				speak(f"Sir, the time is {strTime}")

			elif 'send a whatsapp message' in self.query:
				hrs = datetime.datetime.now().hour
				m = datetime.datetime.now().minute
				m += 2
				a = "0"
				try:
					speak("What should I say?")
					b = self.takeCommand()
					speak("whom should i send")
					q = self.takeCommand()
					for item in l:
						if q == "ashu":
							a = "8879704886"
						elif q == "sarvesh" :
							a = "9892508872"
						elif q == "ritesh" :
							a = "9702398206"
					pywhatkit.sendwhatmsg('+91'+a, b, hrs, m)
					speak("Your message has been sent !")
				except Exception as e:
					print(e)
					speak("I am not able to send this message") 


			elif 'send a mail' in self.query:
				try:
					speak("What should I say?")
					content = self.takeCommand()
					speak("whome should i send")
					p = self.takeCommand()
					for item in l:
						if p == "ashu" :
							to = "thakurashutosh679@gmail.com"
						elif p == "sarvesh" :
							to = "sarveshsasane572@gmail.com"
						elif p == "ritesh":		
							to = "riteshvarma3401@gmail.com"
					sendEmail(to, content)
					speak("Email has been sent !")
				except Exception as e:
					print(e)
					speak("I am not able to send this email")

			elif 'how are you' in self.query:
				speak("I am fine, Thank you")
				speak("How are you, Sir")

			elif 'fine' in query or "good" in self.query:
				speak("It's good to know that your fine")


			elif "who made you" in self.query or "who created you" in self.query:
				speak("some students struggling for mini project made me.")
				
			elif 'joke' in self.query:
				speak(pyjokes.get_joke())
				print(pyjokes.get_joke())
			
			elif "calculate" in self.query:
				
				app_id = "5827XP-842XXU94PP"
				client = wolframalpha.Client(app_id)
				indx = query.lower().split().index('calculate')
				query = query.split()[indx + 1:]
				res = client.query(' '.join(query))
				answer = next(res.results).text
				print("The answer is " + answer)
				speak("The answer is " + answer)

			elif 'search' in self.query or 'play' in self.query:
				
				query = query.replace("search", "")
				query = query.replace("play", "")		
				webbrowser.open(query)

			elif "who i am" in self.query:
				speak("If you can control me then definately you are a human.")

			elif "why you came to world" in self.query:
				speak("So that you can get good marks")

			elif 'is love' in self.query:
				speak("It is 7th sense that destroy all other senses")

			elif "who are you" in self.query:
				speak("I am your virtual assistant ")

			elif 'reason for you' in self.query or "why was you created" in self.query:
				speak("to help you as your Mini project")


			elif 'news' in self.query:
				
				try:
					api_key = "6cc23da452ff42239701fce8a60395bc"
					jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6cc23da452ff42239701fce8a60395bc
	''')
					data = json.load(jsonObj)
					i = 1
					
					speak('Here are some top news from the times of india')
					print('''=============== TIMES OF INDIA ============'''+ '\n')
					
					for item in data['articles']:
						if i <= 2 :
							print(str(i) + '. ' + item['title'] + '\n')
							print(item['description'] + '\n')
							speak(str(i) + '. ' + item['title'] + '\n')
							speak(item['description'] + '\n')
							i += 1
						else :
							break	
				except Exception as e:
					
					print(str(e))

			

			elif 'shutdown system' in self.query:
					speak("Hold On a Sec ! Your system is on its way to shut down")
					os.system('shutdown /s ')
					
			elif 'empty recycle bin' in self.query:
				winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
				speak("Recycle Bin Recycled")

			elif "don't listen" in self.query or "stop listening" in self.query:
				speak("for how much time you want to stop jarvis from listening commands")
				a = int(self.takeCommand())
				time.sleep(a)
				print(a)

			elif "where is" in self.query:
				query = query.replace("where is", "")
				location = self.query
				speak("User asked to Locate")
				speak(location)
				webbrowser.open("https://www.google.nl / maps / place/" + location + "")

			elif "camera" in self.query or "take a photo" in self.query:
				cam = cv2.VideoCapture(0)
				cv2.namedWindow("test")
				img_counter = 0
				while True:
					ret, frame = cam.read()
					if not ret:
						print("failed to grab the frame")
						break
					cv2.imshow("test", frame)
					
					escape = self.takeCommand()
					if escape == "exit" :
						break
					elif escape == "click":
						img_name = "friday_frame_{}.png".format(img_counter)
						img_counter += 1
				cam.release()
				cv2.destroyAllWindows()

			elif "shoot video"	in self.query or "make a video" in self.query :
				cap = cv2.VideoCapture(0)
				fourcc = cv2.VideoWriter_fourcc(* "XVID")
				#out = cv2.videowriter("friday.avi", forcc, 20.0, (640, 480))
				while True :
					ret, frame = cap.read()
					#out.write(frame)
					cv2.imshow("frame", frame)
					i = self.takeCommand()

					if i == "stop" or i == "stop recording":
						#cv2.waitkey(1) & 0xFF = ord("q")
						break
				cap.release()
				#out.release()
				cv2.destroyAllWindows()	
			
			elif "restart" in self.query:
				speak("Are you sure sir?")
				response = self.takeCommand()
				if response == "no" :
					break 

				else:
					os.system("shutdown /r")
				
			elif "hibernate" in self.query or "sleep" in self.query:
				speak("Hibernating")
				subprocess.call("shutdown /h")

			elif "log off" in self.query or "sign out" in self.query:
				speak("Make sure all the application are closed before sign-out")
				time.sleep(5)
				subprocess.call("shutdown /l")

			elif "write a note" in self.query:
				speak("What should i write, sir")
				note = self.takeCommand()
				file = open('friday.txt', 'w')
				speak("Sir, Should i include date and time")
				snfm = self.takeCommand()
				if 'yes' in snfm or 'sure' in snfm:
					strTime = datetime.datetime.now().strftime("%H:%M:%S")
					file.write(strTime)
					file.write(" :- ")
					file.write(note)
				else:
					file.write(note)
			
			elif "show note" in self.query:
				speak("Showing Notes")
				file = open("friday.txt", "r")
				print(file.read())
				speak(file.read(6))

						
			elif "friday" in self.query:
				
				wishMe()
				speak("Friday at your service Sir")
			

			elif "outside temperature" in self.query:
				
				search = "temperature of current location"
				url = f"https://www.google.com/search?q={search}"
				x = requests.get(url)
				data = BeautifulSoup(x.text, "html.parser")
				temp = data.find("div", class_="BNeawe").text
				print (f"current {search} is {temp}")

			elif "weather" in self.query:
				
				speak("city name")
				city_name = self.takeCommand()
				search = f"temperature of {city_name}"
				url = f"https://www.google.com/search?q={search}"
				x = requests.get(url)
				data = BeautifulSoup(x.text, "html.parser")
				temp = data.find("div", class_="BNeawe").text
				print (f"current {search} is {temp}")	
			

			elif "wikipedia" in self.query:
				webbrowser.open("wikipedia.com")

			elif "Good Morning" in self.query:
				speak("A warm" +self.query)
				speak("How are you Sir")


			elif "how are you" in self.query:
				speak("I'm fine, glad you are here")

			elif "i love you" in self.query:
				randNO = random.randint(1, 4)
				if random == 1:
					speak("I Love You Too")
				elif random == 2:
					speak("Aww, that so nice of you")	
				elif random == 3:
					speak("I'm not sure about, may be you should give me some time")
				else :
					speak("Sorry I am Enagaged")

			elif "what is" in self.query or "who is" in self.query:
				
				# Use the same API key
				# that we have generated earlier
				client = wolframalpha.Client("5827XP-842XXU94PP")
				res = client.query(query)
				
				try:
					print (next(res.results).text)
					speak (next(res.results).text)
				except StopIteration:
					print ("No results")
			
			elif "exit" in self.query:
				speak("Thanks and have a good day ahead ")
				exit()

			elif 'abort' in self.query:
				speak("System is closing up")
				sys.exit()

					

			# elif "" in query:
				# Command go here
				# For adding more commands

startExecution = MainThread()

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui =  Ui_fridayUI()
		self.ui.setupUi(self)
		#self.setFixedSize(1920,1080)
		self.ui.pushButton.clicked.connect(self.startTask)
		#self.ui.pushButton_2.clicked.connect(self.close)

	def startTask(self):
		self.ui.movie = QtGui.QMovie("E:/New folder/61c3-unscreen.gif")
		self.ui.label_5.setMovie(self.ui.movie)
		self.ui.movie.start()

		self.ui.movie = QtGui.QMovie("E:/New folder/8a08-unscreen.gif")
		self.ui.label_6.setMovie(self.ui.movie)
		self.ui.movie.start()

		self.ui.movie = QtGui.QMovie("E:/New folder/BR-unscreen.gif")
		self.ui.label_7.setMovie(self.ui.movie)
		self.ui.movie.start()

		self.ui.movie = QtGui.QMovie("E:/New folder/6874-unscreen.gif")
		self.ui.label_9.setMovie(self.ui.movie)
		self.ui.movie.start()

		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)
		startExecution.start()

	def showTime(self):
			current_time = QTime.currentTime()
			current_date = QDate.currentDate()
			label_time = current_time.toString("hh:mm:ss")
			label_date = current_date.toString(Qt.ISODate)
			self.ui.textBrowser.setText(label_time)
			self.ui.textBrowser_2.setText(label_date)		

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())

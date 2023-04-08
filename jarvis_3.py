from cProfile import label
from ipaddress import ip_address
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import numpy as np
from requests import get
import json
#import pywhatkit as kit
#import time
import sys
#import pyjokescli
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#  print(voices[0].id) 
engine.setProperty('voice',voices[0].id)

def  speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
         speak("Good Morning sir!")
         speak("I am jarvis. please tell me how may I help you ")
         
        elif hour>=12 and hour<18:
         speak("Good Afternoon sir!")
         speak("I am jarvis. please tell me how may I help you ")

        else:
         speak("Good Evening sir!")

         speak("I am jarvis. please tell me how may I help you ")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('chaitanyanikam007@gmail.com', '9322079070c')
    server.sendmail('chaitanyanikam007@gmail.com', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
         self.permission = self.takeCommand().lower()
         if "wakeup" or "wake up" in self.permission:
         
          self.taskExecution()

    def takeCommand(self):
        #it takes microphone input from the user and return string output.
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1 ,phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")                                                                 
        
        except Exception as e:
            print(e)
            print("say that again please...")
            return "None"
        return query


    def taskExecution(self):
     wishMe()
     while True:
     #if 1:
        self.query = self.takeCommand().lower()
        if 'wikipedia' in self.query:
            speak('searching wikipedia ... ')
            self.query = self.query.replace("wikipedia","")
            results = wikipedia.summary(self.query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in self.query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in self.query:
            webbrowser.open("facebook.com")

        elif 'open google' in self.query:
            speak("sir, what should i search on google")
            cm = self.takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'open adobe reader' in self.query:
            apath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(apath)

        #elif "send massage" in self.query:
           # kit.sendwhatmsg("+919322079070","this is testing protocall",9,19)
        
       # elif'play songs on youtube' in self.query:
         #   kit.playonyt("see you again")

        elif 'open stack overflow' in self.query:
            webbrowser.open("stackoverflow.com")
           
        elif 'play music' in self.query:
            music_dir = 'D:\\my favourite song'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in self.query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")
        
        elif 'open code' in self.query:
            codePath = "C:\\Users\\chaitanya nikam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open notepad' in self.query:
            npath="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npath)
        
        elif 'open command prompt' in self.query:
            os.system("start cmd")

        elif'open camera' in self.query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam', img)
                k=cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyallWindows()

        elif "ip address" in self.query:
            ip= get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")  
            print(ip) 


            
        elif 'email to pankaj' in self.query:
            try:
                speak("what should i say?")
                content = self.takeCommand()
                to = "baviskarpankaj143@gmail.com"
                sendEmail( to, content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("sorry my friend chaitanya. I am not able to send this mail at that time")
        
        elif "shutdown the system" in self.query:
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in self.query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in self.query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif'no thanks' in self.query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir do you have any work")

startExecution =MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Ui = Ui_jarvisUI()
        self.Ui.setupUi(self)
        self.Ui.pushButton_2.clicked.connect(self.startTask)
        self.Ui.pushButton.clicked.connect(self.close)

    def startTask(self):
        self.Ui.movie =QtGui.QMovie("E:/jarvis/jarvis gui material/7LP8.gif")
        self.Ui.label.setMovie(self.Ui.movie)
        self.Ui.movie.start()

        self.Ui.movie =QtGui.QMovie("E:/jarvis/jarvis gui material/Jarvis_Loading_Screen.gif")
        self.Ui.label_2.setMovie(self.Ui.movie)
        self.Ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_Time = QTime.currentTime()
        current_Date =QDate.currentDate()
        label_time = current_Time.toString("hh:mm:ss")
        label_date = current_Date.toString(Qt.ISODate)
        self.Ui.textBrowser.setText(label_date)
        self.Ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())





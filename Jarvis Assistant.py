import pyttsx3
import pyttsx3.drivers
import pyttsx3.drivers.sapi5
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import wikipedia
import webbrowser
from random import randint
import smtplib
import pickle
import os
import sys
import datetime
from PIL import Image, ImageTk

'''
This is a sample project with less no of tasks.
There is no limit of adding tasks. Just define a mathod and call it.

There are 3 buttons on window.

1. Text To Speech - This button will speak it out whatever the text given to 1st Text Box present on Top.
2. Speech to Text - This button does exactly reverse of 1st Button (Text To Speech). It will take input as
                    your voice and will give you the text. (make sure mic is working fine)
3. Assitant       - This is best thing about of this App. After pressing this you have to speak some commands,
                    It will follow some commands as follows.
                    - what is the time
                    - what is your name
                    - tell me about yourself
                    - Bill gates wikipedia (gives summary from wikipedia)
                    - send email
                    - play some songs / play music
                    - open my resume
                    - open google/youtube
                    - shut down the pc
                    - exit / quit
                    (you can add as many as features you want to add)

Author: Ganesh Patil
GitHub: gproxx-coder
'''

class Jarvis:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def wishMe(self):
        self.hour = int(datetime.datetime.now().hour)
        if 0 <= self.hour < 12:
            self.speak("Good Morning.")
        elif 12 <= self.hour < 16:
            self.speak("Good Afternoon.")
        elif 16 <= self.hour <= 24:
            self.speak("Good Evening.")
        self.speak("How can i help you ?")


    def takeMailCommand(self):
        # It takes microphone input from the user.
        # and Returns that audio Input to string output.

        recognizer = sr.Recognizer()
        with sr.Microphone() as listener:
            print("Can You Please Tell the Content of email...")
            recognizer.pause_threshold = 1
            self.audio = recognizer.listen(listener)

        try:
            self.query = recognizer.recognize_google(self.audio, language='en-in')
            print(f"You said: {self.query}")
        except Exception as e:
            print(e)
            print("Please try again !! ")
            return "None"
        return self.query


    def getTime(self):
        self.strTime = datetime.datetime.now().strftime('%H:%M:%S')
        self.speak(f"Now the time is, {self.strTime}")


    def getWiki(self, query):
        try:
            self.query = self.query.replace('wikipedia', '')
            self.results = wikipedia.summary('"' + self.query + '"', sentences=2)
            self.speak('According to wikipedia,')
            self.speak(self.results)
        except Exception as e:
            self.speak(f"Wikipedia not able to find {self.query}. Please try again")


    def thisPC(self):
        try:
            self.appDir = 'C:\\Users\\Abcd\\Desktop\\This PC.lnk'
            os.startfile(self.appDir)
        except FileNotFoundError:
            print("Something went wrong. Try again with Name.")


    def myResume(self):
        try:
            self.appDir = 'C:\\Users\\Abcd\\Desktop\\Ganesh R Patil Resume.pdf'
            os.startfile(self.appDir)
        except FileNotFoundError:
            self.speak("Something went wrong. Try again.")


    def playMusic(self, musicDir='G:\\songs'):
        self.musicDir = 'G:\\songs'
        self.musicList = os.listdir(self.musicDir)
        shuffle = randint(1, len(self.musicList)-1)
        print(self.musicList[shuffle])
        os.startfile(os.path.join(self.musicDir, self.musicList[shuffle]))


    def sendEmail(self):
        try:
            self.speak("What should i write in mail ? ")
            self.content = self.takeMailCommand()
            self.to = 'email_id_of_receiver'

            #The following 2 lines will Unpickle the User id and password from pickled file
            #The file has dictionary (key:value pair) {'id':'sender_email_id', 'pass':'sender_email_password}
            with open('temp', 'rb') as f:
                self.creds = pickle.load(f)

            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(creds['id'], creds['pass'])
            self.server.sendmail(creds['id'], to, content)
        except Exception as e:
            print(e)
            self.speak("Something went wrong. Unable to send mail.")


    def openVSCode(self):
        try:
            self.appDir = 'C:\\Users\\Abcd\\AppData\\Local\\Programs\\Microsoft VS Code'
            self.appName = 'Code.exe'
            os.startfile(os.path.join(self.appDir, self.appName))
        except FileNotFoundError:
            print("Something went wrong. Try again.")


    def openChrome(self):
        try:
            self.appDir = 'C:\\Program Files (x86)\\Google\\Chrome\\Application'
            self.appName = 'chrome.exe'
            os.startfile(os.path.join(self.appDir, self.appName))
        except FileNotFoundError:
            print("Something went wrong. Try again.")

    #The speak method which will speak the text from tkinter windwos textbox
    def speakTextBox(self, *args):
        self.engine.setProperty('rate',180)
        self.engine.say(textBox.get("1.0",END))
        self.engine.runAndWait()
        # textBox.delete("1.0", END)

    def speak(self, audio):
        self.audio = audio
        self.engine.setProperty('rate',180)
        self.engine.say(self.audio)
        self.engine.runAndWait()

    def takeCommand(self):
        # It takes microphone input from the user.
        # and Returns that audio Input to string output.

        recognizer = sr.Recognizer()
        with sr.Microphone() as listener:
            print("Listening...")  
            # listenBox()
            recognizer.pause_threshold = 1
            self.audio = recognizer.listen(listener)
            
        try:
            self.query = recognizer.recognize_google(self.audio, language='en-in')
            print(f"You said: {self.query}")
            textWidget.insert(END, f"{self.query} / ")
            # textWidget.delete("1.0", END)
        except Exception as e:
            print(e)
            print("Please try again !! ")
            return "None"
        return self.query

def main():
    jarvis.wishMe()
    if 1:
        jarvis.query = jarvis.takeCommand().lower()
            
        if 'the time' in jarvis.query:
             jarvis.getTime()
            
        elif 'your name' in jarvis.query:
            jarvis.speak("thats Good Question. My name is Jarvis, and I am your assistant.")

        elif any(x in jarvis.query for x in ['your info','your information','about yourself','about you']):
            jarvis.speak("thats Good Question. My name is Jarvis, and I am your assistant. I am made by Mr. Ganesh Patil. I am written in Python language with using several important libraries. I am using google speech recognition engine and pyttsx3 engine to speak. Thank you. I hope you will like my work.")

        elif 'wikipedia' in jarvis.query:
            jarvis.getWiki(jarvis.query)

        elif 'open youtube' in jarvis.query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in jarvis.query:
            webbrowser.open('https://www.google.com/')

        elif 'this pc' in jarvis.query:
            jarvis.thisPC()

        elif any(x in jarvis.query for x in ['open my resume','open resume','open cv','open my cv']):
            jarvis.myResume()

        elif any(x in jarvis.query for x in ['play music', 'play song', 'play some music', 'play a song','song','music']):
            jarvis.playMusic()
            
        elif any(x in jarvis.query for x in ['send mail', 'send email']):
            jarvis.sendEmail()

        elif any(x in jarvis.query for x in ['open code', 'open vs code','vs code']):
            jarvis.openVSCode()

        elif any(x in jarvis.query for x in ['open chrome', 'open google chrome']):
            jarvis.openChrome()
            
        elif any(x in jarvis.query for x in ['shut down','shutdown', 'turn off']):
            jarvis.speak("Are you sure you want to Turn Off the PC ?")
            choice = jarvis.takeCommand().lower()
            if choice == 'yes':
                os.system("shutdown /s /t 1")
            else:
                jarvis.speak("Ohh. So you did it by mistakenly. No problem.")

        elif any(x in jarvis.query for x in ['quit','stop','exit']):
            jarvis.speak('Ok. Bye. Take care.')
            sys.exit()
            
        else:
            jarvis.speak("Ummm.. Something went wrong. Please try again.")


if __name__ == "__main__":

    jarvis = Jarvis()

    root = tk.Tk()
    root.title("Personal Assistant {by GP. Github:gproxx-coder}")
    root.geometry('491x300')
    

    image = Canvas(root, width='491', height='300')
    image.place(relx=0, rely=0)

    
    try:
        background = PhotoImage(file=os.path.join(sys.path[0], "background.png"))
        # background = PhotoImage(file=".img\\background.png")
        image.create_image(491,300, image=background)
    except:
        image.configure(bg='black')


    #Text box code
    textBox = Text(root, height = 2, width = 52)
    textBox.place(x=35, y=20)

    #The Speak button code
    speakButton = tk.Button(root, text ="Text to Speech", font=('arial', 15), command=jarvis.speakTextBox, bg='#%02x%02x%02x' % (25, 255, 228), activebackground='#%02x%02x%02x' % (22, 184, 165), activeforeground='white')
    speakButton.place(x=175, y=70)

    #The Listen button code
    listenButton = tk.Button(root, text ="Speech to Text", font=('arial', 15), command=jarvis.takeCommand, bg='#%02x%02x%02x' % (224, 219, 117), activebackground='#%02x%02x%02x' % (201, 194, 38), activeforeground='red')
    listenButton.place(x=50, y=130)

    assistButton = tk.Button(root, text ="Assistant", font=('arial', 15), command=main, bg='#%02x%02x%02x' % (139, 255, 77), activebackground='#%02x%02x%02x' % (79, 158, 36), activeforeground='red', cursor="box_spiral")
    assistButton.place(x=285, y=130, width=150)

    #Text Widget
    textWidget = Text(root, height = 5, width = 52)
    textWidget.place(x=35, y=190)

    root.mainloop()
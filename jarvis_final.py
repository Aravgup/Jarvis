import operator
import os
import sys
import time
from instadownloader import instaloader
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import subprocess
import pyjokes
import pyautogui
from playsound import playsound
from pywikihow import search_wikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JARVISui import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
  engine.say(audio)
  print(audio)
  engine.runAndWait()

def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening")
    r.pause_threshold = 1
    audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak(" ")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak("good morning Arav, its " + current_time)
    elif hour>=12 and hour<=16:
        speak("good afternoon  Arav, its " + current_time)
    else:
        speak("good evening Arav,its " + current_time)
    speak("allow me to introduce myself, I'm JARVIS,I am here to help you with your works ")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aravgupta442@gmail.com','Arav221009')
    server.sendmail('aravgupta442@gmail.com',to,content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=f214490fb4854cdc86bce285094e9bf4b'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second","third", "fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles[:10]:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is {head[i]}")

def pdf_reader():
    book = open('pyread.pdf','rb')
    pdfReader = pyPDF2.pdffileReader(book)
    pages = pdfReader.numpages
    speak(f"sir the pdf contains {pages} number of pages")
    speak("sir please enter the pages number that you want me to speak")
    pg = input("enter the page number: ")
    page = pdfReader.getpage(pg)
    text = page.extractText()
    speak(text)

class MainThread(QThread):
 
      def __init__(self):
          super(MainThread,self).__init__()
          
      def run(self):
          self.TaskExecution()




      def takecommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening")
                r.pause_threshold = 1
                audio = r.listen(source)
                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(f"user said: {query}")
                except Exception as e:
                    speak(" ")
                    return "none"
                return query
            

      def TaskExecution(self):

            while True:

                self.query = self.takecommand().lower()
                if "notepad" in self.query:
                    path = "C:\\Windows\\System32\\notepad.exe"
                    os.startfile(path)

                elif "command prompt" in self.query:
                    path = "C:\\windows\\system32\\cmd.exe"
                    os.startfile(path)

                elif "youtube" in self.query:
                    path = "C:\\Users\\aravg\\Downloads\\windows\\YouTube-win32-x64\\YouTube.exe"
                    webbrowser.open(f"www.youtube.com")

                elif "close the website" in self.uery:
                    speak("closing")
                    os.system("taskkill /f /im chrome.exe")
                elif "chrome" in self.query:
                    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)

                elif "camera" in self.query:
                    cam = cv2.VideoCapture(0)
                    while True:
                        ret,img = cam.read()
                        cv2.imshow("webcam", img)
                        k = cv2.waitKey(10)
                        if k==27:
                            break
                    cam.release()
                    cv2.destroyAllWindows()

                elif "hello JARVIS" in self.query:
                    speak("hello boss i am JARVIS your personal ai assistant")

                elif "wake up" in self.query:
                    wish()


                elif "sleep JARVIS" in self.query:
                    speak("good night friend but if you want my help just let me know")
                    subprocess.call(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0', '1', '0'])

                elif "joke" in self.query:
                    speak("ok  listen  a  joke")
                    jokes = pyjokes.get_joke()
                    speak(jokes)

                elif "ip address" in self.query:
                    ip = get("https://api.ipify.org/").text
                    speak(f"Your IP address is {ip}")

                #elif "TARS where are we" in query:
                #   speak("ok  sir  let me check ")
                #  try:
                #     ipAdd = requests.get('https://api.ipify.org/').text
                    #    print(ipAdd)
                    #   url = 'https://geojs.io/ip/geo/'+ipAdd+'.json'
                    #  geo_requests = requests.get(url)
                    # geo_data = geo_requests.json()
                        #city = geo_data['city']
                        #state = geo_data['state']
                        #country = geo_data['country']
                        #speak(f"sir i think we are in {city} city of {state} state of {country} country")
                    #except Exception as e:
                    #   speak("sorry sir due to some network issue i am unable to find our exact location")
                    #  pass

                elif "thank you JARVIS" in self.query:
                    speak("sir should i sleep or stay with you")
                    cm = takecommand().lower()
                    if "do you want me to sleep or should i stay" in cm:
                        if "stay":
                            speak("ok sir")
                    elif "sleep" in cm:
                        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')



                elif "JARVIS where are we" in self.query:
                    loc = get('https://get.geojs.io/').text
                    speak(f"sir as per my record your location is {loc}")

                elif "pause" in self.query or "play" in self.query   :
                    pyautogui.press('space')

                elif "skip" in self.query:
                    pyautogui.press('right')

                elif "rewind" in self.query:
                    pyautogui.press('left')

                elif "download instagram profile" in self.query:
                    speak("sir please enter  the username correctly:")
                    name = input("Enter Username here:")
                    webbrowser.open(f"www.instagram.com/{name}")
                    time.sleep(5)

                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir , what should i do next")

                elif "JARVIS are you there" in self.query:
                    speak("always with you sir do you need any help")
                    cm = takecommand().lower()
                    if "yes" in cm:
                        speak("ok sir what should i do for you")
                        query = takecommand().lower()
                    elif "no" in cm:
                        speak("ok sir let me know if you need my help")


                elif "wikipedia" in self.query:
                    speak("searching in wikipedia.....")
                    self.query = self.query.replace("wikipedia","")
                    results = wikipedia.summary(self.query,sentences=4)
                    speak("wikipedia says...")
                    speak(results)
                    print(results)

                elif "github" in  self.query:
                    webbrowser.open("www.github.com")

                elif " change the window" in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "time" in self.query:
                    wish()

                elif "instagram" in self.query:
                    webbrowser.open("www.instagram.com")
                elif "facebook" in self.query:
                    webbrowser.open("www.facebook.com")
                elif "geeksforgeeks" in self.query:
                    speak("what should i search in geeks for geeks")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"https://www.geeksforgeeks.org/search?q={cm}")

                elif "google" in self.query:
                    speak("what should i search in google")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"{cm}")

                elif "send message " in self.query:
                    speak("what text you want to send ")
                    cm = self.takecommand().lower()
                    kit.sendwhatmsg("+916000051150",f"{cm}",21,31)

                elif "email" in self.query:
                    try:
                        speak("What should I write?")
                        content = self.takecommand().lower()
                        to = "niragupta98@gmail.com"
                        sendEmail(to, content)
                        speak("Email sent successfully")
                    except Exception as e:
                        print(e)
                        speak("Sorry, unable to send the email")

                elif "code checker" in self.query:
                    speak("opening  codeium")
                    webbrowser.open("www.codeium.com")

                elif "activate how to do" in self.query:
                    speak("ok sir activating how to do mode")
                    how = self.takecommand()
                    max_result = 1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)


                elif "amazon" in self.query:
                    speak("what should i search in amazon")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"https://www.amazon.com/search?q={cm}")

                elif "flipkart" in self.query:
                    speak("what should i search on  flipkart")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"https://www.flipkart.com/search?q={cm}")

                elif "JARVIS restart the system" in self.query:
                    speak("restarting  the  system")
                    os.system("shutdown /r /t 0")

                elif "close notepad" in self.query:
                    speak("closing  notepad")
                    os.system("taskkill /f /im notepad.exe")

                elif "JARVIS close command prompt" in self.query:
                    speak("closing  command prompt")
                    os.system("taskkill /f /im cmd.exe")

                elif "close flipkart" in self.query:
                    speak("closing  flipkart")
                    os.system("taskkill /f /im chrome.exe")


                elif "news" in self.query:
                    speak("ok sir please wait till i fetch the latest news")
                    news()



                elif "shutdown" in self.query:
                    speak("shutting  down")
                    os.system("shutdown /s /t 1")

                elif "screenshot" in self.query:
                    speak("sir by what name should i save this screenshot")
                    name = takecommand().lower()
                    speak("sir please hold the screen i am taking screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir the screenshot has been saved")
        #        elif "read pdf" in query:
        #           pdf_reader()
                elif "hide this file" in self.query or "hide this folder" in self.query or "make it visible to everyone" in self.query:
                    speak("are you sure sir that you want to hide this file or folder or should i make this visible to everyone")
                    cm = self.takecommand().lower()
                    if "hide" in cm:
                        os.system("attrib +h /s /d")
                        speak("task complete sir all files are now hidden")

                    elif "visible" in cm:
                        os.system("attrib -h /s /d")
                        speak("task complete sir all the files are now visible to everyone")

                    else:
                        speak("ok sir")

                elif "can you calculate this" in self.query:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("what should i do")
                        print("Listening......")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            '-': operator.sub,
                            '*': operator.mul,
                            'divided':operator.__truediv__,
                        }[op]
                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("the result is")
                    speak(eval_binary_expr(*(my_string.split())))

                elif "minimise" in self.query:
                    pyautogui.hotkey('winleft', 'down')

                elif "maximize" in self.query:
                    pyautogui.hotkey('winright','up')

                elif "song" in self.query:
                    speak("what do you want to listen")
                    cm = takecommand().lower()
                    kit.playonyt(f"{cm}")

                elif "video" in self.query:
                    speak("what do you want to watch")
                    cm = takecommand().lower()
                    kit .playonyt(f"{cm}")


                elif "no thanks" in self.query:
                    speak("thanks for using me have a good day")
                    sys.exit()

startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("38b9ada46c0a26d92a966cd12c7a3edb.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time('hh:mm:ss')
        label_date = current_date(Qt.ISODate)
        self.ui.setText(label_date)
        self.ui.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()

jarvis.show()
exit(app.exec_())
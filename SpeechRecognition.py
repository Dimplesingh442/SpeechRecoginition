import pyttsx3 # it will convert text to speech(pip install pyttsx3)
import speech_recognition as sr #  this is a Library for performing speech recognition, with support for several engines and APIs, online and offline.(pip install SpeechRecognition)
import wikipedia # this will help you to search wikipedia  (pip install wikipedia)
import webbrowser # this will help you to open any website like google,youtube etc
import random    # this is use to generate random number(pip install random2)
import datetime  # this is use to generate the current time
from selenium import webdriver # selenium will open google find the search bar and types your query in the search bar and clicks the search button (pip install selenium)
from selenium.webdriver.common.keys import Keys
import smtplib # The smtplib module defines an SMTP client session object that can be 
               # used to send mail to any Internet machine with an SMTP  
               # which handles all of the different parts of the protocol, 
               # like connecting, authenticating, validation, 
               # and of course, sending emails.(pip install secure-smtplib)

import os # The OS module in Python provides functions for interacting with the operating system.
import requests # Requests allows you to send HTTP requests extremely easily(pip install requests)
from bs4 import BeautifulSoup # Beautiful Soup is a library that makes it easy to scrape information from web pages. 
                              # Whether it be an HTML or XML page, that can later be used for iterating, searching, 
                              # and modifying the data within it.(pip install bs4)
import pyautogui as pg # it controls the mouse and keybroad by automation(pip install pyautogui)
import keyboard as k # now you can do any operation on you computer throught automation(pip install keyboard)
from time import sleep # it will help to stop your code for some time (pip install python-time)
import wolframalpha #The Wolfram|Alpha Webservice API provides a web-based API allowing the computational 
                    # and presentation capabilities of Wolfram|Alpha to be integrated into web, mobile, desktop, 
                    # and enterprise applications.(pip install wolframalpha)
import ssl #SSL stands for Secure Sockets Layer and is designed to create secure connection between client and server. 
import pyjokes #Pyjokes is used for collection Python Jokes over the Internet.(pip install pyjokes)
import json #The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
from urllib.request import urlopen #The urllib.request module defines functions and classes which help in opening URLs(mostly HTTP) 









#using text to speech conversion library pyttsx3
#nsss gives an api to takes voices
engine=pyttsx3.init('nsss')
engine.setProperty("language",'en')
voices=engine.getProperty('voices') #we are using nsss for using voices
engine.setProperty('voice',voices[7].id) 


 
# speak function so that your system can speak
def speak(audio):
       engine.say(audio)
       engine.runAndWait()




# wishme fuction is used to wish you in the starting of your program like good morning etc
def Wishme():
       hour=int(datetime.datetime.now().hour)# this will calculate the current time
       if hour>0 and hour<12:
              speak("good morning")
       elif hour>=12 and hour<18:
              speak("Good Afternoon ")
       else:
              speak("good evening ") 
       speak(" how may i help you")
       




# takeCommand fuction will listen to you convert your voice into text
def TakeCommand():
       r=sr.Recognizer() #this recognizer class will recognize your voice
       with sr.Microphone() as source:
              print("Go ahead I'm Listening....")
              r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
              audio =r.listen(source)
       try:  
              print("recognizing....")
              query=r.recognize_google(audio,language="en")
              print(f"user said:{query}\n")
       except :
              print("what can I help you with")
              return "None"
       return query







       


#------------------------------------------------------------------main method---------------------------------------------------------------------------------#





if __name__=="__main__":
       
       
       
       Wishme() #f irst of all we will call wishme function to start you program
       while 1:
              query=TakeCommand().lower() # now your program is calling TakeCommand function to recoginize your voice and convert it into text
             

             # various tasks you want you program to perform
              if 'hello' in query:
                     speak("hello what can I help you....")
                     TakeCommand()

              
              
              
              # when you want to search any wikipedia
              if 'wikipedia' in query: # this will search wikipedia word in your query 
                     speak("searching...")
                     query=query.replace("wikipedia"," ") # this will remove the word wikipedia 
                     results=wikipedia.summary(query,sentences=2) # this will store 2 sentenses of searched wikipedia in results
                     speak("according to wikipedia...")
                     print(results) # this will print 2 sentences of searched wikipedia
                     speak(results) # this will speak 2 setences of searched wikipedia


              
              
              # when you want to open any website like google,youtube etc
              elif 'open youtube' in query:
                     webbrowser.open("https://www.youtube.com/")
              elif 'open google' in query:
                     webbrowser.open("https://www.google.co.in/?client=safari&channel=iphone_bm")
              elif 'open facebook' in query:
                     webbrowser.open("https://www.facebook.com")
              elif 'open instagram'  in query:
                     webbrowser.open("https://www.instagram.com/")    

              
              
              
              
              
              
              # when you want to paly hindi or english music on youtube
              elif 'play music' in query:
                    speak(" which music do you want to listen. hindi or english ?") 
                    query=TakeCommand().lower() # it will again take command from you 
                    if 'hindi' in query:
                           n = random.randint(0,5) # this will generate a random number between 0 to 5
                          
                           if(n==1):
                                  webbrowser.open("https://www.youtube.com/watch?v=bi5PhlIQpwU")
                           elif(n==2):
                                   webbrowser.open("https://www.youtube.com/watch?v=HoCwa6gnmM0")
                           elif(n==3):
                                  webbrowser.open("https://www.youtube.com/watch?v=YrrDrx5Rd_I")
                           elif(n==4):
                                  webbrowser.open("https://www.youtube.com/watch?v=qoq8B8ThgEM")
                           else:
                                  webbrowser.open("https://www.youtube.com/watch?v=X2Bsr_WOigU")
                    
                    elif 'english' in query:
                           n = random.randint(0,5)
                           if(n==1):
                                  webbrowser.open("https://www.youtube.com/watch?v=kffacxfA7G4")
                           elif(n==2):
                                   webbrowser.open("https://www.youtube.com/watch?v=pRpeEdMmmQ0")
                           elif(n==3):
                                  webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
                           elif(n==4):
                                  webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
                           else:
                                  webbrowser.open("https://www.youtube.com/watch?v=DIQQfo3ZAvo")
              

              
              
              
              
              
              # when you want to know the current time 
              elif 'time' in query:
                     time=datetime.datetime.now().strftime("%H:%M") # it will store the current time in the time variable and time will be in hours and minutes
                     speak(time) # it will speak the time for you
              



              
              
              
              
              # when you want to search anything on google 
              elif 'search' in query:
                     query=query.replace('search',"")
                     browser = webdriver.Safari() # it will start selenium with safari if you want you can use chrome or whatever you want
                     browser.get('http://www.google.com')
                     search = browser.find_element_by_name('q')
                     search.send_keys(query)
                     search.send_keys(Keys.RETURN)




              # when you want to open any application on your system
              elif 'open' in query:
                     query=query.replace('open',"")
                     
                     
                     if 'whatsapp' in query:
                            os.system("open /Applications/WhatsApp.app") # this will open Whatsapp on your system
                     
                     elif 'calendar' in query:
                            os.system("open /System/Applications/Calendar.app")
                     
                     elif 'chess' in query:
                            os.system("open /System/Applications/Chess.app")
                     
                     elif 'contacts' in query:
                            os.system("open /System/Applications/Contacts.app")
                     
                     elif 'dictionary' in query:
                            os.system("open /System/Applications/Dictionary.app")
                     
                     elif 'facetime' in query:
                            os.system("open /System/Applications/FaceTime.app")
                     
                     elif 'google chrome' in query:
                            os.system("open /System/Applications/Google\ Chrome.app")
                     
                     elif 'app store' in query:
                            os.system("open /System/Applications/App\ Store.app")
                     
                     elif 'find my' in query:
                            os.system("open /System/Applications/Find\ My.app")
                     
                     elif 'font book' in query:
                            os.system("open /System/Applications/Font\ Book.app")
                     
                     elif 'github desktop' in query:
                            os.system("open /Applications/GitHub\ Desktop.app")
                     
                     elif 'home' in query:
                            os.system("open /System/Applications/Home.app")
                     
                     elif 'image capture' in query:
                            os.system("open /System/Applications/Image\ Capture.app")
                     
                     elif 'launchpad' in query:
                            os.system("open /System/Applications/Launchpad.app")
                     
                     elif 'mail' in query:
                            os.system("open /System/Applications/Mail.app")
                     
                     elif 'Maps' in query:
                            os.system("open /System/Applications/Maps.app")
                     
                     elif 'Messages' in query:
                            os.system("open /System/Applications/Messages.app")
                     
                     elif 'mission control' in query:
                            os.system("open /System/Applications/Mission\ Control.app")
                     
                     elif 'music' in query:
                            os.system("open /System/Applications/Music.app")
                     
                     elif 'notes' in query:
                            os.system("open /System/Applications/Notes.app")
                     
                     elif 'photo booth' in query:
                            os.system("open /System/Applications/Photo\ Booth.app")
                     
                     elif 'photos' in query:
                            os.system("open /System/Applications/Photos.app")
                     
                     elif 'podcast' in query:
                            os.system("open /System/Applications/Podcasts.app")
                     
                     elif 'preview' in query:
                            os.system("open /System/Applications/Preview.app")
                     
                     elif 'quicktime player' in query:
                            os.system("open /System/Applications/QuickTime\ Player.app")
                     
                     elif 'reminders' in query:
                            os.system("open /System/Applications/Reminders.app")
                     
                     elif 'safari' in query:
                            os.system("open /System/Applications/Safari.app")
                     
                     elif 'siri' in query:
                            os.system("open /System/Applications/Siri.app")
                     
                     elif 'stickies' in query:
                            os.system("open /System/Applications/Stickies.app")
                     
                     elif 'Stocks' in query:
                            os.system("open /System/Applications/Stocks.app")
                     
                     elif 'system preferences' in query:
                            os.system("open /System/Applications/System\ Preferences.app")
                     
                     elif 'text edit' in query:
                            os.system("open /System/Applications/TextEdit.app")
                     
                     elif 'time machine' in query:
                            os.system("open /System/Applications/Time\ Machine.app")
                     
                     elif 'apple tv' in query:
                            os.system("open /System/Applications/TV.app")
                     
                     elif 'utorrent web' in query:
                            os.system("open /Applications/uTorrent\ Web.app")
                     
                     elif 'vlc' in query:
                            os.system("open /Applications/VLC.app")
                     
                     elif 'voice memos' in query:
                            os.system("open /System/Applications/Voice\ Memos.app")
                     
                     elif 'vs code' in query:
                            os.system("open /Applications/Visual\ Studio\ Code.app")
                     
                     elif 'visual studio code' in query:
                            os.system("open /Applications/Visual\ Studio\ Code.app")
                     
                     elif 'calculator' in query:
                            os.system("open /System/Applications/Calculator.app")
                     

                     
                     
                     
                     
                     
              # this will send email to the give email address
              elif 'email' in query:
                try:
                     if query=='email':
                            query=query.replace("email","recipient")

                     query=query.replace("send email to "," ") 
                     speak("tell me the email of "+ query)
                     recipient_email=TakeCommand().lower() # it will take recipient email address
                     recipient_email=recipient_email.replace(" ","") # it will remove spaces from your recipient email address
                     
                     speak('What should I say ?') 
                     content = TakeCommand()# speak what you want to send to the recipient
                     mail = smtplib.SMTP('smtp.gmail.com', 587) #SMTP (Simple Mail Transfer Protocol) is an application-level protocol 
                                                                 #used to communicate with mail servers from external services, like an email client on your phone. 
                                                                 # SMTP is a delivery protocol only, so you can't actually retrieve email with it, you can only send email
                     
                     
                     mail.ehlo()  # .ehlo(), which identifies you to the SMTP server. Using this server object you can now send email over an insecure connection.
                     mail.starttls() #.starttls() method for secure connection
                     mail.login('singhdimple442@gmail.com', '05688252481') # it will login to your email account
                     mail.sendmail('singhdimple442@gmail.com', recipient_email +'@gmail.com', content) # it will help to send an email to any recipient
                     mail.close() # it will close the connection
                     speak('Email has been sent successfuly. You can check your inbox.') 
                except:
                     speak('I don\'t know what you mean!')

              
              
              
              

              # this will tell you the current temperature of any city if you will speak weather word 
              elif "weather" in query:
                     query=query.replace("weather of "," ")
                     url="https://www.google.com/search?q="+"weather"+query # it will create a URL with the query city in it and pass it to the get function
                     html=requests.get(url).content
                     soup = BeautifulSoup(html, 'html.parser') # Soup will return a heap of data with HTML tags. 
                                                               # So, which we will get all the necessary data with the help of 
                                                               # find function and passing the tag name and class name.
                     temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                     print(temp)
                     speak(f"it appears to be {temp}")

              
              
              # it will also tell you the current temperature if you will speak temperatur word
              elif "temperature " in query:
                     query=query.replace("temperature of "," ")
                    
                     print(query)
                     url="https://www.google.com/search?q="+"temperature"+query
                     html=requests.get(url).content
                     soup = BeautifulSoup(html, 'html.parser')
                     temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                     print(temp)
                     speak(f"it appears to be {temp}")



              
              # this will tell you about each and every thing
              elif 'tell me about' in query:
                     speak("searching...")
                     query=query.replace("Tell me about"," ") # this will remove the word wikipedia 
                     results=wikipedia.summary(query,sentences=2) # this will store 2 sentenses of searched wikipedia in results
                     speak("here what i found on web")
                     print(results) # this will print 2 sentences of searched wikipedia
                     speak(results) # this will speak 2 setences of searched wikipedia
                     speak("do you want to listen more")
                     command=TakeCommand()
                     if 'yes'in command:
                            results2=wikipedia.summary(query,sentences=4)
                            print(results2)
                            speak(results2)

              

              
              
              
              
              # thsi will send whatsapp message 
              elif "whatsapp message" in query:
                     query =query.replace("send whatsapp message to"," ")
                     speak("what should i say ?")
                     message=TakeCommand()
                     browser=webbrowser.open("https://web.whatsapp.com/")# it will open whatsapp
                     sleep(10) # now code will be in sleep for 10 sec so that whatsapp can open in the browser
                     pg.click(79,168) # this will click on the search bar to search the name of recipient
                     sleep(2)
                     k.write(query) #it will write the name of the recipient
                     sleep(2)
                     pg.click(166,292)
                     sleep(2)
                     pg.click(617,772)
                     k.write(message)
                     pg.press('enter')

              
              
              
              
              # if want your assistant to sing for you
              elif "sing a song" in query:
                     speak(" ok if you insist ")
                     speak("Blackbird singing in the dead of night Take these broken wings and learn to fly All your life You were only waiting for this moment to arise")

              
              
              
              
              
              # this will answer simple questions like the ones listed below.
              # Input : Who is the prime minister of India? 
              # Output : narandra modi
              elif 'who is the' in query or 'what is'in query or 'where is'in query:
                app_id='PJWYRK-24AA2AWAVE'  # this is the wolframe api id with the help of this you will be able to access answers
                ssl._create_default_https_context = ssl._create_unverified_context 
                client = wolframalpha.Client(app_id)# it will create an instance of wolframe aplha
                res = client.query(query) # it will store the response from wolframe
                answer = next(res.results).text # it will include only text from the responses
                print(answer) # it will print the result
                speak(answer)# it will speak the result


              
              elif 'who is'in query:
                     query=query.replace("who is"," ") # this will remove the word wikipedia 
                     results=wikipedia.summary(query,sentences=2) # this will store 2 sentenses of searched wikipedia in results
                     speak("here's what I found on web.....")
                     print(results) # this will print 2 sentences of searched wikipedia
                     speak(results) # this will speak 2 setences of searched wikipedia

                    


              
              
              
              
              
              elif "how are you" in query:
                     speak("I am fine, Thank you")
                     speak("How are you, Sir")


              elif 'fine'in query or 'good'in query:
                     speak("It's good to know that your fine")
              


              elif 'what is your name' in query or "what's your name" in query:
                     speak("my name is neer")

              elif 'exit' in query:
                     speak("Thanks for giving me your time")
                     exit()
 
              elif "who made you" in query or "who created you" in query:
                     speak("I have been created by Dimple.")
              
              
              elif 'joke' in query:
                     speak(pyjokes.get_joke())# this will read a joke using pyjokes api


              
              
              
              
              
              # this will calculate value of a given expression
              elif "calculate" in query:
                     app_id = "PJWYRK-24AA2AWAVE" # this is the wolframe api id with the help of this you will be able to access answers
                     ssl._create_default_https_context = ssl._create_unverified_context 
                     client = wolframalpha.Client(app_id) # it will create an instance of wolframe aplha
                     indx = query.lower().split().index('calculate')# first query will convert into lowercase then it will Split the string 
                                                                    # into a list where each word is a list item 
                                                                    # then it will calculate the index value of 'calculate' and
                                                                    # it the value will stored in indx variable
                     
                     query = query.split()[indx + 1:]  # here query will split into a list where each word is a list item and this list 
                                                       # will consider all the things which you will speak after calculate
                     
                     res = client.query(' '.join(query)) # it will search your query from wolframe aplha 
                     answer = next(res.results).text  # it will store the result in the text form to the answer variables
                     print("The answer is " + answer) # it will print the answer
                     speak("The answer is " + answer) # it will speak the answer




              
              elif "who i am" in query:
                     print("you are Dimple that's what you have told me anyway")
                     speak("you are Dimple that's what you have told me anyway")
              


              elif "why you came to the world" in query:
                     print("hmm.. I don't have answer to that. is there something else i can help with")
                     speak("hmm.. I don't have answer to that. is there something else i can help with")
              
              elif " what is love " in query:
                     print("It is 7th sense that destroy all other senses")
                     speak("It is 7th sense that destroy all other senses")

              elif "who are you" in query:
                     print("I am neer your virtual assistant ")
                     speak("I am neer your virtual assistant ")

              elif "what are you doing" in query:
                     print("well I was thinking that if there was no absolute truths,then it cannot be an absolute truth that there are no absolute truth,which means there are absolute truths if there are no absolute truth....")
                     speak("well I was thinking that if there was no absolute truths,then it cannot be an absolute truth that there are no absolute truth,which means there are absolute truths if there are no absolute truth....")


              
              
              # it will tell you some of the top news headlines
              elif 'news' in query:
                     try:   
                            ssl._create_default_https_context = ssl._create_unverified_context
                            news = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey=0446e3bde2154065bbf8f8011e0f6c91') # it will get the news data and store it in the news variable
                            data = json.load(news) # the data which is provided by the url will not be readable that is why we will use json to make it readable
                            i = 1
                            speak('here are some top news')
                            for item in data['articles']: # it will start reading the news from index 0
                                  print(str(i) + '. ' + item['title'] + '\n') # this will print the news title
                                  print(item['description'] + '\n')           # this will print the news description 
                                  speak(str(i) + '. ' + item['title'] + '\n') # this will read the news title
                                  speak(str(i) +'.' + item['description']+'\n') # this will read the description
                                  i += 1
                     except Exception as e:
                            print(str(e))
              




             


              




             

              
              
             
                     

              

              
              





                     
             




                  



              



              











              


              
                      
 
              


              
      
              
       





              










              




             

              
              
             
                     

              

              
              





                     
             




                  



              



              











              


              
                      
 
              


              
      
              
       





              









 

      
              
                        
              



              
              
              
              
            
                         

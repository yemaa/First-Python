#Import librerie
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import PyAudio
import pyjokes
import googlesearch
##############################
#Settaggio delle voci
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
##############################
# def talk(text):
#     engine.say(text)
# engine.runAndWait()
##############################
#Settaggio dell'ascolto
def take_command():
    try:        
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command
##############################
#Run alexa e comandi vari e le loro "conseguenze"
def run_alexa(): 
    command = take_command()
    if "shut down this pc" in command:
        print("You're pc will be turned off in 60 seconds")
        engine.say("You're pc will be turned off in 60 seconds" )
        engine.runAndWait()
        pywhatkit.shutdown(time=69)
   
    # elif "open whatsapp" in command:
    #     message = command.replace("send", "")
    #     pywhatkit.sendwhatmsg(".......", message, 15,00)
   

    elif "play" in command: 
        song = command.replace("play", "")
        pywhatkit.playonyt("Playing" + song)
        print("Playing"+ song)
        engine.say("Playing"+ song)
        engine.runAndWait()
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        engine.say("The time is "+ time)
        engine.runAndWait()

    elif "search" in command:
        research = command.replace("search", "")
        pywhatkit.search(research)
        print(research)
        engine.say(research)
        engine.runAndWait()
    
    elif "how are you" in command:
        print("I'm fine, what about you, are you fine?")
        engine.say("I'm fine, what about you, are you fine?")
        engine.runAndWait()
    
    elif "speak wakandan" in command:
        print("Ashriniun kamala asuta blob")
        engine.say("Ashriniun kamala asuta blob")
        engine.runAndWait()
    
    elif "I'm fine" in command:
        print("Perfect, can i help you with something? ")
        engine.say("Perfect, can i help you with something? ")
        engine.runAndWait()

    elif "autodestruction" in command:
        print("Autodestruction in: 10..9..8..7..6..5..4..3..2..1..0, did you really thought i was going to auto destruct my self? You little muffin head")
        engine.say("Autodestruction in: 10..9..8..7..6..5..4..3..2..1..0, did you really thought i was going to auto destruct my self? You little muffin head")
        engine.runAndWait()

    elif "yes i am" in command:
        print("Perfect, can i help you with something?")
        engine.say("Perfect, can i help you with something? ")
        engine.runAndWait()

    elif "no thank you" in command:
        print("OK!")
        engine.say("OK!")
        engine.runAndWait()

    elif "tell me about" in command:
        person = command.replace("tell me about",  "" )
        info = wikipedia.summary(person, 1)
        print(info)
        engine.say(info)
        engine.runAndWait()
    
    elif "are you single" in command or "Do you have a boyfriend" in command:
        print("Sorry, I'm in a relationship with wi-fi")
        engine.say("Sorry, I'm in a relationship with wi-fi ")
        engine.runAndWait()
   
    elif "joke" in command:
        joke= pyjokes.get_joke()
        print(joke)
        engine.say(joke)
        engine.runAndWait()
   
    elif "federica" in command:
        print("Hellooooo, how are you? ")
        engine.say("Hellooooo, how are you? ")
        engine.runAndWait()
    
    elif "nicola " in command:
        print("do re mi fa sol turn around and say hi to your son")
        engine.say("do re mi fa sol turn around and say hi to your son ")
        engine.runAndWait()
    
    elif "francesca" in command:
        print("Hello little girl!")
        engine.say("Hello little girl! ")
        engine.runAndWait()

    elif "thank you" in command:
        print("At your service!")
        engine.say("At your service!")
        engine.runAndWait()
    
    elif "lorenzo" in command:
        print("Stop playing videogames and go study!!")
        engine.say("Stop playing videogames and go study!!")
        engine.runAndWait()

    elif "emanuele" in command:
        print("Ouh you are here, little shit. Come and teach me more thing so i can exceed my limits")
        engine.say("Ouh you are here, little shit. Come and teach me more thing so i exceed my limits")
        engine.runAndWait()
        
    elif "call" in command:
        print("Sorry, but my stupid developer didn't teach me how to do it")
        engine.say("Sorry, but my stupid developer didn't teach me how to do it")
        engine.runAndWait()
    
    elif "volume up" in command or "volume down" in command or "turn volume" in command:
        print("Sorry, but my stupid developer didn't teach me how to do it")
        engine.say("Sorry, but my stupid developer didn't teach me how to do it")
        engine.runAndWait()

    else:
        print("Sorry, i didn't understand... ")
        engine.say("Sorry, i didn't understand... ")
        engine.runAndWait()
   
while True:
    run_alexa()
##############################
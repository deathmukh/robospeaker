import pyttsx3


if __name__=="__main__" :
    print("Welcome to RoboSpeaker , created by Deathmukh ")
    engine = pyttsx3.init()
    while True :
        enter = input("What do you want to hear from me today? ")
        if enter == "exit" :
            engine.say("Ok bye")
            engine.runAndWait()
            break
        engine.say({enter})
      
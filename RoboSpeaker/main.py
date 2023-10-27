import pyttsx3

if __name__ == '__main__':
    print("Welcome to robospeaker 1.1 created by Neha")
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == 'q':
            engine.say("bye bye friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

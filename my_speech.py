
def Recoz_speech():
    import pyttsx3

    text_speech=pyttsx3.init()

    answer="Welcome to Recoz, Biometric attendance system. You need to stand in front of camera for marking your attendance. " \
           "Your attendance would be marked with your display of name."

    text_speech.say(answer)
    text_speech.runAndWait()

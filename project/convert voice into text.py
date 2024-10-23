import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print(">>>Initialized<<<")
    myAudio=r.record(source,duration=5)
    myQuery=r.recognize_google(myAudio)
    print(":--")
    print(myQuery)

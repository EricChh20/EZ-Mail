'''
Hello!
'''
import speech_recognition as sr

def collect_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)

    recognized_audio = r.recognize_google(audio)
    return recognized_audio

if __name__ == '__main__':
    main()

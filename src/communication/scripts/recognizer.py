import speech_recognition as sr
import Word_functions

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                data=(format(value).encode("utf-8")).upper()
                if data in Word_functions.FullDictionary:
                    print(Word_functions.FullDictionary[data]()[0])
                    pub.publish(Word_functions.FullDictionary[data]()[1])
                elif data in Word_functions.FullDictionary_Nav: 
                    print(Word_functions.FullDictionary_Nav[data]()[0])
                    pub_2.publish(Word_functions.FullDictionary_Nav[data]()[1])
                else:
                    print(data, "not in dictionary")
                print (data)
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
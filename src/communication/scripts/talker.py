#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic
import rospy
import Word_functions  #File containing functions for voice commands
from std_msgs.msg import String
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

print ("talker opened")
pub = rospy.Publisher('command', String, queue_size=10)#bottle color
pub_2 = rospy.Publisher('obs_command', String, queue_size=10) #obstacle color
rospy.init_node('voice', anonymous=True)
rate = rospy.Rate(10) # 10hz

#with open('full_robot/src/communication/scripts/speechoutput.txt', "r+") as Wordfile:
#    while True: #Run Continuously
#            data = Wordfile.readline()
#            to_truncate = bool(data)
#            data = data[:-1] #get rid of new line
#            while "\x00" in data:
#                i = data.index('\x00')
#                data = data[i+1:]
#            if data:
#                if data in Word_functions.FullDictionary:
#                    print(Word_functions.FullDictionary[data]()[0])
#                    pub.publish(Word_functions.FullDictionary[data]()[1])
#                elif data in Word_functions.FullDictionary_Nav: 
#                    print(Word_functions.FullDictionary_Nav[data]()[0])
#                    pub_2.publish(Word_functions.FullDictionary_Nav[data]()[1])
#                else:
#                    print(data, "not in dictionary")
#            if to_truncate:
#                Wordfile.seek(0)
#                Wordfile.truncate()
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    #r.energy_threshold = 150
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
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
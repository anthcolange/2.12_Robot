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

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def start_drawer_task ():
    return ("starting drawer task")
def open_drawer():
    return  ("opening drawer")
def close_drawer():
    return ("closing drawer")
def drawer_done():
    return ("drawer task done")
def start_garment_task():
    return "starting garment task"
def hold_garment():
    return  ("holding garment")
def start_wrapping():
    return ("starting wrapping")
def let_go():
    return  ("letting go")
def start_medicine_task():
    return ("starting medicine task")
def fetch_the_medicine_bottle():
    return ("fetching the medicine value")
def correct_bottle():
    return ("Corrrect bottle")
def incorrect_bottle():
    return ("Incorrect bottle")
def bottle_done():
    return ("Bottle task done")
def start_bedding_task():
    return ("Starting bedding task")
def hold_blanket():
    return ("Holding blanket")
def start_bedding():
    return ("Starting bedding")
def pause_bedding():
    return ("Pausing bedding")
def bedding_done():
    return ("Bedding task done")
def done():
    return ("Done")
FullDictionary = {"START DRAWER TASK" : start_drawer_task, "OPEN" : 
                    open_drawer, "CLOSE" : close_drawer, "DONE" : done, 
                    "START GARMENT TASK" : start_garment_task, "HOLD" : hold_garment,
                    "WRAP" : start_wrapping, "RELEASE" : let_go, 
                    "START MEDICINE TASK" : start_medicine_task, 
                    "FETCH" : fetch_the_medicine_bottle,
                    "CORRECT" : correct_bottle, "INCORRECT" : incorrect_bottle, 
                    "COMPLETE" : bottle_done, "START BEDDING TASK" : start_bedding_task, 
                    "GRASP" : hold_blanket, "MAKE" : start_bedding,
                    "PAUSE" : pause_bedding, "FINISH" : bedding_done  }


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('voice', anonymous=True)

    rospy.Subscriber('command', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

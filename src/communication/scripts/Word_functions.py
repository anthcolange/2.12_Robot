import pyttsx

def approach():
    return ("going to drawer","going to drawer")
def open_arm():
    return  ("opening gripper","opening gripper")
def close_arm():
    return ("closing gripper","closing gripper")
def unlock():
    return ("opening drawer", "opening drawer")
def push():
    return ("closing drawer", "closing drawer")
def wrap():
    return ("wrapping garment", "wrapping garment")
def retrieve():
    return("retrieving bottle", "retrieving bottle")
def complete():
    return ("task complete", "task complete")
def green_bottle():
    return ("bottle is green", "bottle is green")
def blue_bottle():
    return ("bottle is blue","bottle is blue")
def red_bottle():
    return ("bottle is red","bottle is red")
def purple_obstacle():
    return ("obstacle is purple","obstacle is purple")
def green_obstacle():
    return ("obstacle is green", "obstacle is green")
def make():
    return ("making bed","making bed")
def return():
    return ("garment task complete","garment task complete")


FullDictionary = {"APPROACH" : approach, "OPEN" : 
                    open_arm, "CLOTHES" : close_arm, "UNLOCK" : unlock, 
                    "RAP" : wrap, "PUSH" : push,  
                    "RETRIEVE" : retrieve, 
                    "COMPLETE" : complete, 
                     "MAKE" : make, "RETURN" : return
                    "GREEN" : green_bottle, "BLUE" : blue_bottle, 
                    "RED" : red_bottle  }
FullDictionary_Nav= {"PURPLE" : purple_obstacle, "GRASS" : 
                    green_obstacle}

WordList=["APPROACH", "OPEN", "CLOTHES", "UNLOCK", "PUSH", "RETRIEVE", "COMPLETE", "MAKE", "GREEN", "BLUE",
        "RED", "RAP", "RETURN"]
WordList_Nav=["PURPLE","GRASS"]
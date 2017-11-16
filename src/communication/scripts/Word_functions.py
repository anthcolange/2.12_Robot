def start_drawer_task ():
    return ("starting drawer task",'1')
def open_drawer():
    return  ("opening drawer",'2')
def close_drawer():
    return ("closing drawer",'3')
def drawer_done():
    return ("drawer task done",'4')
def start_garment_task():
    return ("starting garment task",'5')
def hold_garment():
    return  ("holding garment",'6')
def start_wrapping():
    return ("starting wrapping",'7')
def let_go():
    return  ("letting go",'8')
def start_medicine_task():
    return ("starting medicine task",'9')
def fetch_the_medicine_bottle():
    return ("fetching the medicine value",'10')
def correct_bottle():
    return ("Corrrect bottle",'11')
def incorrect_bottle():
    return ("Incorrect bottle",'12')
def bottle_done():
    return ("Bottle task done",'13')
def start_bedding_task():
    return ("Starting bedding task",'14')
def hold_blanket():
    return ("Holding blanket",'15')
def start_bedding():
    return ("Starting bedding",'16')
def pause_bedding():
    return ("Pausing bedding",'17')
def bedding_done():
    return ("Bedding task done",'18')
def done():
    return ("Done",'19')
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

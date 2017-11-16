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
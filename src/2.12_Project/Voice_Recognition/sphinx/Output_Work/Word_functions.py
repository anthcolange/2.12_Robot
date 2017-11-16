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
FullDictionary = {"start" : start_drawer_task(), "open" : 
					open_drawer(), "close" : close_drawer(), "done" : drawer_done(), 
					"begin" : start_garment_task(), "hold" : hold_garment(),
					"wrap" : start_wrapping(), "release" : let_go(), 
					"commence" : start_medicine_task(), 
					"fetch" : fetch_the_medicine_bottle(),
					"correct" : correct_bottle(), "wrong" : incorrect_bottle(), 
					"complete" : bottle_done(), "bedding" : start_bedding_task(), 
					"grasp" : hold_blanket(), "make" : start_bedding(),
					"pause" : pause_bedding(), "finish" : bedding_done()  }


#start S T AA R T
#open OW P AH N
#close K L OW S
#done D AH N
#begin B IH G IH N
#hold HH OW L D
#wrap R AE P
#release R IY L IY S
#commence K AH M EH N S
#fetch F EH CH
#correct K ER EH K T
#wrong R AO NG
#complete K AH M P L IY T
#bedding B EH D IH NG
#grasp G R AE S P
#make M EY K
#pause P AO Z
#finish F IH N IH SH
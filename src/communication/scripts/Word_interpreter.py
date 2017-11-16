#import Word_functions  #File containing functions for voice commands
#check=0 #Initialize length of file as 0
#while True: #Run Continuously
#	with open('speechoutput.txt') as Wordfile: #Import data from text file of words written
#			data=Wordfile.readlines() #List containing different line in each index 
#			if (len(data)>check): #If length of file has changed from last check, there is a new command to act on
#				if data[check] in Word_functions.FullDictionary:
#					x=data[check]
#					check=check+1 #Update check to be length of file currently
#					print (Word_functions.FullDictionary[x])

# import Word_functions  #File containing functions for voice commands
# check=0 #Initialize length of file as 0
# while True: #Run Continuously
# 	with open('speechoutput.txt', "w+") as Wordfile: #Import data from text file of words written
# 			#data=Wordfile.readlines() #List containing different line in each index 
# 			Wordfile.seek(0)
# 			data = Wordfile.readline()
# 			#if (len(data)>check): #If length of file has changed from last check, there is a new command to act on
# 				#if data[check] in Word_functions.FullDictionary:
# 			if data in Word_functions.FullDictionary:
# 				#x=data[check]
# 				#check=check+1 #Update check to be length of file currently
# 				print("I should do something")
# 				#print (Word_functions.FullDictionary[x])
# 				print(Word_functions.FullDictionary[data])
# 				Wordfile.seek(0)
# 				#Wordfile.truncate()
# 				print("Now it is deleted")

import Word_functions  #File containing functions for voice commands
with open('speechoutput.txt', "r+") as Wordfile:
	while True: #Run Continuously
			data = Wordfile.readline()
			to_truncate = bool(data)
			data = data[:-1] #get rid of new line
			while "\x00" in data:
				i = data.index('\x00')
				data = data[i+1:]
			if data:
				if data in Word_functions.FullDictionary:
					print(len(data), data)
					print(Word_functions.FullDictionary[data]())
				else:
					print(data, "not in dictionary")
			if to_truncate:
				Wordfile.seek(0)
				Wordfile.truncate()
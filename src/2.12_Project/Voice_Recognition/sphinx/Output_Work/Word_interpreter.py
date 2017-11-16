import Word_functions  #File containing functions for voice commands
check=0 #Initialize length of file as 0
while True: #Run Continuously
	with open('output.txt') as Wordfile: #Import data from text file of words written
			data=Wordfile.readlines() #List containing different line in each index 
			if (len(data)>check): #If length of file has changed from last check, there is a new command to act on
				if data[-1] in Word_functions.FullDictionary:
					check=len(data) #Update check to be length of file currently
					x=data[-1]
					print (Word_functions.FullDictionary[x])
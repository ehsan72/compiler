
print("test")
def scanner():
	""
	with open("code.ll") as f:
		while True:
			c = f.read(1)
			if not c:
				print ("End of file")
				break	
			print ("Read a character:", c)
			
	return
scanner()


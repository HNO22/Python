print("\n\n__________Animal Game__________")

#The game about gussing the animal with 3 giving hints

print("\nI will give you 3 hints. guess what animal I am")
print("I have exceptional memory")

class Animals(object):
	"""docstring for ClassName"""
	def __init__(self, name, sort):
		self.name = name 
		self.sort = sort

	def guess_who_am_i(self):
		count = 0
		sort1 = Animals.sort(self.name)
		
		while (count < 3):
			hs = hints[sort1][count]
			guess1=input("Who am I ?")
			if guess1 == str(self.name()):
				print('You got it! I am'+str(self.name))
				break
			else:
				print("Nope, try again !!\n")
			count += 1
			break
		else:
			print("Done")
x = ["elephant", "tiger", "bat"]
hints= ["I am the biggest cat","I come in black and white or orange and black","I live in the jungle",
		"I use echo-location","I can fly","I see well in dark",
		"I am the largest land-living mammal in the world","I have big ears","I have 2 tusks"]
Animal_class = Animals(x)
Animal_class.guess_who_am_i()
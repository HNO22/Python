print("\n\n__________Animal Game__________")

#The game about gussing the animal with 3 giving hints
print("\nI will give you 3 hints. guess what animal I am")

class Animals(object):
	"""docstring for ClassName"""

	def __init__(self, name):
		self.name =name

	def guess_who_am_i(self):
		count = 0
		for h in (hint[self.name]):
			print("\nHint"+ str(count+1 ) +": "+ h)
			guess1=input("Who am I? ")

			if guess1 == str(self.name):
				print('You got it! I am '+str(self.name))
						
				play= input("\nDo you want play again?")
				if play =="yes":
					break	
				else: 
					print("Done, Bye Bye")
					exit()
				
			else:
				print("Nope, try again !!\n")
		
				count += 1
				

hint= {"tiger": ["I am the biggest cat","I come in black and white or orange and black","I live in the jungle"],
		"bat":["I use echo-location","I can fly","I see well in dark"],
		"elephant":["I have exceptional memory","I am the largest land-living mammal in the world","I have 2 tusks"]}

t = Animals("tiger")
b = Animals("bat")
e = Animals("elephant")

t.guess_who_am_i()
b.guess_who_am_i()
e.guess_who_am_i()
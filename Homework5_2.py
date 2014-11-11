from random import randrange

print("\n\n__________Integer Divisions__________")
	
#The game about learning 'Integer Divisions' for kids

try:
	play = "yes"
	while (play == "yes"):
		a = randrange(5)
		x = randrange(5)
		if (x != 0):
			answer = a // x 
			print ("  Integer Divisions of "+ str(a)+"/" + str(x))
			guess = input ("  ")
			if answer == int(guess):
				print ("  CORRECT !")
			else:
				print("  INCORRECT, try again")
		play = input("  Do you want to play more? ")
	else:
		print("  Thanks for playing\n")

except ValueError:
    print("  ERROR: Please enter Integers Only!\n")
    pass

except ZeroDivisionError:
	print("  ERROR: progaram error, please try again\n")
	pass

except Exception as h:
    print("  ERROR: Unexpected error\n")
    pass
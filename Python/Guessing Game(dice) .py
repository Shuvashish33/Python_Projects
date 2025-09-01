#Guessing Game(dice)
import random
for i in range(13):
	x=int(input("Pick a guess from 1 to 6:"))
	randomNumber=random.randint(1,6)
	if x==randomNumber:
		print('You have won!')
	else:
		print('You have lost, Try again!')
		print("Random number was",randomNumber)
		
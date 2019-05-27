import random
num = random.randint(1,10)

while True :
	guess=input("Guess a number between 1 to 10 : ")
	guess=int(guess)
	if guess<num:
		print("Too Low, try again!")
	elif guess>num:
		print("Too High, try again!")
	else :
		print("HURRAY, you guessed it right!!")
		again=input("Do you want to play again? (y/n)")
		if again == "y":
			num = random.randint(1,10)
			guess = None
		else :
			print("Thannk You for playing!")
			break

	




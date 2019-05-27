import random

print("\n\n\n\n          ****** WELCOME TO ROCK PAPER SCISSORS ***** ")
print("\n1.VS Player\n2.VS Computer")
ch=input("\nchoose the mode : ")
print("    enter 'quit' to exit \n")
if ch=="1":
	count1=0
	count2=0
	times=input("enter the points upto which you want to play(1-5) : ")	
	name1=input("player 1 enter your name : ")
	name2=input("player 2 enter your name : ")
	times=int(times)
	for i in range(times):
		print(f"\n {name1} : {count1}   {name2} : {count2} ")	
		move1=input(f"\n{name1}, make your move : ")
		move2=input(f"\n{name2}, make your move : ")
		if move1=="quit" or move2=="quit" : 
			break
		if move1==move2:
			print("  IT'S A TIE !!  ")
		elif move1=="rock":
			if move2=="paper":
				print(f" {name2} WINS !! ")
				count2+=1	
			elif move2=="scissor":
				print(f" {name1} WINS !! ")
				count1+=1
		elif move1=="paper":
			if move2=="rock":
				print(f"{name1} WINS !! ")
				count1+=1
			elif move2=="scissor":
				print(f"{name2} WINS !! ")
				count2+=1
		elif move1=="scissor":
			if move2=="paper":
				print(f"{name1} WINS !! ")
				count1+=1
			elif move2=="rock":
				print(f"{name2} WINS !! ")
				count2+=1		
		else: print(" INVALID MOVE !! ")
	if count1>count2 : 
		print(f"\n{name1} WON !!")
	elif count1==count2 : 
		print("\nIT'S A TIE !")
	else : print(f"\n{name2} WON !!")	


elif ch=="2":
	count1=0
	count2=0
	turns=3
	while count1<turns and count2<turns : 
		print(f"\n player : {count1}   computer : {count2} \n")
		player=input("make your move : ")
		if player=="quit" : 
			break
		move=random.randint(0,2)  # generate number from 0 to 2
		if move==0:
			computer="rock"
		elif move==1:
			computer="paper"
		else: computer="scissor"
		
		print(f"Computer plays : {computer}")                        	
		if player==computer:                                   
			print("  IT'S A TIE !!  ")
		elif player=="rock":
			if computer=="paper":
				print(" COMPUTER WINS !! ")
				count2+=1			
			elif computer=="scissor":
				print(" YOU WIN !! ")
				count1+=1
		elif player=="paper":
			if computer=="rock":
				print("YOU WIN !! ")
				count1+=1
			elif computer=="scissor":
				print("COMPUTER WINS !! ")
				count2+=1
		elif player=="scissor":
			if computer=="paper":
				print("YOU WIN !! ")
				count1+=1
			elif computer=="rock":
				print("COMPUTER WINS !! ")
				count2+=1
		else: print(" INVALID MOVE !! ")
	if count1>count2 : 
		print("CONGRATS, YOU WON!")
	elif count1==count2 : 
		print("IT'S A TIE !")
	else : print("SORRY, YOU LOST THE GAME !")		
	

	
			
	







	


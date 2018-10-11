a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("--------------------")
	print(a[3],'|',a[4],'|',a[5])
	print("--------------------")
	print(a[6],'|',a[7],'|',a[8])
printboard()

'''playeroneturn=True

while True:
	printboard()
	p=int(input("choose your place >>"))
	if(p in a):
		if playeroneturn:
			#p=input("choose your place,Playerone 1 >>")
			print("player one choose:",p)
			a[p-1]= 'X'		
			playeroneturn = not playeroneturn
		else:
			#p=input("choose your place,Playerone 2 >>")
			print("player two  choose:",p)
			a[p-1]= 'O'		
			playeroneturn = not playeroneturn
		#for winning condition
		for i in (0,1,2):
			if (a[i]==a[i+1] and a[i]==a[i+2]):
				if a=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
		for i in range(3):
			if (a[i]==a[i+3] and a[i]==a[i+6]):
				if a=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
		if(a[2]==a[4] and a[2]==a[6]):
			if a=='X':
				print("player 1 wins")
			else:
				print("player 2 wins")

		if(a[0]==a[4] and a[0]==a[8]):
			if a=='O':
				print("player 2 wins")
			else:
				print("player 1 wins")
					
	else:
		continue'''
import random
from time import sleep
from os import system

a=[1,2,3,4,5,6,7,8,9]
def printboard():
	system('clear')
	print(a[0],'|',a[1],'|',a[2])
	print("---------")
	print(a[3],'|',a[4],'|',a[5])
	print("---------")
	print(a[6],'|',a[7],'|',a[8])
	print("---------")

def possibilities():
	l = []
	for i in a:
		if (i!='X' and i != 'O'):
			l.append(i)
	return l

def compTurn():
	temp = possibilities()
	k = random.choice(temp)
	return k

pl1=True
while True:

	printboard()
	if pl1:
		p=int(input("Choose your place"))
		if(p in a):
			print("Player 1 chose",p)
			a[p-1]='X'
			pl1 = not pl1
	else:
		w = compTurn()
		print("Computer chose",w)
		sleep(3)
		a[int(w)-1]='O'
		pl1 = not pl1

	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			printboard()
			if(a[i]=='X'):
				print("Player 1 wins")
				exit()
			else:
				print("Computer wins")
				exit()

	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			printboard()
			if(a[i]=='X'):
				print("Player 1 wins")
				exit()
			else:
				print("Computer wins")
				exit()

	if(a[0]==a[4] and a[0]==a[8]): 				
		printboard()
		if(a[0]=='X'):
				print("Player 1 wins")
				exit()
		else:
				print("Computer wins")
				exit()

	elif(a[2]==a[4] and a[2]==a[6]): 
		printboard()
		if(a[2]=='X'):
				print("Player 1 wins")
				exit()
		else:
				print("Computer wins")
				exit()
	t = possibilities()
	if len(t) == 0:
		printboard()
		print("It's a tie ...")
		exit()				
		
		

a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("--------------------")
	print(a[3],'|',a[4],'|',a[5])
	print("--------------------")
	print(a[6],'|',a[7],'|',a[8])
printboard()

playeroneturn=True

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
		continue		
		
		

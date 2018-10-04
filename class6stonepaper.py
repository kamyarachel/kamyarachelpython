import random
a=0
b=0
while a<3 and b<3:
    r={1:'r',2:'p',3:'s'}
    comp=r[random.randint(1,3)]
    print(comp)
    p2=input("enter you choice r/p/s or q to quit")
	if p2=='q':
			print("bye")
			exit()
	if p2==p1:
		print("tie!!")
	elif p2=='r':
		if p1=='p':
			print("player 1 got the point")
			a=a+1
		else:
			print("player 2 got the point")
			b=b+1
	elif p2=='p':
		if p1=='r':
			print("player 2 got the point")
			b=b+1
		else:
			print("player 1 got the point")
			a=a+1
	elif p2=='s':
		if p1=='p':
			print("player 2 got the point")
			b=b+1
		else:
			print ("player 1 got the point")
			a=a+1
	if a==3:
		print("u won")
	elif b==3:
		print("comp won")








 
	
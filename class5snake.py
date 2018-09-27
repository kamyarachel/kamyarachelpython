import random
x=0
while True:
	n=input("enter q to quit and r to roll the dice")
	if(n=='q'):
		print("bye")
		exit()
	elif(n=='r'):
		r=random.randint(1,6)
		print("your score is",x)
		x=x+r
		print("score is",x)
		if(x==8):
			x=37
			print("hurray!!! you got a ladder your score is",x)
		elif(x==11):
			x=2
			print("oops!! you have been eatten by a snakeyour score is",x)
		elif(x==13):
			x=34
			print("hurray!!! you got a ladder your score is",x)
		elif(x==38):
			x=9
			print("opps!!! you have been eatten by a snake your score is",x)
		elif(x==40):
			x=68
			print("hurray!!! you got a ladder your score is",x)
		elif(x==52):
			x=81
			print("hurray!!! you got  a ladder your score is",x)
		elif(x==65):
			x=46
			print("opps!!! you have been eatten by a snake your score is",x)
		elif(x==76):
			x=97
			print("hurray!!! you got a ladder your score is",x)
		elif(x==89):
			x=70
			print("opps!!! you have been eatten by a snake your score is",x)
		elif(x==93):
			x=64
			print("opps!!! you have been eatten by a snake your score is",x)
		elif(x==100):
			x=100
			print("hurray!!!! you won")
  


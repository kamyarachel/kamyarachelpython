import random
p1={1:'r',2:'p',3:'s'}
r=random.randint(1,3)
print(r)
while True:
	p2=input("enter you choice r/p/s")
	if p2==p1:
		print("tie!!")
	elif p2==r:
		if p1==p:
			print("player 1 got the point")
	else:
			print("player 2 got the point")
	elif p2==p:
		if p1==r:
			print("player 2 got the point")
	else:
			print("player 1 got the point")
	elif p2==s:
		if p1==p:
			print("player 2 got the point")
	else:
			print ("player 1 got the point")






 
	
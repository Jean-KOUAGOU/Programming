import random
A=['T','H']
m=0
R=[]
if len(R)<2 :
	R.append(random.choice(A))
	m+=1
while R[len(R)-2]+R[len(R)-1]!=['H','H']:
	R.append(random.choice(A))
	m+=1
print(m)
print()
print(R)
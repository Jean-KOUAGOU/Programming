from math import*

Periodic_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,16,20,22,25,29,36,37,41,42,52,50,49,59,137,106,58,89,145,85,97,81,61]

def F(n):
	f=floor(n/100)
	res1=(((n/100)-f)*100)
	s=floor(res1/10)
	res2=(((res1/10-s)*10))
	return (f**2+s**2+(res2)**2)
print("Enter an integer with 3 digits\n")
print()
n=int(input())
print(F(n))
N=n
kmax=1000000000
k=0
if (n in Periodic_numbers)==True:
	print('\nThe number gives a periodic sequence\n')
else:
	while (N in Periodic_numbers)==False and k<kmax:
		N=F(N)
		print(N)
		k+=1
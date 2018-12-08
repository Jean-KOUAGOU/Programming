#print('enter a whole number\n')
#n=int(input())
#def f(t):
#	if t==0 or t==1:
#		return 1
#	else:
#		return f(t-1)+f(t-2)

#print('\nF(',n,') =',f(n),'\n')

from math import*

Periodic_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,16,20,22,25,513,29,36,37,41,42,52,50,49,59,137,106,58,89,145,85,97,81,61]

def F(n):
    f=floor((n/100))
    res1=floor(((n/100)-f)*10)
    s=n-(10*f+res1)*10
    result=f**2+s**2+res1**2
    return result

def f(n):
    #print("\nFor ",n,":")
    k=0
    kmax=15
    if (n in Periodic_numbers)==True:
        pass
        #print('\nThe number',n,'gives a periodic sequence\n')
    else:
        N=n
        while (N in Periodic_numbers)==False and k<kmax:
            N=F(N)
            #print(N)
            k+=1
        if k==kmax:
            return n

def f_check(n):
    #print("\nFor ",n,":")
    k=0
    kmax=15
    N=n
    print(N, ':')
    while k<kmax:
    	print(N, end='  ')
    	N=F(N)
    	k+=1

print('The following numbers are not periodic: \n')
Tab=[]
for i in range(1,244):
    Tab+=[f(i)]
print(Tab)
for i in Periodic_numbers:
	f_check(i)
	print("\n\n")


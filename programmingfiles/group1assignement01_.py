# Cube function
from math import*

Periodic_numbers_C=[1,2,3,4,5,6,7,8,9,919,407,1459,858,1449,1944,1914,1941,588,1149,795,1197,1074,408,576,684,792,1080,513,468,370,99,730,1009,664,952,862,853,586,736,592,286,628,244,19,54,189,1242,18,153,134,125,92,737,713,73,370,371,512,351,352,16,17,155,251,18,27,343,118,18,133,224,37,28,225,141,66,432,1458,72,351,52,17,59,29]

def F_cube(n):
    f1=floor((n/1000))
    res1=floor(((n/1000)-f1)*10)
    res2=floor(n/10-(f1*100+res1*10))
    s=n-(1000*f1+res1*100+res2*10)
    result=f1**3+s**3+res1**3+res2**3
    return result

def f_cube(n):
    #print("\nFor ",n,":")
    k=0
    kmax=15
    if (n in Periodic_numbers_C)==True:
        pass
        #print('\nThe number',n,'gives a periodic sequence\n')
    else:
        N=n
        while (N in Periodic_numbers_C)==False and k<kmax:
            N=F_cube(N)
            #print(N)
            k+=1
        if k==kmax:
            return n
def f_cube_check(n):
    #print("\nFor ",n,":")
    k=0
    kmax=15
    N=n
    print(N,':')
    while k<kmax:
    	print(N, end='  ')
    	N=F_cube(N)
    	k+=1	            
#print('The following numbers are not periodic: \n')
#Tab1=[]
#for i in range(1,2917):
    #Tab1+=[f_cube(i)]

#print(Tab1)
#print('\n\nSo all the numbers are periodic and we can reply Yes to the question\n')
for i in Periodic_numbers_C:
	f_cube_check(i)
	print("\n\n")
    



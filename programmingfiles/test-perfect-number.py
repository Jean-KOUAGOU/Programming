def test_perfect():
	s=0
	n=int(input("Enter an integer please\n"))
	for i in range(1,n):
		if n%i==0:
			s+=i
	if s==n:
		print()
		print(n,'is a perfect number.\n')
	else:
		print()
		print(n,'is not a perfect number.\n')
test_perfect()		
				
  	
  try:
    print("You have some coins for p and q Rands and you would like to buy something costing N Rands and you don't know how to proceed,")
    print("Please enter N, p and q in this order\n")
    N=int(input())
    p=int(input())
    q=int(input())
    Min=min(p,q)
    Max=max(p,q)
    def Proceed(N,p,q):
        n,m,k=0,0,N//Max
        while k>0:
            if (N-Max*k)%Min==0:
                n=k
                m=int((N-Max*k)/Min)
                break
            k-=1
        print("\n",N,"=",n,"x",Max,"+",m,"x",Min,"\n")
    Proceed(N,p,q)
except ValueError:
    print("You didn't respect assignment\n")
                    
                    
  	
  
  				
   	
  

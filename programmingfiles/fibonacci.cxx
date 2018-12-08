#include<iostream>
#include<math.h>
using namespace std;
int fibnac(int);
int main(void){
	int x;
	cout<<"Enter the rank of the fibonnaci therm: ";
	cin>>x;
	cout<<"\nThe therm is: "<<fibnac(x)<< endl;
	return 0;
	}
int fibnac(int n){
	if (n==0 or n==1) 
		return 1;
	else 
		return fibnac(n-1)+fibnac(n-2);
}
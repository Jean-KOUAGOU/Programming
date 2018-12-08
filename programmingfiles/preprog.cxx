#include<iostream>
#include<math.h>
using namespace std;
float f(int);
int main() {
float x;
cout << "Enter a number"<< endl;
cin >> x;
cout << "square root of " << x<< ":"<<f(x);
return 0;
}
float f(int t){
	return sqrt(t);
	}
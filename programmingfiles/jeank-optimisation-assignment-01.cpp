//all the questions
#include <iostream>
#include <math.h>
#include <iomanip>
#include <limits>
#include<chrono>
#include<vector>
#include<array>
using std::cout;
using std::cin;
using std::endl;
using std::setprecision;
using std::setw;
using std::fixed;
using std::vector;
using std::array;
using namespace std::chrono;
void collatz(int);
bool isPrime(int);
void printPrimes(int);
//Question 3 functions
int pow_recursive(int, int),pow_iterative(int, int), recursive_2(int, int),iterative_2(int, int) ;
//Question 4 functions
float solutions_1(float);
double solutions_2(double);
//Question 5 functions
double tent_map(double);
double tent_map_change(double);
//Question 6 functions
//a)
double root_iterative (double, int, int);
//b)
double pow_iterative_with_new_types (double, int);
//c)
void test_root (double, int, int);

//7.
//7.b function
void max_min(vector<int>);
//7.c function
vector<int> reverse ( vector<int> );
//8. functions
array<double, 2> read_point();
vector<array<double, 2>> read_problem();
vector<array<double, 2>> convexhull();
double min_element(vector<double>);

int main () {
            cout<<"\n\n******** KOUAGOU N. JEAN**********************\n\n";
            cout<<"\n\n All the questions are in this cpp file \n\n";
            //Question 1
            cout<<"\n Question 1\n";
            int n1;
            cout<<" Enter a positive integer for Collatz function : "<<endl;
            cin>>n1;
            cout<<""<<endl;
            collatz(n1);
            //Question 2
            int upto;
            cout<<"\n Question 2. \n";
            cout<<" Enter upto : ";
            cin>>upto;
            cout<<" Is prime : "<<isPrime(upto)<<endl;
            cout<<" Prime numbers up to "<<upto<<" : \n";
            printPrimes(upto);
            //Question 3
            cout<<"\n\n Powers of an integer \n";
            int q;
            cout<<"\n Enter q to compute its powers : ";
            cin>>q;
            int n2;
            cout<<"\n Enter n2, the exponent of q : ";
            cin>>n2;
            cout<<" Here we compute the powers by different methods and measure the time \n";
            //measures the time of execution for naive recursive implementation
            auto start1 = high_resolution_clock::now();
            cout<<q<< "^"<<n2<< " with the first recursive implementation is :"<<pow_recursive(q,n2)<<endl;
            auto stop1 = high_resolution_clock::now();
            auto duration1 = duration_cast<microseconds>(stop1 - start1);
            cout<<q<< "^"<<n2<< " with the first iterative implementation is :"<<pow_iterative(q,n2)<<endl;
            //measures the time of execution for efficient recursive implementation
            auto start2 = high_resolution_clock::now();
            cout<<q<< "^"<<n2<<" with the efficient recursive implementation is :"<<recursive_2(q,n2)<<endl;
            auto stop2 = high_resolution_clock::now();
            auto duration2 = duration_cast<microseconds>(stop2 - start2);
            //Display of the time measured for each method
            cout <<" Duration for naive iteration implementationb : "<< duration1.count() << " microseconds "<<endl;
            cout <<" Duration for efficient iteration implementation : "<< duration2.count() << " microseconds " << endl;
            //Question 4
            cout<<"\n Question 4. \n";
            //x to input in the function solution2 to approximate a solution of x+1=1 with the type double
            double x;
            //y to input in the function solution1 to approximate a solution of x+1=1 with the type float
            float y;
            cout<<" Enter x :\n";
            cin>>x;
            cout<<" Enter y :\n";
            cin>>y;
            cout <<"Smallest solution with float-type : "<< setprecision(20) <<solutions_1(y)<<endl;
            cout <<"Smallest solution with double-type : "<< setprecision(20) <<solutions_2(x)<<"\n\n";
            float smallest=std::numeric_limits<float>::min();
            double Smallest=std::numeric_limits<double>::min();
            cout<<"\nSmallest positive float : "<<smallest<<endl;
            cout<<"\nSmallest positive double : "<<Smallest<<endl;
            cout<<"\n\n So the solutions we find are not the smallest positive number that can be represented. \n";

            //Question 5
            cout<<"\n Question 5.a) \n";
            //We need to compute the sequence x_i
            cout<<"We need to compute the sequence x_i with the first expression of f(x) \n";
            x=0.01401;
            cout<<"\n"<<setprecision(5)<<x<<endl;
            for (int i=1; i<=100; i++) {
            x=tent_map(x);
            cout<<x<<setprecision(5)<<endl;
                                       }
            cout<<"\n To see the ploting, please refer to the pictures \n";

             //Question 5 b)

             cout<<"\n Question 5.b) ";
             //We need to compute the sequence x_i
             cout<<"We need to compute the sequence x_i with the second expression of f(x) \n";
             x=0.01401;
            cout<<"\n"<<setprecision(5)<<x<<endl;
            for (int i=1; i<=100; i++) {
            x=tent_map_change(x);
            cout<<setprecision(5)<<x<<endl;
                                        }
            cout<<"\n To see the ploting, please refer to the pictures \n";

            //Question 6 c

            cout<<"\n Question 6.\n\n";
            double q1;
            int n3, steps;
            cout<<" Enter q1 : ";
            cin>>q1;
            cout<<"\n Enter n3 : ";
            cin>>n3;
            cout<<"\n Enter the maximal number of steps you want : ";
            cin>>steps;
            cout<<"\n Approximation of q^(1/n) with q = "<<q1<<" and n = "<<n3<<" : "<<root_iterative(q1, n3, steps)<<endl;
            cout<<"\n If it did not converge, please incease the number of steps \n\n";
            cout<<" Here is to test the accuracy of root_iterative function \n";
            test_root(q1,n3,steps);
            cout<<"\n The result we get is consistent like when we look for the roots of a function using Newton's method";

            //Question 7

            cout<<" \n\nQuestion 7.\n";
            cout<<"\nQuestion 7.a \n";
            vector<int> v(10);
            v[1]=2;
            v[5]=-7;
            for (int i=0; i<v.size(); ++i) {
                cout<<v[i]<<"  ";
                                            }
            cout<<"\n So the values which are not specified are replaced by 0.\n";

            cout<<"\n Question 7.b \n";
            cout"\n Please enter integers ";
            vector<double> vr(10);
            for (int i=0; i<v.size(); ++i) {
            cout<<"Enter an element :";
            cin>>v[i];
                                            }

            cout<<"Minimum and maximum value of the vector : ";
            max_min(v);
            cout<<"\n Question 7.c Reverse of the vector : \n";
            for (int i=0; i<v.size(); ++i) {
                cout<<reverse(v)[i]<<" ";
                                           }
            cout<<"\n ";

           //7.d
           cout<<"\n Question 7.d Rounding the entries of a vector : \n\n";
           for (int i=0; i<vr.size(); ++i) {
            cout<<"Enter an element :";
            cin>>vr[i];
                                            }

            for (int i=0; i<vr.size(); ++i) {
                vr[i]=round(vr[i]);

                                            }
            cout<<"After rounding vr = : ";
            for (int i=0; i<vr.size(); ++i) {

                cout<<vr[i]<<"  ";
                                            }
            //7.e
            cout<<"\n Question 7.e Reversing a vector and saving the result in the same vector : \n\n";
            for (int i=0; i<vr.size(); ++i) {
            cout<<"Enter an element :";
            cin>>vr[i];
                                            }
            double sw;
            if (vr.size()%2==0) {
                for (int i=0; i<vr.size()/2; ++i) {
                sw = vr[i];
                vr[i]=vr[vr.size()-1-i];
                vr[vr.size()-1-i]=sw;

                                                  }
                                 }
            else {
                 for (int i=0; i<(vr.size()-1)/2; ++i) {
                sw = vr[i];
                vr[i]=vr[vr.size()-1-i];
                vr[vr.size()-1-i]=sw;

                                              }
                 }
            //Printing the vector after reversing
            cout<<"\n";
            cout<<"After reversing vr =  ";
            for (int i=0; i<vr.size(); ++i) {

                cout<<vr[i]<<"  ";
                                            }
             //Question 7.f
             cout<<"\n Question 7.f Reversing of a vector and saving the result in the same vector, but using swap : \n\n";
            if (vr.size()%2==0) {
                for (int i=0; i<vr.size()/2; ++i) {
                std::swap(vr[i], vr[vr.size()-1-i]);
                                            }
                                 }
            else {
                 for (int i=0; i<(vr.size()-1)/2; ++i) {
                std::swap(vr[i], vr[vr.size()-1-i]);
                                            }
                 }
            //Printing the vector after the second reversing process
            cout<<"\n\nAfter the second reversing using swap, vr=  ";

            for (int i=0; i<vr.size(); ++i) {

                cout<<vr[i]<<"  ";
                                            }
            cout<<"\n\n";

            //Question 8.

            read_problem();


            return 0;
                                  }

 // 1.
 void collatz(int n) {
      if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
      else {
          cout<<"The sequence is : "<<n<<" ";
          while (n!=1 and n>0) {
               if (n%2==0) {
                   n=n/2;
                   cout<<n<<" ";
                            }
                else {
                     n=3*n+1;
                     cout<<n<<" ";
                     }
                      }
            }
                        }
//2.
bool isPrime(int n) {
     if (cin.fail()) {
        cout<<"There is an error in your input \n";
                      }
      else {
      bool testprime=true;
      for (int divisor=2; divisor<=floor(sqrt(n)); ++divisor) {
           if (n%divisor==0) {
               testprime=false;
               break;
                             }
                                                               }
     return testprime;
            }
                    }
//2.
void printPrimes(int upto) {
     if (cin.fail()) {
        cout<<"There is an error in your input \n";
                      }
      else {
     for (int i=2; i<=upto; ++i)

          if (isPrime(i)==1) {
              cout<<i<<" ";
                             }

            }
                        }
//Question 3.
int pow_recursive(int y, int x) {
     if (cin.fail()) {
        cout<<"There is an error in your input \n";
        return 0;
                      }
      else {
     if (x==0) {
        return 1;
                }
     else {
        return y*pow_recursive(y,x-1);
          }
            }
                               }
//3
int recursive_2(int y, int x) {
    if (cin.fail()) {
       cout<<"There is an error in your input \n";
                    }
      else {
     if (x%2==0) {
        return pow_recursive (y*y,x/2);
            }
     else {
     return y*pow_recursive (y*y,(x-1)/2);
          }
            }
                               }
//3
int pow_iterative(int y, int x) {
    if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
    else {
    int i=1;
    int q=y;
    while (i<x) {
          q=q*y;
          ++i;
                }
    return q;
        }
                                 }
//3
 int iterative_2(int y, int x) {
     if (cin.fail()) {
              cout<<"There is an error in your input \n";
                     }
     else {
     if (x%2==0) {
     return pow_iterative(y*y,x/2);
        }
else {
      return y*pow_iterative (y*y,(x-1)/2);
     }
          }
                                 }
//4.a
float solutions_1(float x) {
      if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
    else {
        float x1=x;
        while (1.+x1!=1.) {
               x1 /= 10.;
                         }
        return x1;
        }
                           }
//4.b
double solutions_2(double x) {
       if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
       else {
            double x2=x;
            while (1.+x2!=1.) {
                   x2 /= 10.;
                             }
            return x2;
            }
                              }

//5.a
double tent_map(double x) {
       if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
       else {

       if (0.0<=x and x<0.5) {
          return 2.0*x;
                             }
        else return 2.0-(2.0*x);
             }
                           }
//5.b
double tent_map_change(double x) {
       if (cin.fail()) {
          cout<<"There is an error in your input \n";
                      }
       else {
       if (0.0<=x and x<0.5) {
          return 1.999999*x;
                           }
        else return 1.999999*(1-x);
            }
                                  }
//6.a)

double root_iterative (double q, int n, int steps) {
       if (cin.fail()) {
          cout<<"There is an error in your input \n";
          return 0;
                       }
       else {
           //double a=std::numeric_limits<double>::infinity();
           double a=pow(q, (1./n))+2;
           double a0=1.0;
           int s=0;
           while ((a-pow(q,(1./n))!=0) and (steps >0)) {
                 a=a0+(1.0/n)*(((q/(pow_iterative_with_new_types(a0,n-1)))-a0));
                 a0=a;
                 ++s;
                 --steps;

                                                        }
            //cout<<"\nNumber of steps taken out of "<<steps+s<<" : "<<s<<endl;
            return a;
            }
                                                      }
//6.b)

double pow_iterative_with_new_types (double y, int x) {
       if (cin.fail()) {
          cout<<"There is an error in your input \n";
          return 0;
                       }
    else {
    int i=1;
    double q=y;
    while (i<x) {
          q=q*y;
          ++i;
                }
    return q;
          }
                                                      }

// 6.c)
void test_root (double q, int n, int steps) {
      cout<<"\n Test of accuracy : "<<endl;
      cout<<" q : "<<q<<endl;
      cout<<" n : "<<n<<endl;
      cout<<" q^(1/n) : "<<root_iterative(q, n, steps)<<endl;
      cout<<" (q^(1/n))^n : "<<pow(root_iterative(q, n, steps), n)<<endl;
      cout<<" q-(q^(1/n))^n : "<<q-pow(root_iterative(q, n, steps), n)<<endl;

                                             }
//This function finds the minimum and the maximum of a vector
void max_min(vector<int> v) {
     int Min=v[0];
     int Max=v[0];
     for (int i=1; i<v.size(); ++i) {
         if (v[i]<Min) {
            Min=v[i];
                       }
          if (v[i]>Max) {
             Max=v[i];
                         }
                                     }
    cout<<Min<<"  and  ";
    cout<<Max<<"\n"<<endl;
                            }
//This function reverses a vector
vector<int> reverse (vector<int> v) {
            vector<int> vr(v.size());
            for (int i=v.size()-1; i>=0; --i) {
                vr[v.size()-1-i]=v[i];
                                            }
            return vr;
                                    }

array<double, 2> read_point() {

              array<double, 2> p;
              double x,y;
              cout<<"Enter the coordinate x : ";
              cin>>x;
              cout<<"Enter the coordinate y : ";
              cin>>y;
              p[0]=x;
              p[1]=y;
              return p;
                           }

vector<array<double, 2>> read_problem() {
                      vector<array<double, 2> > v;
                      int n;
                      cout<<"Enter the number of points : ";
                      cin>>n;
                      for (int i=0; i<n; ++i) {
                      cout<<"Point "<<i+1<<" : ";
                      v.push_back(read_point());

                                         }
                      return v;

                                     }

vector<array<double, 2>> convexhull() {
                         vector<int> pos;
                         vector<array<double, 2>> convset;
                         vector<array<double, 2>> V=read_problem();
                         vector<double> v(V.size());
                         for (int i=0; i<V.size();++i) {
                         v[i]=V[i][1];

                                                       }
//Step 1 point with the lowest y
                         for (int i=0; i<v.size(); ++i) {
                             if (V[i][1]==min_element(v)) {
                                pos.push_back(i);
                                                  }

                                                        }
                         if (pos.size()==1) {
                            convset.push_back(V[pos[0]]);
                                            }
                         else {
                              int j=pos[0];
                              double xmin=V[pos[0]][0];
                              for (int i=1; i<pos.size(); ++i) {
                                  if (V[pos[i]][0]<xmin) { j=pos[i];  }

                                                               }

                              convset.push_back(V[j]);
                               }

                                       }
double min_element(vector<double> v) {
       double Min=v[0];
       for (int i=1; i<v.size(); ++i) {
           if (v[i]<Min) {
            Min=v[i];
                         }
                                     }
       return Min;
                                      }
double anglebetween(array<double,2> v1, array<double, 2> v2 ) {
       return acos((v1[0]*v2[0]+v1[1]*v2[1])/(sqrt((v1[0]*v1[0]+v1[1]*v1[1])*(v2[0]*v2[0]+v2[1]*v2[1]))));
       //This function is not finished, I need more time to complete it

                                                               }



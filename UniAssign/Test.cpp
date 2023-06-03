#include <iostream>

using namespace std;


int main()
{
    int m=3,k=1,n;
    n%=(n=(m+=k)-3);
    cout << n<< endl;
}
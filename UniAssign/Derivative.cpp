#include <iostream>
#include <list>
#include <vector>
#include <iterator>

using namespace std;


void rec(list<double> )
{

}

int main()
{
    int n;
    cin >> n;
    vector<double> a(n + 1);
    list<double> polynomial;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        a[i] = -a[i];
    }

    polynomial.push_back(1);
    polynomial.push_back(a[0]);
    for (int i = 1; i < n; i++)
    {
        list<double> new_polynomial(polynomial);
        new_polynomial.push_front(0);
        polynomial.push_back(0);

        for (int j = 0; j < n + 1; j++)
        {
            list<double>::iterator it = new_polynomial.begin();
            advance(it, j);
            *it = *it * (a[i]);
            list<double>::iterator oit = polynomial.begin();
            advance(oit, j);
            *oit += *it;
        }
    }


    // for(auto x: polynomial)
    // {
    //     cout << x << " ";
    // }
    // cout << endl;
    
    list<double>::iterator itr = polynomial.begin();

    for (int i = 0; i < n + 1; i++)
    {
        *itr *= (n - i);
        advance(itr, 1);
    }
    
    itr = polynomial.begin();
    for (int i = 0; i < n; i++)
    {
        cout << *itr << "*x^" << (n - 1 - i) << " ";
        advance(itr, 1);
    }
    cout << endl;
}
#include <bits/stdc++.h>
#include <math.h>

using namespace std;

#define N 9

void factorial(int index, vector<long long> &vect)
{
    vect[index] *= vect[index - 1];
}


int main(void)
{
    long double x = 0.00;
    long double Ci = 0.00;
    long double gamma = 0.577215664901;
    vector<long long> fact(2*N + 2, 1);

    cout << "put x: " << '\n';
    cin >> x;

    for(int i = 1; i <= 2*N; i++)
    {
        fact[i] = i;
    }
    for (int i = 2; i <= 2*N; i++)
    {
        factorial(i, fact);
    }

    Ci = gamma + logl(x);
    for (int i = 1; i <= N; i++)
    {
        Ci += powl(-1, i) * powl(x, 2*i) / (2*x * fact[2*i]);
    }

    cout << fixed << setprecision(4) << Ci << '\n';
    return 0;

}
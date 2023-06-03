#include <bits/stdc++.h>

using namespace std;


void p(long index, vector<vector<long double>> &coeffs)
{
    if (index == 0) coeffs[0][0] = 1.00;
    else if (index == 1) coeffs[1][1] = 1.00;
    else
    {
        for (long i = 1; i <= index; i++)
        {
            coeffs[index][i] = coeffs[index - 1][i - 1] * static_cast<long double>(static_cast<long double>(2*index - 1) / static_cast<long double>(index));
            coeffs[index][i - 1] = -static_cast<long double>(coeffs[index - 2][i - 1] * static_cast<long double>((static_cast<long double>(index - 1))/ static_cast<long double>(index)));
        }
    }

}



int main(void)
{
    long n;
    cout << "write number n of Pn to get the coefficients: " << '\n';
    cin >> n;

    vector<vector<long double>> coeffs(n + 2, vector<long double>(n + 2, 0.00));


    for (long i = 0; i <= n; i++)
    {
        p(i, coeffs);
    }

    for (long i = 0; i <= n; i++)
    {
        cout << fixed << setprecision(3) << coeffs[n][i] << " ";
        //cout << '\n';
    }

    cout << '\n';
    return 0;

}
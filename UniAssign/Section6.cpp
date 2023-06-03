#include <bits/stdc++.h>
#include <math.h>

using namespace std;

// I guess limitation is 10^9 on n
// So I did for it
// O(log n)

#define MAX 1e9

long long n;


bool comp(long long k)
{
    long long tmp = 0;

    // k/2 + k/3 + k/5 - k/2*3 - k/2*5 - k/3*5 - k/2*3*5
    tmp = floorl(k/2ll) + floorl(k/3ll) + floorl(k/5ll) 
        - floorl(k/6ll) - floorl(k/10ll) - floorl(k/15ll) - floorl(k/30ll);

    return (tmp >= n);
}

long long binary(long long a, long long b)
{
    long long s = -1;
    for (long long i = b; i >= a; i /= 2)
    {
        while(!comp(i+s)) s += i;
    }

    return s + 1;
}


int main(void)
{
    cout << "put a number n: " << '\n';
    cin >> n;

    //cout << binary(1ll, MAX) << '\n';
    long long max_n = n + 10;
    for (long long i = n; i < max_n; i++)
    {
        n = i;
        cout << binary(1ll, MAX) << " ";
    }

    cout << '\n';
    // n += 10;
    // cout << binary(1ll, MAX) << '\n';
}

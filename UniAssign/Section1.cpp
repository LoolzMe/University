#include <bits/stdc++.h>

using namespace std;

long long evk(long long a, long long b)
{
    if (a < b) swap(a, b);

    if (b == 0) return a;
    return evk(b, a % b);
}

int main(void)
{
    long long a, b;

    cin >> a >> b;

    cout << a * b / evk(a, b) << '\n';

}
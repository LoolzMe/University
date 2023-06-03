#include <bits/stdc++.h>

using namespace std;

long long ackermann(long n, long x, long y)
{
    if (n == 0) return x + 1;
    if (y == 0)
    {
        switch (n)
        {
            case 1:
                return x;
                break;;
            case 2:
                return 0;
            case 3:
                return 1;
            default:
                return 2;
        }
    }

    return ackermann(n - 1, ackermann(n, x, y - 1), x);
}

int main(void)
{
    long long n, x, y;

    cout << "put ackermann's function variables (n, x, y): " << '\n';
    cin >> n >> x >> y;

    cout << ackermann(n, x, y) << '\n';

}
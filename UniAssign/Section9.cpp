#include <bits/stdc++.h>

using namespace std;

#define MAX 1e9

int main(void)
{
    long long n, m;
    long long tmp;

    cout << "put dimensions here (columns, rows): " << '\n';
    cin >> n >> m;

    vector<vector<long long>> matrix(n, vector<long long>(m, 0));

    long long min_tmp = MAX;
    cout << "put elements here: " << '\n';
    for (long long i = 0; i < n; i++)
    {
        for (long long j = 0; j < m; j++)
        {
            cin >> tmp;
            matrix[i][j] = tmp;
            min_tmp = min(tmp, min_tmp); 
        }
    }

    for (long long i = 0; i < n; i++)
    {
        for (long long j = 0; j < m; j++)
        {
            if (matrix[i][j] == min_tmp)
            {
                cout << i + 1 << " " << j + 1 << '\n'; 
            }
        }
    }

    return 0;
}
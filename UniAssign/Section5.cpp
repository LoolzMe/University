#include <bits/stdc++.h>
#include <math.h>

using namespace std;


bool comp(pair<long long, long double> a, pair<long long, long double> b)
{
    return (a.second < b.second);
}

int main()
{
    long n;

    cin >> n;
    vector<pair<long long, long double>> results(n); // number, result

    // long long tmp_a;
    // long double tmp_b;
    int k = 0;
    for (auto &x: results)
    {
        cin >> x.second;
        x.first = k;
        k++;
    }

    sort(results.begin(), results.end(), comp);

    long double mean = 0.0;

    for(int i = 0; i < min(5, (int)results.size()); i++)
    {
        cout << results[i].first + 1 << " ";
        mean += results[i].second;
    }
    cout << '\n';

    cout << mean / min(5, (int) results.size()) << '\n';



}
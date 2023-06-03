#include <bits/stdc++.h>

#define MAX 1e9

using namespace std;

void countOccurs(string str, map<long long, long long> &freq_array) 
{
    long long count = 0;
    for (string::iterator itr = str.begin(); itr != str.end(); itr++)
    {
        if (*itr == ' ')
        {
            freq_array[count]++;
            count = 0;
        }
        else count++;
        
    }

    if(count != 0) freq_array[count]++;

}

int main(void)
{
    map<long long, long long> freq_array;

    string file_name;

    cout << "file name: " << '\n';

    cin >> file_name;

    fstream file;
    file.open(file_name, ios::in);

    string line;
    
    //cout << file.is_open();
    while(getline(file, line))
    {
        countOccurs(line, freq_array);
    }


    //long double mean = 0.00;
    long long count = 0;
    for (auto x: freq_array)
    {
        count += x.second;
    }

    for (auto &x : freq_array)
    {
        // mean += x.first * x.second;
        cout << "length of word: " << x.first << " frequency: " << static_cast<double> (x.second) / static_cast<double> (count)<< '\n';
    }

}
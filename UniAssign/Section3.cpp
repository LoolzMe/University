#include <bits/stdc++.h>

using namespace std;

char * Strchr(char * s, int c)
{
    char ch = (char)c;
    //char * res;

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == ch)
        {
            return &s[i];
        }
    }

    return NULL;
}


int main(void)
{
    char * s;
    char c;
    int n;

    cout << "number of characters is your string: " << '\n';
    cin >> n;
    s = new char[n];
    cout << "your string: " << '\n';
    cin >> s;
    cout << "character you'd like to find: " << '\n';
    cin >> c;
    //c--;
    cout << "strchr result: " << *Strchr(s, c) << '\n';
    cout << "real (built-in) strchr result: " << *strchr(s, c) << '\n';

    delete s;

    return 0;
}
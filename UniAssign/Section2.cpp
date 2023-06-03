#include <bits/stdc++.h>
#include <math.h>

using namespace std;

#define MAX 300

typedef pair<string, long long> floatNumber;

string excludeZeros(string number)
{
    int index1 = 0, index2 = number.length();
    while(number[index1] == '0') ++index1;
    // while(number[index2 - 1] == '0') --index2;

    return number.substr(index1, index2);  
}


floatNumber multiply(floatNumber first_float_number, floatNumber second_float_number)
{
    string first_number = first_float_number.first;
    string second_number = second_float_number.first;
    
    int first_length = first_number.length();
    int second_length = second_number.length();

    if (first_length == 0 || second_length == 0) return floatNumber("0", 0);
    
    vector<int> result(first_length + second_length, 0);
 
    int i_n1 = 0;
    int i_n2 = 0;
    
    for (int i = first_length - 1; i >= 0; i--)
    {
        int carry = 0;
        int n1 = first_number[i] - '0';
 
        i_n2 = 0;
         
        for (int j= second_length - 1; j>=0; j--)
        {
            int n2 = second_number[j] - '0';
 
            int sum = n1*n2 + result[i_n1 + i_n2] + carry;
 
            carry = sum/10;
 
            result[i_n1 + i_n2] = sum % 10;
 
            i_n2++;
        }
 
        if (carry > 0)
            result[i_n1 + i_n2] += carry;
 
        i_n1++;
    }
 
    int i = result.size() - 1;
    while (i >= 0 && result[i] == 0)
    i--;
 
    if (i == -1)
    return floatNumber("0", 0);
 
    string s = "";
     
    while (i >= 0)
        s += to_string(result[i--]);
 
    return floatNumber(s, first_float_number.second + second_float_number.second);
}
 

floatNumber add(floatNumber first_number, floatNumber second_number)
{
    floatNumber result("", 0);

    long long diff1 = first_number.second;
    long long diff2 = second_number.second;
    long long diff = abs(diff1 - diff2);

    if (diff1 > diff2)
    {
        swap(first_number, second_number);
    }

    first_number.first += string(diff, '0');
    first_number.second += diff;
    string tmp_str = "";


    if (first_number.first.length() - first_number.second <= 0)
    {
        first_number.first.insert(0, string(first_number.first.length() - first_number.second + 1, '0'));
    }
    if (second_number.first.length() - second_number.second <= 0)
    {
        second_number.first.insert(0, string(second_number.first.length() - second_number.second + 1, '0'));
    }
    
    if (first_number.first.length() - first_number.second > second_number.first.length() - second_number.second) swap(first_number, second_number);

    long long diff_int = second_number.first.length() - second_number.second - first_number.first.length() + first_number.second;
    first_number.first.insert(0, string(diff_int, '0'));
    //diff = first_number.first

    int r = 0;
    int l = 0;

    for (long long i = first_number.first.length() - 1; i >= 0; i--)
    {
        l = r + static_cast<int>(first_number.first[i] - '0') + static_cast<int>(second_number.first[i] - '0');
        if (l >= 10)
        {
            r = 1;
            first_number.first[i] = to_string(l - 10)[0];
        }
        else {first_number.first[i] = to_string(l)[0]; r = 0;}
    }
    if (r)
    {
        first_number.first.insert(0, "1");
    }

    return floatNumber(first_number.first, first_number.second);

}


bool ifBigger(string first_number, string second_number)
{
    if (first_number.length() > second_number.length()) return true;
    else if (first_number.length() < second_number.length()) return false;
    else
    {
        for (long long i = 0; i < first_number.length(); i++)
        {
            if (first_number[i] > second_number[i]) return true;
            else if (first_number[i] < second_number[i]) return false;
            else { }

        }
        return false;
    }
}

bool ifBiggerEqual(string first_number, string second_number)
{
    if (first_number.length() > second_number.length()) return true;
    else if (first_number.length() < second_number.length()) return false;
    else
    {
        for (long long i = 0; i < first_number.length(); i++)
        {
            if (first_number[i] > second_number[i]) return true;
            else if (first_number[i] < second_number[i]) return false;
            else { }

        }
        return true;
    }
}

floatNumber subtraction(floatNumber first_number, floatNumber second_number)
{
    long long diff1 = first_number.second;

    long long diff2 = second_number.second;
    long long diff = abs(diff1 - diff2);

    if (diff1 > diff2)
    {
        swap(first_number, second_number);
    }

    first_number.first += string(diff, '0');
    first_number.second += diff;
    string tmp_str = "";

    if (first_number.first.length() - first_number.second <= 0)
    {
        first_number.first.insert(0, string(first_number.first.length() - first_number.second + 1, '0'));
    }
    if (second_number.first.length() - second_number.second <= 0)
    {
        second_number.first.insert(0, string(second_number.first.length() - second_number.second + 1, '0'));
    }
    
    if (first_number.first.length() - first_number.second > second_number.first.length() - second_number.second) swap(first_number, second_number);

    long long diff_int = second_number.first.length() - second_number.second - first_number.first.length() + first_number.second;
    first_number.first.insert(0, string(diff_int, '0'));
    //diff = first_number.first


    if (ifBigger(second_number.first, first_number.first)) swap(first_number, second_number);

    int r = 0;
    int l = 0;

    for (long long i = first_number.first.length() - 1; i >= 0; i--)
    {
        l = static_cast<int>(first_number.first[i] - '0') - static_cast<int>(second_number.first[i] - '0');
        if (l < 0)
        {
            first_number.first[i - 1]--;
            l += 10;
            first_number.first[i] = to_string(l)[0];
        }
        else {first_number.first[i] = to_string(l)[0];}
    }
    // if (r)
    // {
    //     first_number.first.insert(0, "1");
    // }

    return floatNumber(first_number.first, max(first_number.second, second_number.second));

}

floatNumber division(string number, string divisor)
{
    string ans;

    int count = 0;
    int index = 0;
    string tmp = "";
    tmp += number[index];

    while (ifBigger(divisor, tmp))
    {
        if (++index == number.length()) break;

        tmp += number[index];
    }
 
    while (number.size() > index) 
    {
        string whole_part = "1";
        while (ifBiggerEqual(tmp, multiply(floatNumber(whole_part, 0), floatNumber(divisor, 0)).first)) whole_part[0]++; 
        whole_part[0]--;
        ans += whole_part;

        if (++index == number.size())
            tmp = subtraction(floatNumber(tmp, 0), multiply(floatNumber(whole_part, 0), floatNumber(divisor, 0))).first;
        else 
            tmp = subtraction(floatNumber(tmp, 0), multiply(floatNumber(whole_part, 0), floatNumber(divisor, 0))).first + number[index];
    }
    //tmp.pop_back();

    tmp = excludeZeros(tmp);
    string zero = "0";
    if (ans.length() == 0) ans += "0";

    if (ifBigger(tmp, zero))
    {
        // tmp += "0";
        for (int i = 0; i < MAX; i++)
        {
            tmp = excludeZeros(tmp);

            if (!ifBigger(tmp, zero)) break;
            
            tmp += zero;
            string whole_part = "1";
            while (ifBiggerEqual(tmp, multiply(floatNumber(whole_part, 0), floatNumber(divisor, 0)).first)) whole_part[0]++; 
            whole_part[0]--;

            ans += whole_part;
            tmp = subtraction(floatNumber(tmp, 0), multiply(floatNumber(whole_part, 0), floatNumber(divisor, 0))).first;
            
            count++;
        }

    }

    if (ans.length() == 0) return floatNumber("0", 0);
 
    return floatNumber(ans, count);
}




int main(void)
{
    // cin >> a >> b;
    // floatNumber number(a, 0);
    // floatNumber number1(b, 0);

    // cout << add(number, number1).first << '\n';
    // cout << multiply(number, number1).first << '\n';

    floatNumber number("1", 0);
    floatNumber fact("1", 0);
    floatNumber power2("1", 0);
    floatNumber numerator("1", 0);
    int point = 1;
    int count = 1;
    for (int i = 1; i <= MAX/2; i++)
    {
        fact = multiply(floatNumber(to_string(i), 0), fact);
        power2 = multiply(floatNumber(to_string(2), 0), power2);
        if (i >= 2)
        {
            numerator = multiply(floatNumber(to_string(point), 0), numerator);
            point += 2;
        }
        if (i % 2 == 1)
        {
            number = add(number, division(numerator.first, multiply(power2, fact).first));
        }
        else
        {
            number = subtraction(number, division(numerator.first, multiply(power2, fact).first));
        }
        //number = add(number, division("1", fact.first));
        if (count * 100 <= i) {cout << i << '\n'; count++; }
    }

    cout << '\n';
    cout << number.first << " " << number.second << '\n';

    //cout << subtraction(floatNumber("095", 2), floatNumber("009", 2)).first << '\n';

    return 0;
}
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <random>
#include <string>
#include <vector>
#include <boost/range/adaptor/reversed.hpp>
using namespace std;

std::ifstream DATA1("DATA.2.dat", std::ios::in);
std::ifstream DATA2("DATA.3.dat", std::ios::in);


// DATA << T <<                                                // temperature
//             "\t" << M_avg << "\t" << Mabs_avg << "\t" << Msq_avg << //<M>;<|M|>;<M^2> per spin
//             "\t" << (Msq_avg-(M_avg * M_avg * n)) / (T) <<          // susceptibility per spin (X)
//             "\t" << (Msq_avg-(Mabs_avg * Mabs_avg * n)) / (T) <<    // susceptibility per spin (X’)
//             "\t" << E_avg << "\t" << Esq_avg <<                     //<E>;<E^2> per spin
//             "\t" << (Esq_avg-(E_avg * E_avg * n)) / (T * T) <<      // heat capacity (C) per spin
//             "\t" << 1-((Mq_avg) / (3 * Msq_avg)) << std::endl;           // cumulant (U_L)

int main()
{

    // int index_count = 0;

    vector<string> array10;
    vector<string> array16;
    while (DATA1)
    {
        string row;
        DATA1 >> row;
        array10.push_back(row);
        // cout << row << endl;
    }
    while (DATA2)
    {
        string row;
        DATA2 >> row;
        array16.push_back(row);
        // cout << row << endl;
    }


    // from 5 to 0.5, change = 0.1
    // if we wanna 2.2: i = (5 - 2.2) * 10 + {spec index}

    // accumulant
    vector<float> acc10;
    vector<float> acc16;
    string::size_type sz; 
    for (int i = 0; i < array10.size() / 10; i++)
    {
        if (i * 10 + 9 >= array10.size())
        {
            break;
        }

        acc10.push_back(stof(array10[i * 10 + 9]));
        acc16.push_back(stof(array16[i * 10 + 9]));

    }
    vector<float> mag10;
    vector<float> mag16;
    for (int i = 0; i < array10.size() / 10; i++)
    {
        if (i * 10 + 2 >= array10.size())
        {
            break;
        }

        mag10.push_back(stof(array10[i * 10 + 2]));
        mag16.push_back(stof(array16[i * 10 + 2]));

    }


    vector<float> cap10;
    vector<float> cap16;
    for (int i = 0; i < array10.size() / 10; i++)
    {
        if (i * 10 + 8 >= array10.size())
        {
            break;
        }

        cap10.push_back(stof(array10[i * 10 + 8]));
        cap16.push_back(stof(array16[i * 10 + 8]));

    }

    vector<float> sus10;
    vector<float> sus16;
    for (int i = 0; i < array10.size() / 10; i++)
    {
        if (i * 10 + 7 >= array10.size())
        {
            break;
        }

        sus10.push_back(stof(array10[i * 10 + 5]));
        sus16.push_back(stof(array16[i * 10 + 5]));

    }

    for (auto x : boost::adaptors::reverse(mag16))
    {
        cout << x << ", ";
    }

    return 0;
}
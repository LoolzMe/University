#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <random>


class Ran
{
private:
    float lower_bound = 0;
    float upper_bound = 1;
    long seed;
    std::uniform_real_distribution<float>* unif = nullptr;
    std::default_random_engine* re = nullptr;

public:
    Ran(float lower, float upper, long seed):
    lower_bound(lower),
    upper_bound(upper),
    seed(seed)
    {
        unif = new std::uniform_real_distribution<float>(lower_bound,upper_bound);
        re = new std::default_random_engine();

    }

    ~Ran()
    {
        unif = nullptr;
        re = nullptr;
        delete unif;
        delete re;
    }

    float ran1()
    {
        return (*unif)(*re);
    }

};


int main()
{
    Ran ra(0.0f, 1.0f, 111);
    std::cout << ra.ran1() << '\n';
    std::cout << ra.ran1() << '\n';
    std::cout << ra.ran1() << '\n';

    float T1 = 2.30, T2 = 2.20;

    std::cout << log(0.669938 / 0.794219)/log(0.1) << '\n';
    std::cout << log(4.85644 / 2.3928)/log(0.1) << '\n';
    std::cout << log(1.54246 / 1.28026)/log(0.1) << '\n';
    return 0;
}
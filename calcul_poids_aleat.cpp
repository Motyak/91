#include <iostream>
#include <random>
#include <chrono>

#define MODULO 91

int sumOfDigits(int n)
{
    int sum = 0;
    while(n!=0)
    {
        /* Find last digit of num and add to sum */
        sum += n % 10;

        /* Remove last digit from num */
        n = n / 10;
    }
    return sum;
}

bool remplitCondition(int n, int modulo)
{
    n = n % modulo;
    if(sumOfDigits(n) >= 10)
        return false;
    if(n % 10 == 0 || n == 0)
        return false;
    return true;
}

int generateRandom(int min, int max)
{
    std::random_device random;
    return random() % (max+1) + min;
}

int calculPoids(int n)
{
    int poids = 0;
    while(!remplitCondition(n, MODULO))
    {
        n += 24;
        poids++;
    }
    return poids;
}

int generateNbConforme()
{
    int aleat = generateRandom(100000, 999999);
    while(!remplitCondition(aleat, MODULO))
    {
        aleat += 24;
    }
    return aleat;
}

int main()
{
    int aleat = generateRandom(100000, 999999);
    std::cout<<"nb = "<<aleat<<" ; poids = "<<calculPoids(aleat)<<std::endl;

    return 0;
}


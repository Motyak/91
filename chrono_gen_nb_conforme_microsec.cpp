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
    int nb;
    auto start = std::chrono::steady_clock::now();
    nb = generateNbConforme();
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<float, std::micro> elapsed = end-start;
    std::cout<<"generated "<<nb<<" in "<<elapsed.count()<<std::endl;

    return 0;
}


#include <iostream>
#include <random>

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

int main()
{
    double remplit = 0.0;
    double i;
    for(i = 1.0 ; i <= 1000000.0 ; ++i)
    {
        //generer un nombre aleatoire
        int aleat;
        aleat = generateRandom(0, 90);
        
        //si il remplit la condition en ajoutant 24, incrementer remplit.
        if(remplitCondition(aleat, MODULO))
            remplit = remplit + 1.0;
    }
    
    std::cout<<remplit<<"/"<<i<<" soit "<<remplit/i*100<<"%"<<std::endl;

    return 0;
}


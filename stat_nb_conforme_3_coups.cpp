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
        bool nbConformeTrouve = false;
        int c = 1;
        
        int aleat = generateRandom(0, 90);
        do
        {
            if(remplitCondition(aleat, MODULO))
            {
                nbConformeTrouve = true;
            }
            else
            {
                //aleat = generateRandom(0, 90);
                aleat += 24;
                c++;
            }
        } while(!nbConformeTrouve);
        
        if(c <= 3)
            remplit++;
    }
    
    std::cout<<remplit<<"/"<<i<<" soit "<<remplit/i*100<<"%"<<std::endl;

    return 0;
}


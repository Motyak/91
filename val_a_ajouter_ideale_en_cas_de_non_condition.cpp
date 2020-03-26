#include <iostream>
#include <vector>

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

//a - b
int soustraction(int a, int b, int modulo)
{
    a = a % modulo;
    b = b % modulo;
    int res = a-b;
    if(res < 0)
        return modulo - (b - a);
    return res;
}

//a + b
int addition(int a, int b, int modulo)
{
    a = a % modulo;
    b = b % modulo;
    int res = a + b;
    if(res > 90)
        return res - modulo;
    return res;
}

int main()
{

    
    int occurencesSous[91] = {0};
    int occurencesAdd[91] = {0};
    
    for (int i = 0 ; i <= 90 ; ++i)
    {
        if(!remplitCondition(i, MODULO))
        {
            //ajouter toutes les possibilités
            for(int j = 0 ; j <= 90 ; ++j)
            {
                if(remplitCondition(soustraction(i, j, MODULO), MODULO))
                    occurencesSous[j]++;
            }
        }
    }
    
    for (int i = 0 ; i <= 90 ; ++i)
    {
        if(!remplitCondition(i, MODULO))
        {
            //ajouter toutes les possibilités
            for(int j = 0 ; j <= 90 ; ++j)
            {
                if(remplitCondition(addition(i, j, MODULO), MODULO))
                    occurencesAdd[j]++;
            }
        }
    }
    
    for(int i = 0 ; i<91 ; ++i)
    {
        std::cout<<i<<" : "<<occurencesSous[i]<<std::endl;
    }
    
    for(int i = 0 ; i<91 ; ++i)
    {
        std::cout<<i<<" : "<<occurencesAdd[i]<<std::endl;
    }
    

    return 0;
}


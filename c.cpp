#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <string>
#include <iostream>

int sumOfDigits(int);

struct Sequence
{
    std::vector<int> v;
    explicit Sequence(int from, int to)
    {
        for(int i = from; i < to; ++i)
            v.push_back(i);
    }
};

Sequence operator<<(Sequence, std::function<void(int&)>);
void print(const Sequence&);

int main()
{
    auto seq = Sequence(1, 46) << [](int& n){n=(n%10!=0&&sumOfDigits(n)<10)?n:91-n;}
                               << [](int& n){n=999999*n/91;};
    print(seq);

    // seq = [floor(n/91*10**6) for n in [91-x if x%10==0 or floor(x/10)+x/10%1*10>=10 else x for x in range(1, 46)]];
}

int sumOfDigits(int nb)
{
    std::string str = std::to_string(nb);
    int sum = 0;
    for(const auto& c : str)
        sum += ((int)c - 48);
    return sum;
}

Sequence operator<<(Sequence s, std::function<void(int&)> fn)
{
    for(auto& e : s.v)
        fn(e);
    return s;
}

void print(const Sequence& s)
{
    for(const auto& e : s.v)
        std::cout << e << ",";
    std::cout << std::endl;
}

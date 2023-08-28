// 2개 이하로 다른 비트.  2023-08-28


#include <vector>

using namespace std;

long long calc(long long n)
{
    long long i = 1;
    while (i & n) i <<= 1;
    
    n += i;
    if (i != 1)
        n -= (i >> 1);
    
    return n;
}

vector<long long> solution(vector<long long> numbers)
{
    int size = numbers.size();
    vector<long long> ans(size);
    
    for (int i = 0; i < size; ++i)
        ans[i] = calc(numbers[i]);
    
    return ans;
}

// N개의 최소공배수.  2023-12-08


#include <vector>

using namespace std;

int divisor[101];

void divide(int n)
{
    int temp[101] = { 0, };
    int N = n;
    
    for (int i = 2; 0 < n / i; ++i)
    {
        if (n % i == 0)
        {
            ++temp[i];
            n /= i;
            --i;
        }
    }
    
    for (int i = 2; i <= N; ++i)
    {
        if (divisor[i] < temp[i])
        {
            divisor[i] = temp[i];
        }
    }
}

int solution(vector<int> arr)
{
    for (int n: arr)
    {
        divide(n);
    }
    
    int ans = 1;
    for (int i = 0; i < 101; ++i)
    {
        if (divisor[i] != 0)
        {
            for (int j = 0; j < divisor[i]; ++j)
            {
                ans *= i;
            }
        }
    }
    
    return ans;
}

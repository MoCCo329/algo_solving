// 숫자 블록.  2023-12-20


#include <vector>

using namespace std;

int find(int n)
{
    if (n == 1) return 0;
    
    int i = 2;
    int last = 0;
    
    while (i * i <= n)
    {
        if (n % i == 0)
        {
            if ((n / i) < 10000001) return n / i;
            last = i;
        }
        ++i;
    }
    
    return last == 0 ? 1 : last;
}

vector<int> solution(long long begin, long long end)
{
    vector<int> ans(end - begin + 1);
    
    for (int i = begin; i <= end; ++i)
    {
        ans[i - begin] = find(i);
    }
    
    return ans;
}

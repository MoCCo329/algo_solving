// 입국심사.  2023-09-26


#include <vector>

using namespace std;

long long test(long long t, vector<int> &times, int size)
{
    long long temp_ans = 0;
    for (int i = 0; i < size; ++i)
    {
        temp_ans += t / times[i];
    }
    return temp_ans;
}

long long solution(int n, vector<int> times)
{
    long long l = 0, r = 100000000000000, m;
    
    while (l <= r)
    {
        m = (l + r) / 2;
        if (test(m, times, times.size()) < n)
        {
            l = m + 1;
        }
        else
        {
            r = m - 1;
        }
    }
    
    return l;
}

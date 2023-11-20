// 선입 선출 스케줄링.  2023-11-20


#include <vector>

using namespace std;

int N;
int memo_cnt;
int memo[10000];
vector<int> cores;

long long work(int t)
{
    memo_cnt = 0;
    long long temp = 0;
    for (int i = 0; i < cores.size(); ++i)
    {
        int core = cores[i];
        temp += (t + core - 1) / core;
        if (t % core == 0)
        {
            memo[memo_cnt] = i;
            ++memo_cnt;
            ++temp;
        }
    }
    
    return temp;
}

int solution(int n, vector<int> _cores)
{
    N = n;
    cores = _cores;
    
    int l = 0, r = 500000000;
    while (l <= r)
    {
        int m = (l + r) / 2;
        long long temp = work(m);
        if (temp - memo_cnt < n && n <= temp)
        {
            return memo[memo_cnt - 1 - (temp - n)] + 1;
        }
        
        if (temp < n)
        {
            l = m + 1;
        }
        else
        {
            r = m - 1;
        }
    }
    
    return -1;
}

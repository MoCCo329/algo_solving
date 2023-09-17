// 금과 은 운반하기.  2023-09-18


#include <stdio.h>
#include <vector>

using namespace std;

bool test(int a, int b, long long time, int N, vector<int> &g, vector<int> &s, vector<int> &w, vector<int> &t)
{
    int tot = 0;
    int tot_g = 0;
    int tot_s = 0;
    long long cnt;
    int temp;
    
    for (int i = 0; i < N; ++i)
    {
        cnt = time / (t[i] * 2);
        if (t[i] <= time % (t[i] * 2)) cnt++;
        temp = cnt * w[i] < g[i] + s[i] ? cnt * w[i] : g[i] + s[i];
        tot += temp;
        tot_g += temp < g[i] ? temp : g[i];
        tot_s += temp < s[i] ? temp : s[i];
    }
    
    if (tot < a + b || tot_g < a || tot_s < b) return false;
    return true;
}

long long solution(int a, int b, vector<int> g, vector<int> s, vector<int> w, vector<int> t)
{
    int N = s.size();
    long long l = 1;
    long long r = 900000000000000;
    long long ans = 0;
    long long m;
    
    while (l <= r)
    {
        m = (l + r) / 2;
        if (test(a, b, m, N, g, s, w, t))
        {
            r = m - 1;
        }
        else
        {
            l = m + 1;
        }
    }
    
    return l;
}

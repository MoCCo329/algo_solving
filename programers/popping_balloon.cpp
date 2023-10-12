// 풍성 터트리기.  2023-10-12


#include <vector>

using namespace std;

int dp[1000000];
int dp_rev[1000000];

int min(int a, int b)
{
    return a < b ? a : b;
}

int solution(vector<int> a)
{
    int ans = 2;
    int len = a.size();
    
    if (len < 3) return len;
    
    dp[0] = a[0];
    for (int i = 1; i < len; ++i)
    {
        dp[i] = min(a[i], dp[i - 1]);
    }
    
    dp_rev[len - 1] = a[len - 1];
    for (int i = len - 2; 0 <= i; --i)
    {
        dp_rev[i] = min(a[i], dp_rev[i + 1]);
    }
    
    for (int i = 1; i < len - 1; ++i)
    {
        if (dp[i - 1] < a[i] && dp_rev[i + 1] < a[i]) continue;
        ans++;
    }
    
    return ans;
}

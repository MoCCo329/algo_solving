// 스티커 모으기(2).  2023-10-07


#include <vector>

using namespace std;

int dp[100001][2];
int len;

int max(int a, int b)
{
    return a < b ? b : a;
}

int solution(vector<int> sticker)
{
    len = sticker.size();
    if (len == 1) return sticker[0];
    
    int ans = 0;
    
    dp[1][1] = sticker[1];
    for (int i = 2; i < len; ++i)
    {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
        dp[i][1] = dp[i - 1][0] + sticker[i];
    }
    ans = max(dp[len - 1][0], dp[len - 1][1]);
    
    dp[0][1] = sticker[0];
    dp[1][0] = sticker[0];
    for (int i = 2; i < len; ++i)
    {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
        dp[i][1] = dp[i - 1][0] + sticker[i];
    }
    ans = max(ans, dp[len - 1][0]);
    
    return ans;
}

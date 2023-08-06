// 땅따먹기.  2023-08-06


#include <vector>

using namespace std;
int dp[100000][4];

int max(int a, int b, int c, int d)
{
    if (b <= a && d <= c)
    {
        if (a <= c) return c;
        return a;
    }
    else if (a < b && d <= c)
    {
        if (b <= c) return c;
        return b;
    }
    else if (b <= a && c < d)
    {
        if (a <= d) return d;
        return a;
    }
    else
    {
        if (b <= d) return d;
        return b;
    }
}

int solution(vector<vector<int> > land)
{
    for (int i = 0; i < 4; ++i)
    {
        dp[0][i] = land[0][i];
    }
    for (int i = 1, size = land.size(); i < size; ++i)
    {
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3], 0) + land[i][0];
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3], 0) + land[i][1];
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3], 0) + land[i][2];
        dp[i][3] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], 0) + land[i][3];
    }

    return max(dp[land.size() - 1][0], dp[land.size() - 1][1], dp[land.size() - 1][2], dp[land.size() - 1][3]);
}
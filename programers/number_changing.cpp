// 숫자 변환하기.  2023-08-11


using namespace std;

int dp[1000001];
int MAX = 1000001;

int solution(int x, int y, int n) {
    dp[x] = 1;
    for (int i = x; i < y; ++i)
    {
        if (dp[i] == 0) continue;
        
        if (i + n < MAX && (dp[i + n] == 0 || dp[i] + 1 < dp[i + n]))
            dp[i + n] = dp[i] + 1;
        if ((i << 1) < MAX && (dp[i * 2] == 0 ||dp[i] + 1 < dp[i * 2]))
            dp[i * 2] = dp[i] + 1;
        if (i * 3 < MAX && (dp[i * 3] == 0 || dp[i] + 1 < dp[i * 3]))
            dp[i * 3] = dp[i] + 1;
    }
    
    return dp[y] - 1;
}

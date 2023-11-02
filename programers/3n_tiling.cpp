// 3 x n 타일링.  2023-11-02


using namespace std;

long long dp[5001];
long long MOD = 1000000007;

int solution(int n)
{
    if (n % 2 == 1) return 0;
    
    dp[2] = 3;
    dp[4] = 11;
    
    for (int i = 6; i <= n; i += 2)
    {
        dp[i] = (MOD + dp[i - 2] * 4 - dp[i - 4]) % MOD;
    }
    
    return (int) dp[n];
}

// 최적의 행렬 곱셈.  2023-11-19


#include <vector>

using namespace std;

int dp[201][201];
vector<vector<int> > matrix;

int cal(int l, int r)
{
    if (r - l < 2) return 0;
    if (dp[l][r] != 0) return dp[l][r];
    
    int temp_dp = 987654321;
    for (int m = l + 1; m < r; ++m)
    {
        int temp = cal(l, m) + cal(m, r) + (matrix[l][0] * matrix[m][0] * matrix[r - 1][1]);
        temp_dp = min(temp_dp, temp);
    }
    dp[l][r] = temp_dp;
    return dp[l][r];
}

int solution(vector<vector<int> > matrix_sizes)
{
    matrix = matrix_sizes;
    cal(0, matrix.size());
    
    return dp[0][matrix.size()];
}

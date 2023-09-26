// 순위.  2023-09-26


#include <vector>

using namespace std;

bool win[100][100];
bool lose[100][100];

int solution(int n, vector<vector<int>> results) {
    for (vector<int> res: results)
    {
        win[res[0] - 1][res[1] - 1] = true;
        lose[res[1] - 1][res[0] - 1] = true;
    }
    
    for (int k = 0; k < n; ++k)
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (win[i][k] && win[k][j])
                {
                    win[i][j] = true;
                    lose[j][i] = true;
                }
                
                if (lose[i][k] && lose[k][j])
                {
                    win[j][i] = true;
                    lose[i][j] = true;
                }
            }
        }
    }
    
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int temp = 0;
        for (int j = 0; j < n; ++j)
        {
            if (win[i][j] || lose[i][j]) temp++;
        }
        if (temp == n - 1) ans++;
    }
    
    return ans;
}

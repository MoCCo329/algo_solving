// 리틀 프렌즈 사천성.  2023-11-04


#include <string>
#include <vector>

using namespace std;

int N;
int M;
int cnt;
int flag_cnt;
int memo[26][4];

bool test(int k, vector<string> &board)
{
    int max_i = max(memo[k][0], memo[k][2]);
    int min_i = min(memo[k][0], memo[k][2]);
    int max_j = max(memo[k][1], memo[k][3]);
    int min_j = min(memo[k][1], memo[k][3]);
    
    bool path1 = true;
    bool path2 = true;
    if (memo[k][0] == memo[k][2])
    {
        for (int j = min_j + 1; j < max_j; ++j)
        {
            if (board[memo[k][0]][j] != '.') return false;
        }
    }
    else if (memo[k][1] == memo[k][3])
    {
        for (int i = min_i + 1; i < max_i; ++i)
        {
            if (board[i][memo[k][1]] != '.') return false;
        }
    }
    else if ((memo[k][0] < memo[k][2] && memo[k][1] < memo[k][3]) || (memo[k][2] < memo[k][0] && memo[k][3] < memo[k][1]))
    {
        for (int i = min_i; i <= max_i; ++i)
        {
            if (i != memo[k][0] && board[i][memo[k][1]] != '.')
            {
                path1 = false;
            }
            if (i != memo[k][2] && board[i][memo[k][3]] != '.')
            {
                path2 = false;
            }
        }
        for (int j = min_j; j <= max_j; ++j)
        {
            if (j != memo[k][3] && board[memo[k][2]][j] != '.')
            {
                path1 = false;
            }
            if (j != memo[k][1] && board[memo[k][0]][j] != '.')
            {
                path2 = false;
            }
        }
    }
    else
    {
        for (int i = min_i; i <= max_i; ++i)
        {
            if (i != memo[k][2] && board[i][memo[k][3]] != '.')
            {
                path1 = false;
            }
            if (i != memo[k][0] && board[i][memo[k][1]] != '.')
            {
                path2 = false;
            }
        }
        for (int j = min_j; j <= max_j; ++j)
        {
            if (j != memo[k][1] && board[memo[k][0]][j] != '.')
            {
                path1 = false;
            }
            if (j != memo[k][3] && board[memo[k][2]][j] != '.')
            {
                path2 = false;
            }
        }
    }
    
    if (!path1 && !path2) return false;
    board[memo[k][0]][memo[k][1]] = '.';
    board[memo[k][2]][memo[k][3]] = '.';
    return true;
}

string solution(int n, int m, vector<string> board)
{
    N = n;
    M = m;
    cnt = 0;
    bool not_vis[26] = { false, };
    
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0 ; j < M; ++j)
        {
            if (board[i][j] != '.' && board[i][j] != '*')
            {
                if (!not_vis[board[i][j] - 'A'])
                {
                    ++cnt;
                    not_vis[board[i][j] - 'A'] = true;
                    memo[board[i][j] - 'A'][0] = i;
                    memo[board[i][j] - 'A'][1] = j;
                }
                else
                {
                    memo[board[i][j] - 'A'][2] = i;
                    memo[board[i][j] - 'A'][3] = j;
                }
            }
        }
    }
    
    string ans = "";
    while (0 < cnt)
    {
        flag_cnt = cnt;
            
        for (int i = 0; i < 26; ++i)
        {
            if (!not_vis[i]) continue;
            if (test(i, board))
            {
                --cnt;
                not_vis[i] = false;
                char temp = (char) i + 'A';
                ans = ans + temp;
                break;
            }
        }
        
        if (flag_cnt == cnt) return "IMPOSSIBLE";
    }
    
    return ans;
}

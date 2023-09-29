// 단어 번역.  2023-09-30


#include <string>
#include <vector>

using namespace std;

bool adj_mat[52][52];
bool vis[52];
int len;
int ans;
int target_idx = -1;

void dfs(int i, int cnt)
{
    if (i == target_idx)
    {
        ans = cnt;
        return;
    }
    if (ans != 0 && ans <= cnt) return;
    
    for (int j = 0; j < len + 2; ++j)
    {
        if (vis[j] || !adj_mat[i][j]) continue;
        vis[j] = true;
        dfs(j, cnt + 1);
        vis[j] = false;
    }
}

int solution(string begin, string target, vector<string> words)
{
    len = words.size();
    words.push_back(begin);
    
    for (int i = 0; i < words.size(); ++i)
    {
        for (int j = 0; j < words.size(); ++j)
        {
            if (i == j) continue;
            int cnt = 0;
            for (int k = 0; k < words[i].size(); ++k)
            {
                if (words[i][k] != words[j][k]) cnt++;
            }
            if (cnt == 1)
            {
                adj_mat[i][j] = true;
                adj_mat[j][i] = true;
            }
        }
    }
    
    for (int i = 0; i < len; ++i)
    {
        if (target == words[i]) target_idx = i;
    }
    
    vis[len] = true;
    dfs(len, 0);
    
    return ans;
}

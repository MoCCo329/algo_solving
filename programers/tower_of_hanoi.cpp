// 하노이의 탑.  2023-12-23


#include <vector>

using namespace std;

void dfs(int from, int to, int n, vector<vector<int> > &ans)
{
    int mid = 6 - from - to;
    
    if (n == 1)
    {
        vector<int> temp = { from, to };
        ans.push_back(temp);
        return;
    }
    
    dfs(from, mid, n - 1, ans);
    vector<int> temp = { from, to };
    ans.push_back(temp);
    dfs(mid, to, n - 1, ans);
}

vector<vector<int> > solution(int n)
{
    vector<vector<int> > ans;
    dfs(1, 3, n, ans);
    
    return ans;
}

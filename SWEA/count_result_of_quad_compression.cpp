// 쿼드압축 후 개수 세기.  2023-10-15


#include <vector>

using namespace std;

vector<int> dfs(vector<vector<int> > &arr, int i, int j, int N)
{
    vector<int> ans(2);
    
    if (N == 1)
    {
        if (arr[i][j] == 1)
        {
            ans[1] = 1;
        }
        else
        {
            ans[0] = 1;
        }
        return ans;
    }
    
    vector<int> temp(2);
    
    temp = dfs(arr, i + 0, j + 0, N / 2);
    ans[0] += temp[0];
    ans[1] += temp[1];
    
    temp = dfs(arr, i + 0, j + N / 2, N / 2);
    ans[0] += temp[0];
    ans[1] += temp[1];
    
    temp = dfs(arr, i + N / 2, j + 0, N / 2);
    ans[0] += temp[0];
    ans[1] += temp[1];
    
    temp = dfs(arr, i + N / 2, j + N / 2, N / 2);
    ans[0] += temp[0];
    ans[1] += temp[1];
    
    if (ans[0] == 0)
    {
        ans[1] = 1;
    }
    if (ans[1] == 0)
    {
        ans[0] = 1;
    }
    return ans;
}

vector<int> solution(vector<vector<int>> arr)
{
    return dfs(arr, 0, 0, arr.size());
}

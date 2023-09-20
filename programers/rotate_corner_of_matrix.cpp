// 행렬 테두리 회전하기.  2023-09-20


#include <vector>

using namespace std;

int temp;

int maps[100][100];

int rotate(int si, int sj, int ei, int ej)
{
    int ans;
    
    int temp = ans = maps[si][ej];
    for (int j = ej; sj < j; --j)
    {
        maps[si][j] = maps[si][j - 1];
        ans = min(ans, maps[si][j]);
    }
    
    int temp2 = maps[ei][ej];
    for (int i = ei; si < i; --i)
    {
        maps[i][ej] = maps[i - 1][ej];
        ans = min(ans, maps[i][ej]);
    }
    maps[si + 1][ej] = temp;
    ans = min(ans, temp);
    
    int temp3 = maps[ei][sj];
    for (int j = sj; j < ej; ++j)
    {
        maps[ei][j] = maps[ei][j + 1];
        ans = min(ans, maps[ei][j]);
    }
    maps[ei][ej - 1] = temp2;
    ans = min(ans, temp2);
    
    for (int i = si; i < ei; ++i)
    {
        maps[i][sj] = maps[i + 1][sj];
        ans = min(ans, maps[i][sj]);
    }
    maps[ei - 1][sj] = temp3;
    ans = min(ans, temp3);
    
    return ans;
}

int min(int i, int j)
{
    return i < j ? i : j;
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries)
{
    int cnt = 1;
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < columns; ++j)
        {
            maps[i][j] = cnt++;
        }
    }
    
    vector<int> ans;
    for (vector<int> query: queries)
    {
        ans.push_back(rotate(query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1));
    }
    
    return ans;
}

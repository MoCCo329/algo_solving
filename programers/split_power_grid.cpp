// 전력망을 둘로 나누기.  2023-08-21


#include <string>
#include <vector>

using namespace std;

int uf[101];
int count[101];

int find(int x)
{
    if (uf[x] == x) return x;
    uf[x] = find(uf[x]);
    return uf[x];
}

void _union(int x, int y)
{
    int X = find(x), Y = find(y);
    if (X != Y) uf[X] = Y;
}


int solution(int n, vector<vector<int>> wires) {
    int ans = 101;
    int size = wires.size();
    
    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < 101; ++j) uf[j] = j, count[j] = 0;
        
        for (int j = 0; j < size; ++j)
        {
            if (i == j) continue;
            
            _union(wires[j][0], wires[j][1]);
        }
        
        int cnt = -1;
        int vis[2] = { 0, 0 };
        for (int j = 1; j <= n; ++j)
        {
            int p = find(j);
            if (count[p] == 0)
            {
                cnt++;
                vis[cnt] = p;
                if (1 < cnt) break;
            }
            count[p]++;
        }
        
        if (cnt != 1) continue;
        int temp_ans = count[vis[0]] > count[vis[1]] ? count[vis[0]] - count[vis[1]] : count[vis[1]] - count[vis[0]];
        ans = ans > temp_ans ? temp_ans : ans;
    }
    
    return ans;
}
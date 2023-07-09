// 무인도 여행  2023-07-09


#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> maps) {
    vector<int> ans;
    int N = maps.size();
    int M = maps[0].size();
    int d_list[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    bool vis[100][100] = {false,};
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (vis[i][j]) continue;
            vis[i][j] = true;
            if (maps[i][j] == 'X') continue;
            
            queue<pair<int, int>> q;
            q.push(make_pair(i, j));
            int cnt = maps[i][j] - '0';
            while (!q.empty()) {
                pair<int, int> temp = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    int di = d_list[d][0], dj = d_list[d][1];
                    int ni = temp.first + di, nj = temp.second + dj;
                    if (ni < 0 || N <= ni || nj < 0 || M <= nj) continue;
                    if (maps[ni][nj] == 'X' || vis[ni][nj]) continue;
                    vis[ni][nj] = true;
                    cnt += maps[ni][nj] - '0';
                    q.push(make_pair(ni, nj));
                }
            }
            
            ans.push_back(cnt);
        }
    }
    
    if (ans.size() == 0) ans.push_back(-1);
    else sort(ans.begin(), ans.end());
    return ans;
}
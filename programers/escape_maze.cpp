// 미로 탈출  2023-07-06


#include <string>
#include <vector>
#include <queue>

using namespace std;

int d_list[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

int solution(vector<string> maps) {
    int si, sj, li, lj, ei, ej;
    int N = maps.size();
    int M = maps[0].size();
    bool vis[N][M];
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (maps[i][j] == 'S') {
                si = i;
                sj = j;
            } else if (maps[i][j] == 'L') {
                li = i;
                lj = j;
            } else if (maps[i][j] == 'E') {
                ei = i;
                ej = j;
            }
        }
    }
    
    queue<pair<int, int>> q;
    queue<int> q_cnt;
    q.push(make_pair(si, sj));
    q_cnt.push(0);
    int i, j, cnt;
    
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            vis[i][j] = false;
    vis[si][sj] = true;
    while (!q.empty()) {
        pair<int, int> temp = q.front();
        cnt = q_cnt.front();
        q.pop();
        q_cnt.pop();
        
        i = temp.first;
        j = temp.second;
        if (i == li && j == lj) break;
        
        for (int d = 0; d < 4; ++d) {
            int ni = i + d_list[d][0], nj = j + d_list[d][1];
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] || maps[ni][nj] == 'X') continue;
            vis[ni][nj] = true;
            q.push(make_pair(ni, nj));
            q_cnt.push(cnt + 1);
        }
    }
    if (i != li || j != lj) return -1;
    
    while (!q.empty()) q.pop();
    while (!q_cnt.empty()) q_cnt.pop();
    q.push(make_pair(li, lj));
    q_cnt.push(cnt);
    
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            vis[i][j] = false;
    vis[li][lj] = true;
    while (!q.empty()) {
        pair<int, int> temp = q.front();
        cnt = q_cnt.front();
        q.pop();
        q_cnt.pop();
        
        i = temp.first;
        j = temp.second;
        if (i == ei && j == ej) break;
        
        for (int d = 0; d < 4; ++d) {
            int ni = i + d_list[d][0], nj = j + d_list[d][1];
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] || maps[ni][nj] == 'X') continue;
            vis[ni][nj] = true;
            q.push(make_pair(ni, nj));
            q_cnt.push(cnt + 1);
        }
    }
    
    if (i == ei && j == ej) return cnt;
    else return -1;
}
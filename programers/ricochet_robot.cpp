// 리코쳇 로봇  2023-07-04


#include <string>
#include <vector>
#include <queue>

using namespace std;

int vis[100][100];
int d_list[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int solution(vector<string> board) {
    int N = board.size();
    int M = board[0].size();
    queue<pair<int, int>> q;
    
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j) {
            vis[i][j] = -1;
            if (board[i][j] == 'R') q.push({i, j});
        }
    
    vis[q.front().first][q.front().second] = 0;
    while (!q.empty())
    {
        pair<int, int> ij = q.front();
        q.pop();
        
        for (int d = 0; d < 4; ++d) {
            int di = d_list[d][0], dj = d_list[d][1];
            int i = ij.first, j = ij.second;
            
            while (0 <= i + di && i + di < N && 0 <= j + dj && j + dj < M && board[i + di][j + dj] != 'D') {
                i += di;
                j += dj;
            }
            
            if (board[i][j] == 'G') return vis[ij.first][ij.second] + 1;
            if (0 <= vis[i][j]) continue;
            vis[i][j] = vis[ij.first][ij.second] + 1;
            q.push({i, j});
        }
    }
    
    return -1;
}
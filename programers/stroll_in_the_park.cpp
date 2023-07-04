// 공원 산책  2023-07-04


#include <string>
#include <vector>

using namespace std;

int N, M;
int maps[50][50];
int ii, jj;

bool test(int i, int j) {
    if ((i < 0) || (N <= i) || (j < 0) || (M <= j)) return false;
    if (maps[i][j] == 1) return false;
    return true;
}

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> ans;
    N = park.size();
    M = park[0].size();
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (park[i][j] == 'O') maps[i][j] = 0;
            else if (park[i][j] == 'X') maps[i][j] = 1;
            else {
                maps[i][j] = 0;
                ii = i;
                jj = j;
            }
        }
    }
    
    for (string s: routes) {
        int d = (int)s[2] - '0';
        int di = 0, dj = 0;
        if (s[0] == 'E') di = 0, dj = 1;
        else if (s[0] == 'W') di = 0, dj = -1;
        else if (s[0] == 'N') di = -1, dj = 0;
        else di = 1, dj = 0;
        
        int oi = ii, oj = jj;
        while (d--) {
            ii += di;
            jj += dj;
            if (!test(ii, jj)) {
                ii = oi;
                jj = oj;
                break;
            }
        }
    }
    
    ans.push_back(ii);
    ans.push_back(jj);
    
    return ans;
}
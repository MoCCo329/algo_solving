// 여행 경로.  2023-11-16


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool vis[10000];
int N;
vector<string> ans;
bool isEnd;

void dfs(string s, int cnt, vector<string> &path, vector<vector<string> > &tickets)
{
    if (cnt == N)
    {
        ans = path;
        isEnd = true;
        return;
    }
    
    if (isEnd) return;
    
    for (int i = 0; i < N; ++i)
    {
        if (vis[i]) continue;
        if (tickets[i][0] != s) continue;
        vis[i] = true;
        path.push_back(tickets[i][1]);
        dfs(tickets[i][1], cnt + 1, path, tickets);
        path.pop_back();
        vis[i] = false;
    }
}

vector<string> solution(vector<vector<string> > tickets)
{
    N = tickets.size();
    sort(tickets.begin(), tickets.end());
    
    vector<string> path;
    path.push_back("ICN");
    dfs("ICN", 0, path, tickets);
    
    return ans;
}

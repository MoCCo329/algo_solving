// 달리기 경주  2023-07-03


#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> ans;
    map<int, string> rank_to_p;
    map<string, int> p_to_rank;
    
    for (int i = 0; i < players.size(); ++i)
    {
        p_to_rank[players[i]] = i;
        rank_to_p[i] = players[i];
    }
    
    for (int i = 0; i < callings.size(); ++i)
    {
        string p1 = callings[i];
        int r = p_to_rank[p1];
        string p2 = rank_to_p[r - 1];
        p_to_rank[p1] -= 1;
        p_to_rank[p2] += 1;
        rank_to_p[r - 1] = p1;
        rank_to_p[r] = p2;
    }
    
    for (int i = 0; i < players.size(); ++i) ans.push_back(rank_to_p[i]);
    
    return ans;
}
// 혼자 놀기의 달인.  2023-07-23


#include <vector>
#include <algorithm>

using namespace std;

vector<int> counts(101);
bool vis[101];

int solution(vector<int> cards) {
    int ans = 0;
    int cnt = 0;
    int N = cards.size();
    
    for (int i = 0; i < N; ++i)
    {
        if (!vis[i + 1])
        {
            int temp = i + 1;
            while (!vis[temp])
            {
                vis[temp] = true;
                temp = cards[temp - 1];
                counts[cnt]++;
            }
            
            cnt++;
        }
    }
    
    sort(counts.begin(), counts.end());
    
    return counts[100] * counts[99];
}
// 디펜스 게임.  2023-07-19


#include <vector>
#include <queue>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    int ans = 0;
    int size = enemy.size();
    priority_queue<int> pq;
    int tot = 0;
    
    if (size <= k) return size;
    
    for (int e: enemy)
    {
        pq.push(-e);
        if (k < pq.size())
        {
            tot -= pq.top();
            pq.pop();
        }
        if (n < tot) break;
        ans++;
    }
    
    return ans;
}
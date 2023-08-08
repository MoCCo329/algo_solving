// 더 맵게.  2023-08-08


#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int ans = 0;
    priority_queue<int> pq;
    
    for (int s: scoville) pq.push(-s);
    
    while (1 < pq.size() && -K < pq.top())
    {
        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();
        
        pq.push(a + b * 2);
        ans++;
    }
    
    if (-K < pq.top()) return -1;
    return ans;
}

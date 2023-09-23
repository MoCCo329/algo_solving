// 야근 지수.  2023-09-24


#include <vector>
#include <queue>

using namespace std;

priority_queue<int> pq;

long long solution(int N, vector<int> works)
{
    for (int w: works)
    {
        pq.push(w);
    }
    
    while (0 < N-- && !pq.empty())
    {
        int w = pq.top();
        pq.pop();
        if (w != 1) pq.push(w - 1);
    }
    
    long long ans = 0;
    while (!pq.empty())
    {
        int temp = pq.top();
        pq.pop();
        ans += temp * temp;
    }
    
    return ans;
}

// 프로세스.  2023-12-05


#include <vector>
#include <queue>

using namespace std;

int N;
int pri_count[101];

bool test(int k)
{
    for (int i = k + 1; i < 101; ++i)
    {
        if (pri_count[i] != 0) return false;
    }
    return true;
}

int solution(vector<int> priorities, int location)
{
    N = priorities.size();
    queue<int> q;
    for (int i = 0; i < N; ++i)
    {
        ++pri_count[priorities[i]];
        q.push(i);
    }
    
    int ans = 0;
    while (!q.empty())
    {
        int temp = q.front();
        q.pop();
        if (test(priorities[temp]))
        {
            --pri_count[priorities[temp]];
            ++ans;
            if (temp == location) return ans;
        }
        else
        {
            q.push(temp);
        }
    }
    
    return ans;
}

// 스타 수열.  2023-10-01


#include <vector>

int ans;
int counts[500001];
int vis[500001];

int solution(std::vector<int> a)
{
    if (a.size() < 2) return 0;
    
    for (int i = 0; i <= a.size(); ++i) vis[i] = -1;
    
    for (int i = 0; i < a.size() - 1; ++i)
    {
        if (a[i] != a[i + 1] && vis[i] == -1)
        {
            counts[a[i]]++;
            vis[i] = i + 1;
        }
        if (a[i] != a[i + 1] && (i == 0 || a[i - 1] != a[i + 1] || vis[i - 1] != i))
        {
            counts[a[i + 1]]++;
            vis[i + 1] = i;
        }
    }
    
    for (int i = 0; i <= a.size(); ++i)
    {
        if (ans < counts[i]) ans = counts[i];
    }
    
    return ans * 2;
}

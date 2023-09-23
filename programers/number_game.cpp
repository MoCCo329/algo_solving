// 숫자 게임.  2023-09-24


#include <algorithm>
#include <vector>

using namespace std;

vector<int> *B;
int len;
bool vis[100000];

int u_b(int n, int l)
{
    int r = len;
    while (l < r)
    {
        int m = (l + r) / 2;
        if ((*B)[m] <= n)
        {
            l = m + 1;
        }
        else
        {
            r = m;
        }
    }

    while (l != len && vis[l]) ++l;
    return l;
}

int solution(vector<int> A, vector<int> _B)
{
    B = &_B;
    len = A.size();
    sort(_B.begin(), _B.end());
    
    int ans = 0;
    for (int i = 0; i < len; ++i)
    {
        int temp = u_b(A[i], 0);
        
        if (temp != len)
        {
            vis[temp] = true;
            ans++;
        }
    }
    
    return ans;
}

// 줄 서는 방법.  2023-12-18


#include <vector>

using namespace std;

int N;
long long facto_memo[20];
bool vis[21];

int find_and_use(int n_th)
{
    int temp_th = 0;
    if (n_th == -1)
    {
        while (0 < N + n_th + 1)
        {
            if (vis[N + n_th + 1])
            {
                --n_th;
                continue;
            }
            vis[N + n_th + 1] = true;
            return N + n_th + 1;
        }
    }

    for (int i = 1; i <= N; ++i)
    {
        if (vis[i]) continue;
        if (temp_th == n_th)
        {
            vis[i] = true;
            return i;
        }
        ++temp_th;
    }
    
    return 1;
}

vector<int> solution(int n, long long k)
{
    N = n;
    facto_memo[0] = 1;
    for (long long i = 1; i < 20; ++i)
    {
        facto_memo[i] = facto_memo[i - 1] * i;
        vis[i] = false;
    }

    int i = n;
    vector<int> ans(n);
    while (i != 0)
    {
        int idx = (int) (k / facto_memo[i - 1]);
        k = k % facto_memo[i - 1];
        if (k == 0)
        {
            ans[n - i] = find_and_use(idx - 1);
        }
        else
        {
            ans[n - i] = find_and_use(idx);
        }
        --i;
    }
    
    return ans;
}

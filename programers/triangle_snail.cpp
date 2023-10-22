// 삼각 달팽이.  2023-10-22


#include <vector>

using namespace std;

vector<int> solution(int n)
{
    int len = n * (n + 1) / 2;
    int l = n - 1;
    int type = 0;
    int type_cnt = 0;
    int i = 0;
    vector<int> ans(len);
    n = 1;
    
    for (int k = 1; k <= len; ++k)
    {
        ans[i] = k;
        type_cnt += 1;
        if (type == 0)
        {
            i += n;
            n += 1;
            if (type_cnt == l)
            {
                type = 1;
                type_cnt = 0;
            }
        }
        else if (type == 1)
        {
            i += 1;
            if (type_cnt == l)
            {
                type = 2;
                type_cnt = 0;
            }
        }
        else
        {
            if (type_cnt == l)
            {
                type = 0;
                type_cnt = 0;
                i += n;
                n += 1;
                l -= 3;
            }
            else
            {
                i -= n;
                n -= 1;
            }
        }
    }
    
    return ans;
}

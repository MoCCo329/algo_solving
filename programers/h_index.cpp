// H-index.  2023-11-26


#include <vector>

using namespace std;

int pre_sum[10001];

int solution(vector<int> citations)
{
    for (int c: citations)
    {
        ++pre_sum[c];
    }
    
    if (10000 <= pre_sum[10000]) return 10000;
    
    for (int i = 9999; i != -1; --i)
    {
        pre_sum[i] += pre_sum[i + 1];
        if (i <= pre_sum[i])
        {
            return i;
        }
    }
    
    return -1;
}

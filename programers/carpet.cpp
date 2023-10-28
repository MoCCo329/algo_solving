// 카펫.  2023-10-28


#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow)
{
    vector<int> ans(2);
    
    int m = 1;
    while (m <= yellow)
    {
        if (yellow % m == 0 && (brown + yellow) / ((yellow / m) + 2) == m + 2)
        {
            ans[0] = yellow / m + 2;
            ans[1] = m + 2;
            return ans;
        }
        ++m;
    }
    
    return ans;
}

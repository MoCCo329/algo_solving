// 캠핑.  2023-10-30


#include <vector>
#include <algorithm>

using namespace std;

bool compare(vector<int> a, vector<int> b)
{
    if (a[0] == b[0]) return a[1] < b[1];
    return a[0] < b[0];
}

int solution(int n, vector<vector<int>> data)
{
    int ans = 0;
    
    sort(data.begin(), data.end(), compare);
    
    for (int i = 0; i < n - 1; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            if (data[i][0] == data[j][0] || data[i][1] == data[j][1]) continue;
            
            bool flag = true;
            for (int k = i + 1; k < j; ++k)
            {
                if (data[i][0] < data[k][0] && data[k][0] < data[j][0] &&
                    min(data[i][1], data[j][1]) < data[k][1] && data[k][1] < max(data[i][1], data[j][1]))
                {
                    flag = false;
                    break;
                }
            }
            if (flag) ++ans;
        }
    }
    
    return ans;
}

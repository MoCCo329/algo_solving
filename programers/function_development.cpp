// 기능개발.  2023-11-30


#include <vector>

using namespace std;

int t = 1;
int temp_ans;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
    vector<int> ans;
    
    for (int i = 0; i < progresses.size(); ++i)
    {
        if (100 <= progresses[i] + speeds[i] * t)
        {
            ++temp_ans;
            continue;
        }
        
        if (i != 0) ans.push_back(temp_ans);
        while (progresses[i] + speeds[i] * t  < 100) ++t;
        temp_ans = 1;
    }
    ans.push_back(temp_ans);
    
    return ans;
}

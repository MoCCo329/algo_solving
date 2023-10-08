// 110 옮기기.  2023-10-09


#include <string>
#include <vector>

using namespace std;

int cnt;
int one;

vector<string> solution(vector<string> ss)
{
    vector<string> ans;
    
    for (string s: ss)
    {
        cnt = 0;
        one = 0;
        string temp_ans;
        
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '0')
            {
                if (2 <= one)
                {
                    cnt++;
                    one -= 2;
                } else
                {
                    if (0 < one) --one, temp_ans += '1';
                    temp_ans += '0';
                }
            }
            else
            {
                one++;
            }
        }
        
        while (cnt--) temp_ans += "110";
        while (one--) temp_ans += '1';
        
        ans.push_back(temp_ans);
    }
    
    return ans;
}

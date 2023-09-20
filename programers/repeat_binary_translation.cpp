// 이진 변환 반복하기.  2023-09-21


#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s)
{
    vector<int> ans = {0, 0};
    int acc;
    int zero;
    int one;
    int temp;
    
    while (s.size() != 1)
    {
        ans[0]++;
        zero = 0;
        one = 0;
        
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '0') zero++;
            else one++;
        }
        ans[1] += zero;
        
        s = "";
        temp = 1;
        while (temp <= one)
        {
            if (temp & one) s = "1" + s;
            else s = "0" + s;
            temp <<= 1;
        }
    }
    
    return ans;
}

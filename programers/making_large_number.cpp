// 큰 수 만들기.  2023-07-31


#include <string>
#include <stack>

using namespace std;

string solution(string number, int k)
{
    string ans = "";
    
    stack<int> s;
    int l = number.size();
    for (int i = 0; i < l; ++i)
    {
        char n = number[i];
        while (0 < k && !s.empty() && s.top() < n) --k, s.pop();
        s.push(n);
        if (l - i + 1 == k) break;
    }
    
    while (0 < k) --k, s.pop();
    while (!s.empty())
    {
        ans = (char) s.top() + ans;
        s.pop();
    }
    
    return ans;
}
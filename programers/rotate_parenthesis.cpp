// 괄호 회전하기.  2023-08-09


#include <string>
#include <vector>
#include <stack>

using namespace std;

int get_reverse_hash(char c)
{
    switch (c)
    {
        case ']':
            return 91;
        case '}':
            return 123;
        case ')':
            return 40;
    }
    return 0;
}

int solution(string s)
{
    int ans = 0;
    int size = s.size();
    
    for (int i = 0; i < size; ++i)
    {
        stack<int> stack;
        bool flag = true;
        for (int j = 0; j < size; ++j)
        {
            int idx = (i + j) % size;
            if (get_reverse_hash(s[idx]) == 0)
            {
                stack.push(s[idx]);
            }
            else
            {
                if (stack.empty() || stack.top() != get_reverse_hash(s[idx]))
                {
                    flag = false;
                    break;
                }
                stack.pop();
            }
        }
        
        if (flag && stack.empty()) ans++;
    }
    
    return ans;
}
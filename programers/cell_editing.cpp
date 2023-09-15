// 표 편집.  2023-09-15


#include <stack>
#include <string>
#include <vector>

using namespace std;

int _prev[1000001];
int _next[1000001];

string solution(int n, int k, vector<string> cmd)
{
    string ans = "";
    stack<int> stac;
    int m;
    int start = 0;
    int end = n - 1;
    
    for (int i = 0; i < n; ++i)
    {
        ans += "O";
        _prev[i] = i - 1;
        _next[i] = i + 1;
    }
    _prev[0] = 0, _next[n - 1] = n - 1;
    
    for (string s: cmd)
    {
        switch (s[0])
        {
            case 'D':
                m = stoi(s.substr(2));
                while (m--)
                {
                    k = _next[k];
                }
                break;
            case 'U':
                m = stoi(s.substr(2));
                while (m--)
                {
                    k = _prev[k];
                }
                break;
            case 'C':
                stac.push(k);
                if (k != n - 1) _next[_prev[k]] = _next[k];
                if (k != 0) _prev[_next[k]] = _prev[k];
                
                if (k == end) end = k = _prev[k];
                else if (k == start) start = k = _next[k];
                else k = _next[k];
                break;
            case 'Z':
                int kk = stac.top();
                stac.pop();
                if (kk != 0) _next[_prev[kk]] = kk;
                if (kk != n - 1) _prev[_next[kk]] = kk;
                if (kk < start) start = kk;
                if (end < kk) end = kk;
        }
    }
    
    while (!stac.empty())
    {
        ans[stac.top()] = 'X';
        stac.pop();
    }
    
    return ans;
}

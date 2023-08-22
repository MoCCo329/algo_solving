// 괄호 변환.  2023-08-22


#include <string>

using namespace std;

char c_arr[1000];
int c_idx;
int p_size;
char* p;

bool test_correct(int l, int r)
{
    int cnt = 0;
    for (int k = l; k <= r; ++k)
    {
        if (p[k] == 41)
        {
            if (cnt == 0)
            {
                return false;
            }
            cnt--;
        }
        else
        {
            cnt++;
        }
    }
    if (0 < cnt) return false;
    return true;
}

void dfs(int l, int r)
{
    int count[2] = { 0, 0 };
    
    for (; r < p_size; ++r)
    {
        if (p[r] == 40) count[0]++;
        else count[1]++;
        
        if (count[0] == count[1])
        {
            if (!test_correct(l, r))
            {
                c_arr[c_idx++] = '(';
                dfs(r + 1, r + 1);
                c_arr[c_idx++] = ')';
                for (int k = l + 1; k < r; ++k)
                {
                    c_arr[c_idx++] = p[k] == 40 ? 41 : 40;
                }
                return;
            }
            else
            {
                for (int k = l; k <= r; ++k)
                {
                    c_arr[c_idx++] = p[k];
                }
                l = r + 1;
            }
        }
    }
}

string solution(string s)
{
    p_size = s.size();
    p = (char*) s.c_str();
    
    dfs(0, 0);
    c_arr[c_idx] = 0;
    
    return c_arr;
}
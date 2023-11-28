// 주식가격.  2023-11-28


#include <vector>

using namespace std;

int N;
int stack[100000];
int s_idx;

vector<int> solution(vector<int> prices)
{
    N = prices.size();
    vector<int> ans(N);
    
    for (int i = N - 1; 0 <= i; --i)
    {
        int idx = s_idx - 1;
        int temp_ans = 0;
        int now = prices[i];
        
        while (0 <= idx)
        {
            ++temp_ans;
            if (stack[idx] < now) break;
            --idx;
        }
        stack[s_idx] = now;
        s_idx++;
        ans[i] = temp_ans;
    }
    
    return ans;
}

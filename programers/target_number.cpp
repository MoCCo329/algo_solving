// 타겟 넘버.  2023-10-03


#include <vector>

using namespace std;

int ans;
int target;
int len;

void dfs(vector<int> &numbers, int i, int n)
{
    if (i == len)
    {
        if (target == n) ans++;
        return;
    }
    
    dfs(numbers, i + 1, n + numbers[i]);
    dfs(numbers, i + 1, n - numbers[i]);
}

int solution(vector<int> numbers, int _target)
{
    target = _target;
    len = numbers.size();
    
    dfs(numbers, 0, 0);
    return ans;
}

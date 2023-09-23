// 최고의 집합.  2023-09-24


#include <vector>

using namespace std;

vector<int> ans;

vector<int> solution(int N, int S) {
    
    if (S < N)
    {
        ans.push_back(-1);
        return ans;
    }
    
    int div = S / N;
    int mod = S % N;
    for (int _ = 0; _ < N - mod; ++_)
    {
        ans.push_back(div);
    }
    for (int _ = 0; _ < mod; ++_)
    {
        ans.push_back(div + 1);
    }
    
    return ans;
}

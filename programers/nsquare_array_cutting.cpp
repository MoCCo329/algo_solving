// n^2 배열 자르기  2023-08-06


#include <string>
#include <vector>

using namespace std;

vector<int> solution(int N, long long left, long long right) {
    vector<int> ans;
    
    for (long long k = left; k <= right; ++k)
    {
        int i = k / N + 1, j = k % N + 1;
        if (j <= i) ans.push_back(i);
        else ans.push_back(j);
    }
    
    return ans;
}
// 우박수열 정적분.  2023-07-24


#include <vector>

using namespace std;

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> ans;
    vector<int> acc;
    vector<int> nums;
    int size;
    
    acc.push_back(k);
    nums.push_back(k);
    
    while (k != 1)
    {
        if (k % 2 == 1) k = 3 * k + 1;
        else k /= 2;
        
        acc.push_back(acc.back() + k);
        nums.push_back(k);
    }
    size = nums.size();
    
    for (int i = 0; i < ranges.size(); ++i)
    {
        int s = ranges[i][0], e = size - 1 + ranges[i][1];
        if (e < s) ans.push_back(-1.0);
        else
        {
            int temp = acc[e] - acc[s] - nums[e];
            temp *= 2;
            ans.push_back((double) (temp + nums[e] + nums[s]) / 2);
        }
    }
    
    
    return ans;
}
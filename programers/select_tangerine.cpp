// 귤 고르기.  2023-07-18


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int ans = 0;
    int tot = 0;
    vector<int> counts(10000001);
    
    for (int n: tangerine) counts[n]++;
    sort(counts.begin(), counts.end(), greater<int>());
    
    while (tot < k) tot += counts[ans++];
    
    return ans;
}
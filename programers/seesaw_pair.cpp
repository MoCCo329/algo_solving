// 시소 짝궁.  2023-07-11


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int counts[100000];

long long solution(vector<int> weights) {
    long long ans = 0;
    int N = weights.size();
    
    for (int w: weights) counts[w]++;
    
    long temp_ans = 0;
    for (int w: weights) {
        temp_ans += counts[w] - 1;
        if (w % 2 == 0) ans += counts[w / 2];
        if (w % 3 == 0) ans += counts[w / 3 * 2];
        if (w % 4 == 0) ans += counts[w / 4 * 3];
    }
    
    return ans + temp_ans / 2;
}
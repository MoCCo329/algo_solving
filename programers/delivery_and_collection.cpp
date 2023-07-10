// 택배 배달과 수거하기  2023-07-10


#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int N, vector<int> deliveries, vector<int> pickups) {
    long long ans = 0;
    int i = N - 1;
    int j = N - 1;
    
    while (0 <= i && deliveries[i] == 0) --i;
    while (0 <= j && pickups[j] == 0) --j;
    
    while (0 <= i || 0 <= j) {
        ans += (max(i, j) + 1) * 2;
        
        int temp = cap;
        while (0 <= i) {
            if (temp < deliveries[i]) {
                deliveries[i] -= temp;
                break;
            } else {
                temp -= deliveries[i];
                --i;
            }
        }
        
        temp = cap;
        while (0 <= j) {
            if (temp < pickups[j]) {
                pickups[j] -= temp;
                break;
            } else {
                temp -= pickups[j];
                --j;
            }
        }
    }
    
    return ans;
}
// 연속 부분 수열 합의 개수.  2023-07-17


#include <vector>

using namespace std;

int counts[1000000];

int solution(vector<int> elements) {
    int ans = 0;
    int size = elements.size();
    int l = 0;
    int i = 0;
    int tot = 0;
    
    while (l < size) {
        i = 0;
        tot += elements[l++];
        
        while (true) {
            if (counts[tot]++ == 0) ans += 1;
            tot += elements[(i + l) % size] - elements[i];
            i++;
            if (i == size) break;
        }
    }
        
    return ans;
}
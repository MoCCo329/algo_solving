// 구명보트.  2023-08-03


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int ans = 0;
    sort(people.begin(), people.end());
    
    int l = 0;
    int r = people.size() - 1;
    while (l <= r)
    {
        if (people[l] + people[r] <= limit)
        {
            ++l;
            --r;
        }
        else --r;
        ans++;
    }
    
    return ans;
}
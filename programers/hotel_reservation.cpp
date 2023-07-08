// 호텔 대실  2023-07-08


#include <string>
#include <vector>
#include <queue>

using namespace std;

int get_time(string s) {
    return (s[0] - '0') * 600 + (s[1] - '0') * 60 + (s[3] - '0') * 10 + (s[4] - '0');
}

int solution(vector<vector<string>> book_time) {
    int ans = 0;
    int cnt = 0;
    priority_queue<pair<int, int>> pq;
    
    for (vector<string> book: book_time)
    {
        pq.push(make_pair(-get_time(book[0]), -1));
        pq.push(make_pair(-get_time(book[1]) - 10, 1));
    }
    
    while (!pq.empty())
    {
        cnt -= pq.top().second;
        pq.pop();
        ans = ans < cnt ? cnt : ans;
    }
    
    return ans;
}
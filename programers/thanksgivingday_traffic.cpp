// 추석 트래픽.  2023-10-07


#include <string>
#include <vector>
#include <queue>

using namespace std;

priority_queue<int> pq;
priority_queue<pair<int, int> > order_pq;

int get_end_time(string s)
{
    int t = 0;
    t += stoi(s.substr(20, 3));
    t += 1000 * stoi(s.substr(17, 2));
    t += 60000 * stoi(s.substr(14, 2));
    t += 3600000 * stoi(s.substr(11, 2));
    
    return t;
}

int get_start_time(string s)
{
    int t = get_end_time(s);
    string temp = s.substr(24);
    t -= (int)(1000 * stof(temp.substr(0, temp.size() - 1))) - 1;
    
    return t;
}

int solution(vector<string> lines)
{
    for (int i = 0; i < lines.size(); ++i)
    {
        order_pq.push(make_pair(-get_start_time(lines[i]), i));
    }
    
    int ans = 1;
    while (!order_pq.empty())
    {
        int i = order_pq.top().second;
        order_pq.pop();
        string line = lines[i];
        
        int start = get_start_time(line);
        int end = get_end_time(line);
        while (!pq.empty() && -pq.top() <= start - 1000) pq.pop();
        pq.push(-end);
        ans = ans < pq.size() ? pq.size() : ans;
    }

    return ans;
}

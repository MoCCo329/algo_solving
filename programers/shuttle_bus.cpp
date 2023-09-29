// [1차] 셔틀 버스.  2023-09-30


#include <string>
#include <vector>
#include <queue>

using namespace std;

bool vis[2000];
priority_queue<pair<int, int> > pq;
int now;
int bus_time;
int ans;

int conv_time(string s)
{
    return stoi(s.substr(0, 2)) * 60 + stoi(s.substr(3, 2));
}

void insert_crew(vector<string> &t)
{
    while (!pq.empty()) pq.pop();
    
    for (int i = 0; i < t.size(); ++i)
    {
        if (vis[i]) continue;
        int temp = conv_time(t[i]);
        if (bus_time < temp) continue;
        pq.push(make_pair(-temp, i));
    }
}

string solution(int n, int t, int m, vector<string> timetable)
{
    bus_time = 540;
    
    for (int bus = 0; bus < n; ++bus)
    {
        insert_crew(timetable);
        int cnt = 0;
        while (!pq.empty() && cnt++ < m)
        {
            pair<int, int> temp = pq.top();
            pq.pop();
            now = -temp.first;
            if (bus == n - 1 && cnt == m) ans = now - 1;
            vis[temp.second] = true;
        }
        if (bus == n - 1 && cnt < m) ans = bus_time;
        bus_time += t;
    }
    
    string temp_ans = "";
    temp_ans += ans / 60 < 10 ? ("0" + to_string(ans / 60)) : to_string(ans / 60);
    temp_ans += ":";
    temp_ans += ans % 60 < 10 ? ("0" + to_string(ans % 60)) : to_string(ans % 60);
    
    return temp_ans;
}

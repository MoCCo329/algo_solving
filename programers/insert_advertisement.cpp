// 광고 삽입.  2023-10-01


#include <string>
#include <vector>

using namespace std;

int time_s[360000];
int time_e[360000];
int l;
int r;
int curr_l;
int curr_r;
long long acc;
long long ans_v;
int ans;

int conv_time(string s)
{
    return 3600 * stoi(s.substr(0, 2)) + 60 * stoi(s.substr(3, 2)) + stoi(s.substr(6, 2));
}

string solution(string play_time, string adv_time, vector<string> logs)
{
    for (string log: logs)
    {
        time_s[conv_time(log.substr(0, 8))] += 1;
        time_e[conv_time(log.substr(9))] += 1;
    }
    
    l = 0;
    r = 0;
    for (int size = conv_time(adv_time); r < size; ++r)
    {
        curr_r += time_s[r] - time_e[r];
        acc += curr_r;
    }
    
    int size = 360000 < conv_time(play_time) ? 360000 : conv_time(play_time);
    for (int _ = r; _ < size; ++_, ++l, ++r)
    {
        if (ans_v < acc)
        {
            ans_v = acc;
            ans = l;
        }
        curr_l += time_s[l] - time_e[l];
        curr_r += time_s[r] - time_e[r];
        acc -= curr_l;
        acc += curr_r;
    }
    if (ans_v < acc)
    {
        ans_v = acc;
        ans = l;
    }
    
    string temp = ans / 3600 < 10 ? ("0" + to_string(ans / 3600)) : (to_string(ans / 3600));
    temp += ":";
    temp += (ans % 3600) / 60 < 10 ? ("0" + to_string((ans % 3600) / 60)) : (to_string((ans % 3600) / 60));
    temp += ":";
    temp += (ans % 60) < 10 ? ("0" + to_string(ans % 60)) : (to_string(ans % 60));
    
    return temp;
}

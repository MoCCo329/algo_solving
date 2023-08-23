// 이모티콘 할인행사.  2023-08-23


#include <vector>

using namespace std;

int emo_size;
int user_size;
int ans[2];
int sale[7];
int discount_list[4] = { 10, 20, 30, 40 };
vector<vector<int>> *users;
vector<int> *emoticons;

int* get_result()
{
    static int temp_ans[2];
    temp_ans[0] = 0, temp_ans[1] = 0;
    
    for (int i = 0; i < user_size; ++i)
    {
        int p = 0;
        int percent = (*users)[i][0];
        int limit = (*users)[i][1];
        
        for (int j = 0; j < emo_size; ++j)
        {
            if (percent <= sale[j])
            {
                p += (*emoticons)[j] * (100 - sale[j]) / 100;
                if (limit <= p) break;
            }
        }
        
        if (limit <= p) temp_ans[0]++;
        else temp_ans[1] += p;
    }
    
    return temp_ans;
}

void dfs(int k)
{
    if (k == emo_size)
    {
        int* temp = get_result();
        if (ans[0] < temp[0] || (ans[0] == temp[0] && ans[1] < temp[1]))
        {
            ans[0] = temp[0];
            ans[1] = temp[1];
        }
        return;
    }
    
    for (double discount: discount_list)
    {
        sale[k] = discount;
        dfs(k + 1);
    }
}

vector<int> solution(vector<vector<int>> _users, vector<int> _emoticons) {
    users = &_users;
    emoticons = &_emoticons;
    emo_size = _emoticons.size();
    user_size = _users.size();
    ans[0] = 0, ans[1] = 0;
    
    dfs(0);
    
    vector<int> res = { ans[0], ans[1] };
    return res;
}

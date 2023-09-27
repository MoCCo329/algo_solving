// 다단계 칫솔 판매.  2023-09-28


#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int uf[10001];
int unordered_ans[10001];
int hm_idx;
unordered_map<string, int> hm;

int get_hash(string s)
{
    if (hm.count(s) == 1) return hm[s];
    hm_idx++;
    hm.insert({s, hm_idx});
    return hm[s];
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount)
{
    int size = enroll.size();
    int temp;
    
    for (int i = 0; i < size; ++i)
    {
        int c = get_hash(enroll[i]);
        int p = referral[i] == "-" ? 0 : get_hash(referral[i]);
        
        uf[c] = p;
    }
    
    size = seller.size();
    for (int i = 0; i < size; ++i)
    {
        int c = get_hash(seller[i]);
        int cost = amount[i] * 100;
        
        if (uf[c] == c) unordered_ans[c] += cost;
        else
        {
            temp = cost / 10;
            unordered_ans[c] += cost - temp;
            cost = temp;
        }
        while (uf[c] != c && cost != 0)
        {
            c = uf[c];
            temp = cost / 10;
            unordered_ans[c] += cost - temp;
            cost = temp;
        }
    }
    
    vector<int> ans;
    for (string s: enroll)
    {
        int c = get_hash(s);
        ans.push_back(unordered_ans[c]);
    }
    
    return ans;
}

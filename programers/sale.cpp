// 할인 행사.  2023-08-12


#include <string>
#include <vector>

using namespace std;

int w_size;
int counts[11];
int is_full[11];
int full_value[10];
char* hash_arr[10];

void set_hash(char* s, int n)
{
    for (int i = 0; i < w_size; ++i)
    {
        if (hash_arr[i] == nullptr)
        {
            hash_arr[i] = s;
            full_value[i] = n;
            break;
        }
    }
}

int get_hash(char* s)
{
    for (int i = 0; i < w_size; ++i)
    {
        bool is_match = true;
        for (int j = 0; j < 13; ++j)
        {
            if (hash_arr[i][j] != s[j])
            {
                is_match = false;
                break;
            }
            if (hash_arr[i][j] == 0 && s[j] == 0) break;
        }
        if (is_match) return i;
    }
    
    return 10;
}

bool test()
{
    for (int i = 0; i < w_size; ++i)
    {
        if (!is_full[i]) return false;
    }
    return true;
}

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int ans = 0;
    int cnt = 0;
    w_size = want.size();
    
    for (int i = 0; i < w_size; ++i)
    {
        set_hash((char*) want[i].c_str(), number[i]);
    }
    
    for (int i = 0; i < discount.size(); ++i)
    {
        if (9 < i)
        {
            int hv = get_hash((char*) discount[i - 10].c_str());
            if (full_value[hv] == counts[hv]) is_full[hv] = false;
            counts[hv]--;
        }
        
        int hv = get_hash((char*) discount[i].c_str());
        counts[hv]++;
        if (full_value[hv] == counts[hv]) is_full[hv] = true;
        
        if (test()) ans++;
    }
    
    return ans;
}

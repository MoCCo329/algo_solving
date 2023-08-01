// 스킬트리.  2023-08-01


#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int ans = 0;
    bool counts[26] = { false, };
    
    for (string s: skill_trees)
    {
        for (int i = 0; i < 26; ++i) counts[i] = false;
        for (char c: skill) counts[c - 'A'] = true;
        
        int i = 0;
        int j = 0;
        bool flag = false;
        while (j < s.size())
        {
            if (i < skill.size() && skill[i] == s[j])
            {
                counts[skill[i] - 'A'] = false;
                ++i;
                ++j;
            }
            else if (counts[s[j] - 'A'] == true)
            {
                flag = true;
                break;
            }
            else ++j;
        }
        
        if (!flag) ans++;
    }
    
    return ans;
}
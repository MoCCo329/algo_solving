// 추억 점수  2023-07-03


#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> ans;
map<string, int> n_to_score;
int temp;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    
    for (int i = 0; i < name.size(); ++i) n_to_score[name[i]] = yearning[i];
    for (int i = 0; i < photo.size(); ++i)
    {
        temp = 0;
        for (int j = 0; j < photo[i].size(); ++j) temp += n_to_score[photo[i][j]];
        ans.push_back(temp);
    }
    
    return ans;
}
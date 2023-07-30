// 방문 길이.  2023-07-30


#include <string>
using namespace std;

bool hash_row[110];
bool hash_col[110];

int solution(string dirs) {
    int i = 5, j = 5;
    int ans = 0;
    
    for (char d: dirs)
    {
        if (d == 'U')
        {
            if (i == 0) continue;
            if (!hash_col[(i - 1) * 11 + j])
            {
                ans++;
                hash_col[(i - 1) * 11 + j] = true;
            }
            i--;
        }
        else if (d == 'D')
        {
            if (i == 10) continue;
            if (!hash_col[i * 11 + j])
            {
                ans++;
                hash_col[i * 11 + j] = true;
            }
            i++;
        }
        else if (d == 'R')
        {
            if (j == 10) continue;
            if (!hash_row[i * 10 + j])
            {
                ans++;
                hash_row[i * 10 + j] = true;
            }
            j++;
        }
        else
        {
            if (j == 0) continue;
            if (!hash_row[i * 10 + j - 1])
            {
                ans++;
                hash_row[i * 10 + j - 1] = true;
            }
            j--;
        }
    }
    
    return ans;
}
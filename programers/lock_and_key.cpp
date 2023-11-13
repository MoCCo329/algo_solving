// 자물쇠와 열쇠.  2023-11-14


#include <vector>

using namespace std;

void rotate(vector<vector<int> > &key)
{
    int M = key.size();
    vector<vector<int> > temp(M);
    for (int i = 0; i < M; ++i) temp[i] = vector<int>(M);
    
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            temp[j][M - 1 - i] = key[i][j];
        }
    }
    
    key = temp;
}

bool test(vector<vector<int> > key, vector<vector<int> > lock, int cnt)
{
    int key_cnt;
    bool flag;
    int N = lock.size();
    int M = key.size();
    
    for (int base_i = -M + 1; base_i < N; ++base_i)
    {
        for (int base_j = -M + 1; base_j < N; ++base_j)
        {
            key_cnt = 0;
            flag = true;
            for (int i = 0; i < M; ++i)
            {
                if (!flag) break;
                for (int j = 0; j < M; ++j)
                {
                    int ni = i + base_i, nj = j + base_j;
                    if (ni < 0 || N <= ni || nj < 0 || N <= nj) continue;
                    if (key[i][j] == 1 && lock[ni][nj] == 0) ++key_cnt;
                    if (key[i][j] == 1 && lock[ni][nj] == 1)
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if (key_cnt == cnt && flag) return true;
        }
    }
    return false;
}

bool solution(vector<vector<int> > key, vector<vector<int> > lock)
{
    int cnt = 0;
    int N = lock.size();
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (lock[i][j] == 0)
            {
                ++cnt;
            }
        }
    }
    
    if (test(key, lock, cnt)) return true;
    
    rotate(key);
    if (test(key, lock, cnt)) return true;
    
    rotate(key);
    if (test(key, lock, cnt)) return true;
    
    rotate(key);
    if (test(key, lock, cnt)) return true;
    
    return false;
}

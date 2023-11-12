// 단체사진 찍기.  2023-11-12


#include <string>
#include <vector>

using namespace std;

vector<string> *datas;
int vis[8];
int ans;
int c_to_i[26] = { 0, 0, 1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 4, 5, 0, 0, 0, 6, 0, 7, 0, 0, 0, 0, 0, 0 };
int N;

bool test()
{
    for (int i = 0; i < N; ++i)
    {
        int a = c_to_i[(*datas)[i][0] - 'A'];
        int b = c_to_i[(*datas)[i][2] - 'A'];
        
        if ((*datas)[i][3] == '=')
        {
            if (abs(vis[a] - vis[b]) - 1 != ((*datas)[i][4]) - '0') return false;
        }
        else if ((*datas)[i][3] == '>')
        {
            if (abs(vis[a] - vis[b]) - 1 <= ((*datas)[i][4]) - '0') return false;
        }
        else
        {
            if (abs(vis[a] - vis[b]) - 1 >= ((*datas)[i][4]) - '0') return false;
        }
    }
    return true;
}

void make_sequence(int k)
{
    if (k == 8)
    {
        if (test()) ++ans;
        return;
    }
    
    for (int i = 0; i < 8; ++i)
    {
        if (vis[i] != -1) continue;
        vis[i] = k;
        make_sequence(k + 1);
        vis[i] = -1;
    }
}

int solution(int n, vector<string> _data)
{
    datas = &_data;
    N = n;
    for (int i = 0; i < 8; ++i) vis[i] = -1;
    ans = 0;
    
    make_sequence(0);
    
    return ans;
}

// N으로 표현.  2023-10-06


#include <vector>
#include <unordered_set>

using namespace std;

vector<unordered_set<int> > s_list(9);

int solution(int N, int number)
{
    int temp = N;
    int cnt = 0;
    while (temp < 64001)
    {
        s_list[++cnt].insert(temp);
        temp = temp * 10 + N;
    }
    
    for (int i = 1; i < 8; ++i)
    {
        for (int j = 1; j <= i; ++j)
        {
            if (8 < i + j) continue;
            for (int n1: s_list[i])
            {
                for (int n2: s_list[j])
                {
                    long t = stol(to_string(n1) + "" + to_string(n2));
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert((int) temp);

                    temp = n1 / n2;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);
                    
                    temp = n2 / n1;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);

                    temp = n1 * n2;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);

                    temp = n1 - n2;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);
                    
                    temp = n2 - n1;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);

                    temp = n1 + n2;
                    if (0 < temp && temp < 64001 && i + j < 9)
                        s_list[i + j].insert(temp);
                }
            }
        }
        
        for (int k = 1; k < 9; ++k)
        {
            if (s_list[k].find(number) != s_list[k].end()) return k;
        }
    }
    
    return -1;
}

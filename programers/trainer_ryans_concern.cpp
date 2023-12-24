// 몸짱 트레이너 라이언의 고민.  2023-12-24


#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N;

int abs(int a)
{
    return a < 0 ? -a : a;
}

bool test(int idx1, vector<int> &list, int d)
{
    int i1 = idx1 / N, j1 = idx1 % N;
    for (int idx2: list)
    {
        int i2 = idx2 / N, j2 = idx2 % N;
        if (abs(i1 - i2) + abs(j1 - j2) < d) return false;
    }
    return true;
}

int solution(int _N, int M, vector<vector<int> > timetable)
{
    priority_queue<int> pq;
    int max_v = 0;
    sort(timetable.begin(), timetable.end());
    
    for (vector<int> time: timetable)
    {
        while (!pq.empty() && -pq.top() < time[0])
        {
            pq.pop();
        }
        pq.push(-time[1]);
        if (max_v < pq.size()) max_v = pq.size();
    }
    if (max_v == 1) return 0;
    if (max_v == 2) return (_N - 1) * 2;
    if ((_N * _N + 1) / 2 < max_v) return 1;
    
    N = _N;
    int NN = N * N;
    for (int d = (N - 1) * 2 - 1; 2 < d; --d)
    {
        for (int i = 0; i < NN - max_v + 1; ++i)
        {
            vector<int> list;
            list.push_back(i);
            for (int j = i + 1; j < NN; ++j)
            {
                if (test(j, list, d))
                {
                    list.push_back(j);
                    if (max_v == list.size()) return d;
                }
            }
        }
    }
    
    return 2;
}

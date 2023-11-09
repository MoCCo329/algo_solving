// 소수 찾기.  2023-11-09


#include <string>

using namespace std;

bool memo[100000000];
int counts[10];
int N;
int max_n;
int ans;

void make_nums(int k, int num)
{
    if (!memo[num]) ++ans;
    memo[num] = true;
    max_n = max(max_n, num);
    
    for (int i = 0; i < 10; ++i)
    {
        if (counts[i] != 0)
        {
            counts[i]--;
            make_nums(k + 1, num * 10 + i);
            counts[i]++;
        }
    }
}

int solution(string numbers)
{
    N = numbers.size();
    for (int i = 0; i < N; ++i)
    {
        counts[numbers[i] - '0']++;
    }
    
    make_nums(0, 0);
    if (memo[0]) --ans;
    if (memo[1]) --ans;
    
    int n = 2;
    while (n * n <= max_n)
    {
        int temp = n * 2;
        while (temp <= max_n)
        {
            if (memo[temp]) --ans, memo[temp] = false;
            temp += n;
        }
        ++n;
    }
    
    return ans;
}

// 모음사전.  2023-08-27


#include <string>

using namespace std;

int get_c(char c)
{
    switch (c)
    {
        case 'A':
            return 0;
        case 'E':
            return 1;
        case 'I':
            return 2;
        case 'O':
            return 3;
        case 'U':
            return 4;
    }
}

int get_count(int k)
{
    int ans = 0;
    int temp = 1;
    for (int l = k; l < 5; ++l)
    {
        ans += temp;
        temp *= 5;
    }
    return ans;
}

int solution(string word)
{
    int size = word.size();
    
    int ans = size;
    for (int i = 0; i < size; ++i)
    {
        int j_size = get_c(word[i]);
        for (int j = 0; j < j_size; ++j)
        {
            ans += get_count(i);
        }
    }
    
    return ans;
}

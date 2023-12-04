// 가장 큰 수.  2023-12-04


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(int a, int b)
{
    string AB = to_string(a) + to_string(b);
    string BA = to_string(b) + to_string(a);
    
    int i = 0;
    while (i < AB.size())
    {
        if (AB[i] != BA[i]) return AB[i] > BA[i];
        ++i;
    }
    return a > b;
}

string solution(vector<int> numbers)
{
    sort(numbers.begin(), numbers.end(), comp);
    
    string ans = "";
    for (int number: numbers)
    {
        ans = ans + to_string(number);
    }
    
    if (ans[0] == '0') return "0";
    return ans;
}

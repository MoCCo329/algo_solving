// 123 나라의 숫자.  2023-11-22


#include <string>

using namespace std;

int remain;

string solution(int n)
{
    string ans = "";
    
    while (true)
    {
        if (n == 0) break;
        remain = n % 3;
        if (remain == 1)
        {
            ans = '1' + ans;
        }
        else if (remain == 2)
        {
            ans = '2' + ans;
        }
        else
        {
            ans = '4' + ans;
            n -= 3;
        }
        n /= 3;
    }
    
    return ans;
}

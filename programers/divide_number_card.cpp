// 숫자 카드 나누기.  2023-10-17


#include <string>
#include <vector>

using namespace std;

int candi1, candi2;
bool avail1, avail2;
int temp;

int gcd(int a, int b)
{
    if (a < b)
    {
        int temp = a;
        a = b;
        b = temp;
    }
    
    while (b != 0)
    {
        int temp = a % b;
        if (b < temp)
        {
            a = temp;
        }
        else
        {
            a = b;
            b = temp;
        }
    }
    
    return a;
}

int solution(vector<int> arrayA, vector<int> arrayB)
{
    candi1 = arrayA[0], candi2 = arrayB[0];
    avail1 = true, avail2 = true;
    
    for (int i = 1; i < arrayA.size(); ++i)
    {
        candi1 = gcd(candi1, arrayA[i]);
    }
    for (int j = 0; j < arrayB.size(); ++j)
    {
        if (arrayB[j] % candi1 == 0)
        {
            avail1 = false;
            break;
        }
    }
    
    for (int i = 1; i < arrayB.size(); ++i)
    {
        candi2 = gcd(candi2, arrayB[i]);
    }
    for (int j = 0; j < arrayA.size(); ++j)
    {
        if (arrayA[j] % candi2 == 0)
        {
            avail2 = false;
            break;
        }
    }
    
    if (!avail1 && !avail2) return 0;
    if (!avail1) return candi2;
    if (!avail2) return candi1;
    return candi1 < candi2 ? candi2 : candi1;
}

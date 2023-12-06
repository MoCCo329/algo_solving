// 다음 큰 숫자.  2023-12-07


int tot = 0;

bool test(int n)
{
    int k = 0;
    int temp_tot = 0;
    
    while ((1 << k) <= n)
    {
        if ((1 << k) & n)
        {
            ++temp_tot;
        }
        ++k;
    }
    
    if (temp_tot == tot) return true;
    return false;
}

int solution(int n)
{
    int k = 0;
    while ((1 << k) <= n)
    {
        if ((1 << k) & n)
        {
            ++tot;
        }
        ++k;
    }
    
    while (!test(++n))
    {
    }
    
    return n;
}

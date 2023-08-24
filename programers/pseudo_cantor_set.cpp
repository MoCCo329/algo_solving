// 유사 칸토어 비트열.  2023-08-24


long long memo[20] = { 1, 5, 25, 125, 625, };

long long pow2(int k)
{
    if (memo[k] != 0) return memo[k];
    
    long long temp = pow2(k / 2);
    if (k % 2 == 1) memo[k] = temp * temp * 5;
    else memo[k] = temp * temp;
    return memo[k];
}

int get_cnt(int k, long long l, long long r)
{
    if (k == 0) return 1;
    
    int temp_ans = 0;
    long long div = pow2(k - 1);
    long long L = l / div;
    long long R = r / div;
    
    for (int i = L; i <= R; ++i)
    {
        if (i == 2) continue;
        if (L == R) temp_ans += get_cnt(k - 1, l - L * div, r - R * div);
        else if (i == L) temp_ans += get_cnt(k - 1, l - L * div, div - 1);
        else if (i == R) temp_ans += get_cnt(k - 1, 0, r - R * div);
        else temp_ans += get_cnt(k - 1, 0, div - 1);
    }
    return temp_ans;
}

int solution(int n, long long l, long long r)
{    
    return get_cnt(n, l - 1, r - 1);
}

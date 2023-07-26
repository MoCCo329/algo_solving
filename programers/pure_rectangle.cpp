// 멀쩡한 사각형.  2023-07-26


using namespace std;

long long solution(int w,int h) {
    long long ans = 0;
    
    if (h < w)
        for (int i = 1; i < h; ++i)
            ans += ((long long) w * i) / h;
    else
        for (int i = 1; i < w; ++i)
            ans += ((long long) h * i) / w;
    
    return ans * 2;
}
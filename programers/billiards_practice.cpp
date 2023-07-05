// 당구 연습  2023-07-05


#include <string>
#include <vector>

using namespace std;

bool test(int x1, int y1, int x2, int y2, int x3, int y3)
{
    if (x1 == x2) {
        if (y1 < y2 && y1 < y3 && y3 < y2) return false;
        if (y2 < y1 && y2 < y3 && y3 < y1) return false;
        return true;
    }
    if (y1 == y2) {
        if (x1 < x2 && x1 < x3 && x3 < x2) return false;
        if (x2 < x1 && x2 < x3 && x3 < x1) return false;
        return true;
    }
    if (y3 == ((float)(y2 - y1) / (x2 - x1) * (float)(x3 - x1) + y1)) return false;
    
    return true;
}

void get_max_v(int x1, int y1, int x2, int y2, int* max_v)
{
    int temp = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    *max_v = *max_v < temp ? *max_v : temp;
}


vector<int> solution(int m, int n, int x1, int y1, vector<vector<int>> balls) {
    vector<int> ans;
    int x2 = 0, y2 = 0;
    
    for (vector<int> ball: balls) {
        int max_v = n * n + m * m;
        
        x2 = 2 * m - ball[0], y2 = ball[1];
        if (test(x1, y1, x2, y2, ball[0], ball[1]))
            get_max_v(x1, y1, x2, y2, &max_v);
        x2 = -ball[0], y2 = ball[1];
        if (test(x1, y1, x2, y2, ball[0], ball[1]))
            get_max_v(x1, y1, x2, y2, &max_v);
        x2 = ball[0], y2 = 2 * n - ball[1];
        if (test(x1, y1, x2, y2, ball[0], ball[1]))
            get_max_v(x1, y1, x2, y2, &max_v);
        x2 = ball[0], y2 = -ball[1];
        if (test(x1, y1, x2, y2, ball[0], ball[1]))
            get_max_v(x1, y1, x2, y2, &max_v);
        
        ans.push_back(max_v);
    }
    
    return ans;
}
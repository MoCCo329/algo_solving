// 택배상자.  2023-07-16


#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    int size = order.size();
    stack<int> s;
    
    int i = 0;
    int n = 1;
    while (i < size)
    {
        if (order[i] == n) (i++, n++);
        else if (!s.empty() && order[i] == s.top()) (s.pop(), i++);
        else {
            while (order[i] != n && n <= size) s.push(n++);
            if (order[i] != n) break;
            i++;
            n++;
        }
    }
    
    return i;
}
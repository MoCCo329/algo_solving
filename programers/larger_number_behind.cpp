// 뒤에 있는 큰 수 찾기  2023-07-10


#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> ans(numbers.size(), -1);
    stack<int> stack;
    
    for (int i = 0; i < numbers.size(); ++i) {
        while (!stack.empty() && numbers[stack.top()] < numbers[i]) {
            ans[stack.top()] = numbers[i];
            stack.pop();
        }
        stack.push(i);
    }
    
    return ans;
}
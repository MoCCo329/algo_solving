// 혼자서 하는 틱택토.  2023-07-21


#include <string>
#include <vector>

using namespace std;

bool check(char c, int x_cnt, int o_cnt) {
    if (c == 'O' && x_cnt == o_cnt) return false;
    if (c == 'X' && (x_cnt + 1) == o_cnt) return false;
    return true;
}

int solution(vector<string> board) {
    int o_cnt = 0;
    int x_cnt = 0;
    
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == 'O') o_cnt++;
            else if (board[i][j] == 'X') x_cnt++;
        }
    }
    if (x_cnt != o_cnt && (x_cnt + 1) != o_cnt) return 0;
    
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] != '.' && board[i][0] == board[i][1] && board[i][1] == board[i][2]) if (!check(board[i][0], x_cnt, o_cnt)) return 0;
        if (board[0][i] != '.' && board[0][i] == board[1][i] && board[1][i] == board[2][i]) if (!check(board[0][i], x_cnt, o_cnt)) return 0;
    }
    if (board[0][0] != '.' && board[0][0] == board[1][1] && board[1][1] == board[2][2]) if (!check(board[0][0], x_cnt, o_cnt)) return 0;
    if (board[2][0] != '.' && board[2][0] == board[1][1] && board[1][1] == board[0][2]) if (!check(board[2][0], x_cnt, o_cnt)) return 0;
    
    return 1;
}
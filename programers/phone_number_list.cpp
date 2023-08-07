// 전화번호 목록.  2023-08-07


#include <string.h>
#include <string>
#include <vector>

using namespace std;

typedef struct Node {
    struct Node* children[10];
    bool isEnd;
} Node;
Node root;

bool solution(vector<string> phone_book) {
    
    for (string s: phone_book)
    {
        Node* now = &root;
        bool flag = true;
        for (char c: s)
        {
            flag = true;
            if ((now->children)[c - '0'] == NULL)
            {
                flag = false;
                Node* newNode = NULL;
                while (newNode == NULL)
                    newNode = (Node*) malloc(sizeof(Node));
                memset(newNode, 0, sizeof(Node));
                (now->children)[c - '0'] = newNode;
            }
            now = (now->children)[c - '0'];
            
            if (now->isEnd) return false;
        }
        if (flag) return false;
        now->isEnd = true;
    }
    
    return true;
}
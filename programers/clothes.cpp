// 의상.  2023-08-16


#include <string>
#include <vector>

using namespace std;

int type_idx;
int type_count[30];
string type_name[30];

void apply_dict(string type)
{
    for (int i = 0; i < type_idx; ++i)
    {
        if (type_name[i] == type)
        {
            type_count[i]++;
            return;
        }
    }
    
    type_count[type_idx]++;
    type_name[type_idx++] = type;
}

int solution(vector<vector<string>> clothes) {
    
    for (vector<string> c_vector: clothes)
    {
        apply_dict(c_vector[1]);
    }
    
    int ans = 1;
    for (int i = 0; i < type_idx; ++i) ans *= type_count[i] + 1;
    
    return ans - 1;
}



/*
아래 코드는 실패한다.
std::basic_string<CharT,Traits,Allocator>::c_str 레퍼런스를 보면 주소를 재활용 한다.
The pointer obtained from may be invalidated by: c_str()
*/ 

#include <string>
#include <vector>

using namespace std;

int type_idx;
int type_count[30];
char* type_name[30];

void apply_dict(char* type)
{
    for (int i = 0; i < type_idx; ++i)
    {
        char* c1 = type_name[i];
        char* c2 = type;
        bool is_match = true;
        while (*c1 != 0 && *c2 != 0)
        {
            if (*c1 != *c2)
            {
                is_match = false;
                break;
            }
            c1++;
            c2++;
        }
        
        if (is_match)
        {
            type_count[i]++;
            return;
        }
    }
    
    type_count[type_idx]++;
    type_name[type_idx++] = type;
}

int solution(vector<vector<string>> clothes) {
    
    for (int i = 0; i < clothes.size(); ++i)
    {
        apply_dict((char*) clothes[i][1].c_str());
    }
    
    int ans = 1;
    for (int i = 0; i < type_idx; ++i) ans *= type_count[i] + 1;
    
    return ans - 1;
}

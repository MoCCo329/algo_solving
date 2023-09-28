// 길 찾기 게임.  2023-09-29


#include <vector>
#include <algorithm>

using namespace std;

int children[10000][2];
vector<vector<int> > ans(2);

bool my_comp(vector<int> &a, vector<int> &b)
{
    if (a[1] != b[1]) return a[1] > b[1];
    return a[0] < b[0];
}

void pre(vector<vector<int> > &nodeinfo, int i)
{
    ans[0].push_back(nodeinfo[i][2]);
    if (children[i][0] != 0) pre(nodeinfo, children[i][0]);
    if (children[i][1] != 0) pre(nodeinfo, children[i][1]);
}

void post(vector<vector<int> > &nodeinfo, int i)
{
    if (children[i][0] != 0) post(nodeinfo, children[i][0]);
    if (children[i][1] != 0) post(nodeinfo, children[i][1]);
    ans[1].push_back(nodeinfo[i][2]);
}

vector<vector<int>> solution(vector<vector<int> > nodeinfo)
{
    for (int i = 0; i < nodeinfo.size(); ++i)
    {
        nodeinfo[i].push_back(i + 1);
    }
    sort(nodeinfo.begin(), nodeinfo.end(), my_comp);
    
    for (int i = 1; i < nodeinfo.size(); ++i)
    {
        int temp = 0;
        while (nodeinfo[temp][1] > nodeinfo[i][1])
        {
            if (nodeinfo[temp][0] < nodeinfo[i][0] && children[temp][1] != 0) temp = children[temp][1];
            else if (nodeinfo[i][0] < nodeinfo[temp][0] && children[temp][0] != 0) temp = children[temp][0];
            else break;
        }
        if (nodeinfo[i][0] < nodeinfo[temp][0]) children[temp][0] = i;
        else children[temp][1] = i;
    }
    
    pre(nodeinfo, 0);
    post(nodeinfo, 0);
    
    return ans;
}

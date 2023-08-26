// 테이블 해시 함수.  2023-08-26


#include <vector>

using namespace std;

vector<vector<int>>* table;
int i_size;
int j_size;
int p;
int sorted_t[2500][500];

void merge(int l, int m, int r);

void merge_sort(int l, int r)
{
    if (r <= l) return;
    
    int m = (l + r) / 2;
    merge_sort(l, m);
    merge_sort(m + 1, r);
    merge(l, m, r);
}

void merge(int l, int m, int r)
{
    int i = l, j = m + 1;
    int idx = l;
    while (i <= m && j <= r)
    {
        if ((*table)[i][p] == (*table)[j][p])
        {
            if ((*table)[i][0] < (*table)[j][0])
            {
                for (int k = 0; k < j_size; ++k)
                    sorted_t[idx][k] = (*table)[j][k];
                j++;
                idx++;
            }
            else
            {
                for (int k = 0; k < j_size; ++k)
                    sorted_t[idx][k] = (*table)[i][k];
                i++;
                idx++;
            }
        }
        else if ((*table)[i][p] < (*table)[j][p])
        {
            for (int k = 0; k < j_size; ++k)
                sorted_t[idx][k] = (*table)[i][k];
            i++;
            idx++;
        }
        else
        {
            for (int k = 0; k < j_size; ++k)
                sorted_t[idx][k] = (*table)[j][k];
            j++;
            idx++;
        }
    }
    while (i <= m)
    {
        for (int k = 0; k < j_size; ++k)
            sorted_t[idx][k] = (*table)[i][k];
        i++;
        idx++;
    }
    while (j <= r)
    {
        for (int k = 0; k < j_size; ++k)
            sorted_t[idx][k] = (*table)[j][k];
        j++;
        idx++;
    }
    
    for (i = l; i <= r; ++i)
    {
        for (j = 0; j < j_size; ++j)
        {
            (*table)[i][j] = sorted_t[i][j];
        }
    }
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end)
{
    table = &data;
    i_size = data.size();
    j_size = data[0].size();
    p = col - 1;
    
    merge_sort(0, i_size - 1);

    long long ans = 0;
    for (int i = row_begin - 1; i < row_end; ++i)
    {
        long long temp_ans = 0;
        for (int j = 0; j < j_size; ++j)
        {
            temp_ans += data[i][j] % (i + 1);
        }
        ans ^= temp_ans;
    }
    
    return ans;
}

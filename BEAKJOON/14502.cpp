// 14502. 연구소 2024-03-18


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int N, M;
int maps[8][8];
int candi[64];
int candi_cnt;
int vir[10];
int vir_cnt;
int d_list[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int wall_cnt = 3;


int test()
{
	bool vis[8][8] = { false, };
	int queue[64] = { 0, };
	int front = 0, rear = 0;

	for (int idx = 0; idx < vir_cnt; ++idx)
	{
		queue[front++] = vir[idx];
		int i = vir[idx] / M, j = vir[idx] % M;
		vis[i][j] = true;
	}

	while (rear < front)
	{
		int temp = queue[rear++];
		int i = temp / M, j = temp % M;
		for (int d = 0; d < 4; ++d)
		{
			int ni = i + d_list[d][0], nj = j + d_list[d][1];
			if (ni < 0 || N <= ni || nj < 0 || M <= nj) continue;
			if (vis[ni][nj] || maps[ni][nj] != 0) continue;
			vis[ni][nj] = true;
			queue[front++] = ni * M + nj;
		}
	}

	return front;
}

int main()
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			scanf("%d", &maps[i][j]);
			if (maps[i][j] == 0)
			{
				candi[candi_cnt++] = i * M + j;
			}
			else if (maps[i][j] == 2)
			{
				vir[vir_cnt++] = i * M + j;
			}
			else
			{
				++wall_cnt;
			}
		}
	}
	
	int ans = 0;
	for (int i = 0; i < candi_cnt - 2; ++i)
	{
		int i1 = candi[i] / M, j1 = candi[i] % M;
		maps[i1][j1] = 1;
		for (int j = i + 1; j < candi_cnt - 1; ++j)
		{
			int i2 = candi[j] / M, j2 = candi[j] % M;
			maps[i2][j2] = 1;
			for (int k = j + 1; k < candi_cnt; ++k)
			{
				int i3 = candi[k] / M, j3 = candi[k] % M;
				maps[i3][j3] = 1;

				int temp_ans = N * M - wall_cnt - test();
				ans = ans < temp_ans ? temp_ans : ans;

				maps[i3][j3] = 0;
			}
			maps[i2][j2] = 0;
		}
		maps[i1][j1] = 0;
	}

	printf("%d\n", ans);
}
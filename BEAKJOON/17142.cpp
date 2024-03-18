// 17142. 연구소 3 2024-03-19


#define _CRT_SECURE_NO_WARNINGS
#define min(X,Y) (((X)<(Y))?(X):(Y))

#include <stdio.h>

int d_list[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int N, V;
int vir_cnt;
int vir_candi[10];
bool vir_selected[10];
int maps[50][50];
int vis[50][50];
int queue[2500];
int wall_cnt;
int ans = -1;


void test_maps()
{
	int front = 0, rear = 0;
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			vis[i][j] = -1;
		}
	}

	for (int vir_idx = 0; vir_idx < vir_cnt; ++vir_idx)
	{
		if (vir_selected[vir_idx])
		{
			queue[front++] = vir_candi[vir_idx];
			vis[vir_candi[vir_idx] / N][vir_candi[vir_idx] % N] = 0;
		}
	}

	int cnt = vir_cnt;
	int max_day = 0;
	int idx, i, j, ni, nj;
	while (rear < front)
	{
		if (N * N - wall_cnt - cnt == 0) break;
		idx = queue[rear++];
		i = idx / N, j = idx % N;
		for (int d = 0; d < 4; ++d)
		{
			ni = i + d_list[d][0], nj = j + d_list[d][1];
			if (ni < 0 || N <= ni || nj < 0 || N <= nj) continue;
			if (vis[ni][nj] != -1 || maps[ni][nj] == 1) continue;
			
			queue[front++] = ni * N + nj;
			if (maps[ni][nj] != 2) ++cnt;
			vis[ni][nj] = vis[i][j] + 1;
			if (maps[ni][nj] != 2 && max_day < vis[ni][nj])
			{
				max_day = vis[ni][nj];
			}
		}
	}

	if (N * N - wall_cnt - cnt == 0)
	{
		if (ans == -1) ans = max_day;
		else
		{
			ans = min(ans, max_day);
		}
	}
}

void dfs(int vir_idx, int step, int end)
{
	if (step == end)
	{
		test_maps();
	}
	else
	{
		if (end - step < vir_cnt - vir_idx)
		{
			dfs(vir_idx + 1, step, end);
		}
		vir_selected[vir_idx] = true;
		dfs(vir_idx + 1, step + 1, end);
		vir_selected[vir_idx] = false;
	}
}

int main()
{
	scanf("%d %d", &N, &V);
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &maps[i][j]);

			if (maps[i][j] == 2)
			{
				vir_candi[vir_cnt++] = i * N + j;
			}
			else if (maps[i][j] == 1)
			{
				++wall_cnt;
			}
		}
	}

	dfs(0, 0, V);

	printf("%d\n", ans);
}
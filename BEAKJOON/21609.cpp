// 21609. G2 상어 중학교  2024-03-23


#define _CRT_SECURE_NO_WARNINGS
#define MAX 401

#include <stdio.h>


typedef struct pos
{
	short i;
	short j;
} POS;
POS queue[400];
short front, rear;

short d_list[][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
short N, M;

short maps[20][20];
short maps_temp[20][20];

int group_size[400];
short vis[20][20];
int ans;

void gravity()
{	
	for (int j = 0; j < N; ++j)
	{
		for (int i = N - 1; 0 <= i; --i)
		{
			if (0 <= maps[i][j])
			{
				int temp_i = i;
				while (temp_i + 1 < N && maps[temp_i + 1][j] == -2)
					++temp_i;
				if (temp_i != i)
				{
					maps[temp_i][j] = maps[i][j];
					maps[i][j] = -2;
				}
			}
		}
	}
}

void rotate()
{
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			maps_temp[N - 1 - j][i] = maps[i][j];

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			maps[i][j] = maps_temp[i][j];
}

int main()
{
	scanf("%hd %hd", &N, &M);
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &maps[i][j]);
		}
	}

	while (true)
	{
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				vis[i][j] = 0;
		for (int i = 0, size = N * N; i < size; ++i) group_size[i] = 0;
		
		for (short i = 0; i < N; ++i)
		{
			for (short j = 0; j < N; ++j)
			{
				if (maps[i][j] <= 0 || maps[i][j] == vis[i][j]) continue;

				short group_num = maps[i][j];
				front = 0, rear = 0;
				vis[i][j] = group_num;
				queue[front++] = { i, j };
				int cnt = 1;
				while (rear < front)
				{
					POS temp = queue[rear++];
					for (int d = 0; d < 4; ++d)
					{
						short ni = temp.i + d_list[d][0], nj = temp.j + d_list[d][1];
						if (ni < 0 || N <= ni || nj < 0 || N <= nj) continue;
						if (vis[ni][nj] == group_num || (maps[ni][nj] != group_num && maps[ni][nj] != 0)) continue;
						vis[ni][nj] = group_num;
						queue[front++] = { ni, nj };
						if (maps[ni][nj] == 0) cnt += MAX;
						++cnt;
					}
				}
				if (1 < cnt) group_size[i * N + j] = cnt;
			}
		}

		int max_size = 0;
		short max_group = 0;
		for (int i = 0, size = N * N; i < size; ++i)
		{
			if (max_size < group_size[i] % MAX)
			{
				max_size = group_size[i] % MAX;
				max_group = i;
			}
			else if (max_size == group_size[i] % MAX)
			{
				if (group_size[max_group] <= group_size[i])
				{
					max_size = group_size[i] % MAX;
					max_group = i;
				}
			}
		}
		if (max_size == 0) break;
		ans += max_size * max_size;

		front = 0, rear = 0;
		short i = max_group / N, j = max_group % N;
		queue[front++] = { i, j };
		short group_num = maps[i][j];
		maps[i][j] = -2;
		while (rear < front)
		{
			POS temp = queue[rear++];
			for (int d = 0; d < 4; ++d)
			{
				short ni = temp.i + d_list[d][0], nj = temp.j + d_list[d][1];
				if (ni < 0 || N <= ni || nj < 0 || N <= nj) continue;
				if (maps[ni][nj] != 0 && maps[ni][nj] != group_num) continue;
				maps[ni][nj] = -2;
				queue[front++] = { ni, nj };
			}
		}
		
		gravity();
		rotate();
		gravity();
	}

	printf("%d\n", ans);
}
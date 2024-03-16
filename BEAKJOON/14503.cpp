// 14503 G5 ·Îº¿ Ã»¼Ò±â  2024-03-17


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

short N, M;
short si, sj, sd;
short maps[50][50];
short vis[50][50];
short di_list[4] = { -1, 0, 1, 0 };
short dj_list[4] = { 0, 1, 0, -1 };

int main()
{
	scanf("%hd %hd", &N, &M);
	scanf("%hd %hd %hd", &si, &sj, &sd);
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			scanf("%hd", &maps[i][j]);
		}
	}

	int ans = 0;
	while (true)
	{
		if (!vis[si][sj])
		{
			++ans;
			vis[si][sj] = true;
		}

		bool flag = false;
		for (int d = 0; d < 4; ++d)
		{
			int ni = si + di_list[d], nj = sj + dj_list[d];
			if (maps[ni][nj] == 0 && !vis[ni][nj])
			{
				flag = true;
				break;
			}
		}

		if (!flag)
		{
			int ni = si - di_list[sd], nj = sj - dj_list[sd];
			if (maps[ni][nj] == 1) break;
			si = ni;
			sj = nj;
		}
		else
		{
			sd = (sd + 3) % 4;
			int ni = si + di_list[sd], nj = sj + dj_list[sd];
			if (maps[ni][nj] == 0 && !vis[ni][nj])
			{
				si = ni;
				sj = nj;
			}
		}
	}

	printf("%d\n", ans);
}
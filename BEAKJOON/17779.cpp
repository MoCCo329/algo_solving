// 17779. 게리맨더링 2  2024-03-21


#define _CRT_SECURE_NO_WARNINGS
#define max(X,Y) (((X)<(Y))?(Y):(X))
#define min(X,Y) (((X)<(Y))?(X):(Y))

#include <stdio.h>

short N, ans;
short maps[21][21];

short test(short x, short y, short d1, short d2)
{
	short area[5] = { 0, };
	short min_c, max_c;

	for (int r = 1; r <= N; ++r)
	{
		if (r <= x + d1) min_c = y - (r - x);
		else min_c = y - d1 + (r - x - d1);
		if (r <= x + d2) max_c = y + (r - x);
		else max_c = y + d2 - (r - x - d2);

		for (int c = 1; c <= N; ++c)
		{
			if (x <= r && r <= x + d1 + d2 && min_c <= c && c <= max_c) area[4] += maps[r][c];
			else if (1 <= r && r < x + d1 && 1 <= c && c <= y) area[0] += maps[r][c];
			else if (1 <= r && r <= x + d2 && y < c && c <= N) area[1] += maps[r][c];
			else if (x + d1 <= r && r <= N && 1 <= c && c < y - d1 + d2) area[2] += maps[r][c];
			else if (x + d2 < r && r <= N && y - d1 + d2 <= c && c <= N) area[3] += maps[r][c];
		}
	}

	short min_v = 1 << 13;
	short max_v = 0;
	for (int i = 0; i < 5; ++i)
	{
		min_v = min(min_v, area[i]);
		max_v = max(max_v, area[i]);
	}

	return max_v - min_v;
}

int main()
{
	scanf("%hd", &N);
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			scanf("%hd", &maps[i][j]);
		}
	}

	ans = 1 << 13;

	for (int x = 1; x <= N; ++x)
	{
		for (int y = 1; y <= N; ++y)
		{
			for (int d1 = 1; d1 <= N; ++d1)
			{
				for (int d2 = 1; d2 <= N; ++d2)
				{
					if (!(x + d1 + d2 <= N) || !(1 <= y - d1) || !(y + d2 <= N)) continue;
					short temp_ans = test(x, y, d1, d2);
					ans = min(ans, temp_ans);
				}
			}
		}
	}

	printf("%d\n", ans);
}
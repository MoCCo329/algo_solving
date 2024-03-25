// 1253. G4 좋다  2024-03-26


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int N;
int arr[2000];

bool check(int idx)
{
	int l = 0, r = N - 1;
	while (l < r)
	{
		if (arr[l] + arr[r] == arr[idx])
		{
			if (l == idx) ++l;
			else if (r == idx) --r;
			else return true;
		}
		else if (arr[l] + arr[r] < arr[idx]) ++l;
		else --r;
	}
	return false;
}

int main()
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < N - 1; ++i)
	{
		int temp_i = i;
		for (int j = i + 1; j < N; ++j)
		{
			if (arr[j] < arr[temp_i])
			{
				temp_i = j;
			}
		}
		int temp = arr[i];
		arr[i] = arr[temp_i];
		arr[temp_i] = temp;
	}

	int ans = 0;
	for (int i = 0; i < N; ++i)
	{
		if (check(i)) ++ans;
	}

	printf("%d\n", ans);
}
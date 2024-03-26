// 2212. G5 센서  2024-03-27


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int N, K;
int arr[10000];
int gap_arr[10000];

void quick_sort(int* arr, int s, int e)
{
	int p;
	int i, j;
	int temp;

	if (s < e)
	{
		p = s;
		i = s;
		j = e;

		while (i < j)
		{
			while (arr[i] <= arr[p] && i < e) ++i;
			while (arr[p] < arr[j]) --j;
			if (i < j)
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}

		temp = arr[p];
		arr[p] = arr[j];
		arr[j] = temp;

		quick_sort(arr, 0, j - 1);
		quick_sort(arr, j + 1, e);
	}
}

int main()
{
	scanf("%d", &N);
	scanf("%d", &K);
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &arr[i]);
	}

	if (N <= K)
	{
		printf("0\n");
		return 0;
	}

	quick_sort(arr, 0, N - 1);

	for (int i = 0; i < N - 1; ++i)
	{
		gap_arr[i] = arr[i + 1] - arr[i];
	}

	quick_sort(gap_arr, 0, N - 2);

	int ans = 0;
	for (int i = 0; i < N - 1 - (K - 1); ++i)
	{
		ans += gap_arr[i];
	}

	printf("%d\n", ans);
}
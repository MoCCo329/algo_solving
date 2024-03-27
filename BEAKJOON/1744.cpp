// 1744. G4 수 묶기  2024-03-28


#define _CRT_SECURE_NO_WARNINGS
#define ABS(x) ((0<x)?(x):(-x))

#include <stdio.h>

int N;
int arr[50];
int rev_arr[50];
int arr_size, rev_arr_size;
int ans, i;
bool zero;

void sort(int* arr, int s, int e)
{
	if (e <= s) return;

	int i = s, j = e, pivot = s, temp;

	while (i < j)
	{
		while (ABS(arr[pivot]) <= ABS(arr[i]) && i < e) ++i;
		while (ABS(arr[j]) < ABS(arr[pivot])) --j;
		if (i < j)
		{
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}

	temp = arr[pivot];
	arr[pivot] = arr[j];
	arr[j] = temp;

	sort(arr, s, j - 1);
	sort(arr, j + 1, e);
}

int main()
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		int temp;
		scanf("%d", &temp);
		if (temp == 0) zero = true;
		else if (temp == 1) ++ans;
		else if (temp < 0) rev_arr[rev_arr_size++] = temp;
		else arr[arr_size++] = temp;
	}

	sort(arr, 0, arr_size - 1);
	sort(rev_arr, 0, rev_arr_size - 1);

	i = 0;
	while (i < rev_arr_size)
	{
		if (i + 1 < rev_arr_size) ans += rev_arr[i] * rev_arr[i + 1], i += 2;
		else if (zero) ++i;
		else ans += rev_arr[i], ++i;
	}

	i = 0;
	while (i < arr_size)
	{
		if (i + 1 < arr_size) ans += arr[i] * arr[i + 1], i += 2;
		else ans += arr[i], ++i;
	}

	printf("%d\n", ans);
}
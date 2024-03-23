// 1655. G2 가운데를 말해요  2024-03-24


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int small_heap_size;
int big_heap_size;
short small_heap[50001];
short big_heap[50001];

int N;
short mid, v;

bool big_heap_pop(short *value)
{
	if (big_heap_size == 0) return false;

	*value = big_heap[0];
	big_heap[0] = big_heap[--big_heap_size];

	int cur = 0;
	while (cur * 2 + 1 < big_heap_size)
	{
		int c;
		if (cur * 2 + 2 == big_heap_size)
		{
			c = cur * 2 + 1;
		}
		else
		{
			c = big_heap[cur * 2 + 1] < big_heap[cur * 2 + 2] ? cur * 2 + 1 : cur * 2 + 2;
		}

		if (big_heap[cur] < big_heap[c]) break;
		short temp = big_heap[cur];
		big_heap[cur] = big_heap[c];
		big_heap[c] = temp;
		cur = c;
	}

	return true;
}

bool small_heap_pop(short* value)
{
	if (small_heap_size == 0) return false;

	*value = small_heap[0];
	small_heap[0] = small_heap[--small_heap_size];

	int cur = 0;
	while (cur * 2 + 1 < small_heap_size)
	{
		int c;
		if (cur * 2 + 2 == small_heap_size)
		{
			c = cur * 2 + 1;
		}
		else
		{
			c = small_heap[cur * 2 + 1] < small_heap[cur * 2 + 2] ? cur * 2 + 2 : cur * 2 + 1;
		}

		if (small_heap[c] < small_heap[cur]) break;
		short temp = small_heap[cur];
		small_heap[cur] = small_heap[c];
		small_heap[c] = temp;
		cur = c;
	}

	return true;
}

void big_heap_push(short value)
{
	big_heap[big_heap_size] = value;

	int cur = big_heap_size;
	while (0 < cur && big_heap[cur] < big_heap[(cur - 1) / 2])
	{
		short temp = big_heap[(cur - 1) / 2];
		big_heap[(cur - 1) / 2] = big_heap[cur];
		big_heap[cur] = temp;
		cur = (cur - 1) / 2;
	}

	++big_heap_size;
}

void small_heap_push(short value)
{
	small_heap[small_heap_size] = value;

	int cur = small_heap_size;
	while (0 < cur && small_heap[(cur - 1) / 2] < small_heap[cur])
	{
		short temp = small_heap[(cur - 1) / 2];
		small_heap[(cur - 1) / 2] = small_heap[cur];
		small_heap[cur] = temp;
		cur = (cur - 1) / 2;
	}

	++small_heap_size;
}

int main()
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf("%hd", &v);
		if (big_heap_size < small_heap_size) big_heap_push(v);
		else small_heap_push(v);

		if (0 < small_heap_size && 0 < big_heap_size)
		{
			if (big_heap[0] < small_heap[0])
			{
				short temp;
				small_heap_pop(&temp);
				big_heap_push(temp);
				big_heap_pop(&temp);
				small_heap_push(temp);
			}
		}

		printf("%hd\n", small_heap[0]);
	}
}
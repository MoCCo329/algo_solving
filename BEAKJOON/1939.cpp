// 1939. G3 중량제한  2024-03-23


#define _CRT_SECURE_NO_WARNINGS
#define MIN(X,Y) (((X)<(Y))?(X):(Y))

#include <stdio.h>

typedef struct road
{
	int to;
	int payload;
	struct road* NEXT;
} ROAD;
ROAD* adj_list[10001];
ROAD roads[200000];
int road_idx;

typedef struct head_node
{
	int i;
	int payload;
} HEAP_NODE;

int N, M;
int a, b, c;
int start, end;
HEAP_NODE heap[100000];
int heap_size;
int dist[10001];

void heap_push(int i, int v)
{
	heap[heap_size] = { i, v };
	int cur = heap_size;
	while (0 < cur && heap[(cur - 1) / 2].payload < heap[cur].payload)
	{
		HEAP_NODE temp = heap[(cur - 1) / 2];
		heap[(cur - 1) / 2] = heap[cur];
		heap[cur] = temp;
		cur = (cur - 1) / 2;
	}

	++heap_size;
}

HEAP_NODE heap_pop()
{
	if (heap_size <= 0) return { -1, -1 };

	HEAP_NODE ans = heap[0];
	heap[0] = heap[--heap_size];
	int cur = 0;
	while (cur * 2 + 1 < heap_size)
	{
		int c;
		if (cur * 2 + 2 == heap_size)
		{
			c = cur * 2 + 1;
		}
		else
		{
			c = heap[cur * 2 + 2].payload < heap[cur * 2 + 1].payload ? cur * 2 + 1 : cur * 2 + 2;
		}

		if (heap[c].payload < heap[cur].payload) break;

		HEAP_NODE temp = heap[cur];
		heap[cur] = heap[c];
		heap[c] = temp;
		cur = c;
	}

	return ans;
}

int main()
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; ++i)
	{
		scanf("%d %d %d", &a, &b, &c);
		roads[road_idx] = { b, c, adj_list[a] };
		adj_list[a] = &roads[road_idx++];
		roads[road_idx] = { a, c, adj_list[b] };
		adj_list[b] = &roads[road_idx++];
	}
	scanf("%d %d", &start, &end);

	dist[start] = 1000000000;
	heap_push(start, 1000000000);
	while (true)
	{
		HEAP_NODE heap_node = heap_pop();
		if (heap_node.i == -1 || heap_node.i == end) break;
		if (heap_node.payload < dist[heap_node.i]) continue;
		ROAD* node = adj_list[heap_node.i];
		while (node)
		{
			int new_dist = MIN(heap_node.payload, node->payload);
			if (dist[node->to] != 0 && new_dist <= dist[node->to])
			{
				node = node->NEXT;
				continue;
			}
			dist[node->to] = new_dist;
			heap_push(node->to, new_dist);
			node = node->NEXT;
		}
	}

	printf("%d\n", dist[end]);
}
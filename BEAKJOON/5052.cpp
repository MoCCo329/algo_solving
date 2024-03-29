// 5052 G4 전화번호 목록  2024-03-30


#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
	bool is_occ = false;
	node* c[10] = { NULL, };
} NODE;

int T, N;
NODE* root;
char num[11];
bool flag;

bool insert()
{
	NODE* now = root;
	for (int i = 0; i < 11; ++i)
	{
		if (num[i] == '\0') break;

		int idx = num[i] - '0';

		if (now->c[idx] == NULL)
		{
			now->c[idx] = (NODE*)malloc(sizeof(NODE));
			memset(now->c[idx], 0, sizeof(NODE));
		}
		else if (num[i + 1] == '\0') return false;
		now = now->c[idx];

		if (now->is_occ) return false;
	}
	now->is_occ = true;

	return true;
}

int main()
{
	scanf("%d", &T);
	while (T-- != 0)
	{
		root = (NODE*)malloc(sizeof(NODE));
		memset(root, 0, sizeof(NODE));
		flag = false;

		scanf("%d", &N);
		while (N-- != 0)
		{
			scanf("%s", &num);
			if (flag) continue;

			if (!insert())
			{
				flag = true;
			}
		}
		if (!flag) printf("YES\n");
		else printf("NO\n");

		free(root);
	}
}
#include <stdio.h>

int main()
{
	int N; // 무게 입력
	int min = -1; // 봉지 최소갯수

	scanf("%d", &N);

	for (int i = 0; i <= 1000; i++)
	{
		for (int j = 0; j < 1667; j++)
		{
			if (i * 5 + j * 3 == N)
			{
				min = i + j;
			}
		}
	}
	printf("%d", min);
}
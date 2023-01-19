# 15824. 너 봄에는 캡사이신이 맛있단다  2023-01-19


def power(x, n):
    if n <= 1: return x ** n
    temp = power(x, n // 2)
    if n % 2 == 1:
        return temp * temp * x % 1000000007
    else:
        return temp * temp % 1000000007


N = int(input())
foods = list(map(int, input().split()))
foods.sort()

ans = 0
for i in range(N):
    ans = (ans + (power(2, i) - power(2, N - i - 1)) * foods[i]) % 1000000007
    # ans = (ans + (pow(2, i, 1000000007) - pow(2, N - i - 1, 1000000007)) * foods[i]) % 1000000007

print(ans)
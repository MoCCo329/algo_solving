# 1111. IQ Test  2023-04-02


N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    temp1 = arr[1] - arr[0]
    temp2 = arr[2] - arr[1]

    if temp1 == 0 or temp2 == 0:
        a = 0
    else:
        a = temp2 // temp1
    b = arr[1] - arr[0] * a

    for i in range(2, N):
        temp = arr[i - 1] * a + b
        if arr[i] != temp:
            print("B")
            exit(0)
    else:
        print(arr[-1] * a + b)
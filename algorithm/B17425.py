T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0

    for i in range (1, n+1):
        cnt += (n//i)*i

    print(cnt)    
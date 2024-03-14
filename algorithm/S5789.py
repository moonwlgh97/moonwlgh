T = int(input())

for tc in range(1, T+1):
    n, q = map(int,input().split())

    li=[0]*n

    for i in range(1,q+1):
        l, r = map(int,input().split())
        for j in range(l-1,r):
            li[j]= i

    print(f'#{tc}',*li)






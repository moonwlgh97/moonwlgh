
T = int(input())

for tc in range(1,T+1):
    n,m = map(int, input().split())
    li=[]
    max =0

    for _ in range(n):
        li.append(list(map(int,input().split())))


    for i in range(0,n-m+1):
        for j in range(0, n-m+1):
            sum=0
            for k in range(i,i+m):
                for z in range(j,j+m):
                    sum += li[k][z]

            if sum >= max:
                max =sum


    print(f'#{tc}', max)
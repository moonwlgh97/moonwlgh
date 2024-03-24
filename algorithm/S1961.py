T = int(input())

for tc in range(1, T+1):

    n = int(input())

    li =[list(map(int,input().split())) for _ in range(n)]

    li_90 = [[0]*n for _ in range(n)]
    li_180 = [[0] * n for _ in range(n)]
    li_270 = [[0] * n for _ in range(n)]

    # 90
    for i in range(n):
        for j in range(n):

            li_90[i][j] = li[n-1-j][i]


    # 180

    for i in range(n):
        for j in range(n):
            li_180[i][j] = li_90[n-j-1][i]


    #270

    for i in range(n):
        for j in range(n):
            li_270[i][j] =  li_180[n-j-1][i]



    print(f'#{tc}')

    for i in range(n):
        for a in range(n):
            print(li_90[i][a], end='')
        print(end=' ')

        for b in range(n):
            print(li_180[i][b], end='')
        print(end=' ')

        for c in range(n):
            print(li_270[i][c], end='')

        print()












        

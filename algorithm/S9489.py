T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]

    cnt = []



    # 가로
    for i in range(n):
        row = 0
        for j in range(m):

            if li[i][j] == 1:
                row += 1
            else:
                row = 0
            cnt.append(row)


    # 세로

    for j in range(m):
        col = 0
        for i in range(n):

            if li[i][j] == 1:
                col += 1

            else:
                col = 0
            cnt.append(col)

    print(f'#{tc}', max(cnt))

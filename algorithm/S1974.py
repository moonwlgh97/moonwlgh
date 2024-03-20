T = int(input())

for tc in range(1, T+1):
    li = [list(map(int,input().split())) for _ in range(9)]
    ans =0
    ans_check=[0]*3

    #3x3
    for i in range(0,9,3):
        visited = [0]*9
        for j in range(0,9,3):

            for k in range(i, i+3):
                for z in range(j,j+3):
                    visited[li[k][z]-1] =1

            if 0 in visited:
                break
            else:
                ans_check[0]+=1

    #가로

    for i in range(9):
        row = [0]*9
        for j in range(9):
            row[li[i][j]-1]=1

        if 0 in row:
            break
        else:
            ans_check[1]+=1


    # 세로

    for i in range(9):
        col = [0]*9
        for j in range(9):
            col[li[j][i]-1] =1

        if 0 in col:
            break
        else:
            ans_check[2]+=1


    for i in range(3):
        if ans_check[i] == 9:
            ans+=1

    if ans ==3:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)








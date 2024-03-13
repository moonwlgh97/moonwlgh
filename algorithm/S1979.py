T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    li = []
    cnt = 0
    for _ in range(n):
        li.append(list(map(int, input().split())))
    for i in range(1,4):
        for j in range(1,4):
            if li[i][j] ==1 and li[i][j-1] ==1 and li[i][j+1] ==1 and sum(li[i])==3:
                cnt +=1

            if li[j][i] ==1 and li[j-1][i] ==1  and li[j+1][i] ==1 and






def check(li) :
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if li[i][j] == li[i][j+1]:
                cnt +=1
            else:
                cnt =1

            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(n-1):

            if li[j][i] == li[j+1][i]:
                cnt +=1
            else:
                cnt =1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

n = int(input())
li = [list(input()) for _ in range(n)]
ans = 0

for i in range (n):
    for j in range(n):

        if j+1 < n:
            li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
            cnt = check(li)
            ans = max(ans, cnt)
            li[i][j], li[i][j + 1] = li[i][j + 1], li[i][j]


        if i +1 < n :
            li[i][j], li[i+1][j] = li[i+1][j], li[i][j]
            cnt = check(li)
            ans = max(ans,cnt)

            li[i][j], li[i + 1][j] = li[i + 1][j], li[i][j]

print(ans)

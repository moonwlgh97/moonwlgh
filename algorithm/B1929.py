n, m = map(int,input().split())

li = [True for i in range(m+1)]

for i in range(n,m):
    j =2
    while (i*j <= m):
        if li[i*j] == True:
            li[i*j] = False
        else:
            continue
        j+=1

for i in range(n,m+1):
    if li[i]:
        print(i)

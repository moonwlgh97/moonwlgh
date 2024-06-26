n,m = map(int, input().split())
li =[]
for _ in range(n):
    li.append(list(map(int,input().split())))

ans =0

def shape1(i,j):
    if j+3 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i][j+2] + li[i][j+3]

def shape2(i,j):
    if i+3 >= n:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i+3][j]

def shape3(i,j):
    if i+1 >= n or j+1 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i+1][j] + li[i+1][j+1]

def shape4(i,j):
    if i-1 < 0 or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i-1][j+1] + li[i][j+2]

def shape5(i,j):
    if i+2 >= n or j+1 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i+1][j+1]

def shape6(i,j):
    if i+1 >= n or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i][j+2] + li[i+1][j+1]

def shape7(i,j):
    if i+2 >= n or j-1 <0:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i+1][j-1]

def shape8(i,j):
    if i+2 >= n or j+1 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i+2][j+1]

def shape9(i,j):
    if i+1 >= n or j+2 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i][j+1] + li[i][j+2]

def shape10(i,j):
    if i+2>= n or j+1 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i+1][j+1] + li[i+2][j+1]

def shape11(i,j):
    if i-1 < 0 or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i][j+2] + li[i-1][j+2]

def shape12(i,j):
    if i+2 >= n or j-1 <0:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i+2][j-1]

def shape13(i,j):
    if i+1 >= n or j+2 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i+1][j+1] + li[i+1][j+2]

def shape14(i,j):
    if i+2 >= n or j+1 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i+2][j] + li[i][j+1]

def shape15(i,j):
    if i+1 >= n or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i][j+2] + li[i+1][j+2]

def shape16(i,j):
    if i+2 >= n or j+1 >= m:
        return 0
    return li[i][j] + li[i+1][j] + li[i+1][j+1] + li[i+2][j+1]

def shape17(i,j):
    if i-1 < 0 or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i-1][j+1] + li[i-1][j+2]

def shape18(i,j):
    if i+2 >= n or j -1 <0:
        return 0
    return li[i][j] + li[i+1][j] + li[i+1][j-1] + li[i+2][j-1]

def shape19(i,j):
    if i+1 >= n or j+2 >= m:
        return 0
    return li[i][j] + li[i][j+1] + li[i+1][j+1] + li[i+1][j+2]


for i in range(n):
    for j in range(m):
        ans = max(ans, shape1(i,j),shape2(i,j),shape3(i,j),shape4(i,j),shape5(i,j),shape6(i,j),shape7(i,j),shape8(i,j),shape9(i,j),shape10(i,j)
                  ,shape11(i,j),shape12(i,j),shape13(i,j),shape14(i,j),shape15(i,j),shape16(i,j),shape17(i,j),shape18(i,j),shape19(i,j))

print(ans)
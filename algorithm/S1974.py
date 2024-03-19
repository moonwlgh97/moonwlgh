T = int(input())

for tc in range(1, T+1):
    li = [list(map(int,input().split())) for _ in range(9)]
    ans =0

    for i in range(0,9,3):
        visited = [0]*10
        for j in range(0,9,3):

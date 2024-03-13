T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    li = []
    cnt = 0
    for _ in range(n):
        li.append(list(map(int, input().split())))
    for i in range(n):
        sum = 0

        # 가로
        for j in range(n):

            if li[i][j] == 1:
                sum+=1

            if li[i][j] ==0 or j==n-1:
                if sum ==k:
                    cnt +=1
                sum=0

        # 세로

        for j in range(n):

            if li[j][i] ==1:
                sum +=1

            if  li[j][i] ==0 or j==n-1:

                if sum == k:
                    cnt +=1
                sum = 0

    # 1. 가로 세로 따로 따로 생각한다
    # 2. 1인 경우와 0 or 인덱스가 4일 때 생각을 함
    # 3. 우선 1일땐 카운트를 해줘서 저장
    # 4. 0이거나 마지막 인덱스인 경우 sum이 k와 같은지 비교후 cnt를 카운트 그리고 이 구문으로 들어오면 무조건 sum을 0으로 초기화 시켜준다.



    print(f'#{tc}', cnt)




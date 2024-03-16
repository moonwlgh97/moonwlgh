T = int(input())

for tc in range(1,T+1):
    n = int(input())
    stop = [0]*5001

    for _ in range(n):
        a, b = map(int,input().split())

        for i in range(a, b+1):
            stop[i] +=1

    p = int(input())

    print(f'#{tc}', end=' ')
    for _ in range(p):
        c = int(input())
        print(stop[c], end=' ')
    print()


    # 버스 정류장 stop을 만든다
    # a,b 를 n 만큼 받으며 해당 정류소에 +=1 해준다
    # 해당 정류소 번호를  stop[c] 와 print(, end=' ') 를 이용해 받아준다.



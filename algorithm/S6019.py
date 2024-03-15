T = int(input())

for tc in range(1,T+1):
    d, a, b, f = map(int,input().split())

    t = d/(a+b)


    print(f'#{tc}', t*f)

    # 제논의 역설, 무한급수 참고
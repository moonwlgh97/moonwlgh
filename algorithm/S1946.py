T = int(input())


for tc in range(1,T+1):
    n = int(input())
    all=''

    for _ in range(n):
        alpha, num = map(str,input().split())
        all+= alpha*int(num)

    print(f'#{tc}')
    for i in range(0,len(all),10):
        print(all[i:i+10])










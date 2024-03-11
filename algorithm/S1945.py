T = int(input())

for tc in range(1,T+1):
    n = int(input())
    ans = [0]*5

    while n != 1:
        if n % 2 ==0:
            ans[0]+=1
        elif n % 3 ==0:
            ans[1] +=1
        elif n % 5 ==0:
            ans[2] +=1

        elif n % 7 ==0:
            ans[3] +=1

        elif n% 11==0:
            ans[4] +=1


    print(f'#{tc} {ans}')                    





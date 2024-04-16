while(1):
    try:
        n = int(input())
    except:
        break

    cnt = 1
    num = 0

    while(1):
        num = num *10+1

        if num % n == 0:
            print(cnt)
            break
        else:
            cnt +=1


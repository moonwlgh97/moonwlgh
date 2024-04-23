li = [i for i in range(1, 1000001,2)]
sosu = []
for i in li:
    if i ==1:
        continue
    else:
        for j in range(2, int(max(li)**0.5)+1):
            if i % j == 0:
                break
        else:
            sosu.append(i)


while(1):
    n = int(input())

    if n ==0 :
        break

    n_li =[]
    a=0
    b=0

    for i in sosu:

        if i <= n:
            n_li.append(i)
        else:
            break

    for i in range(0, len(n_li)+1):
        for j in range(len(n_li), i-1, -1):
            if n_li[i]+n_li[j] == n:
                a = n_li[i]
                b = n_li[j]
                break
    else:
        print("Goldbach's conjecture is wrong.")


    print(f'{n} = {a} + {b}')




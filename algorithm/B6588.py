import sys

sosu = [True]*1000001
m= int(1000001 **0.5)

for i in range(2,m+1):
    if sosu[i]:
        for j in range(i+i, 1000001, i):
            sosu[j] = False


while(1):
    n = int(sys.stdin.readline())

    if n ==0:
        break
    else:

        for i in range(2, m+1):
            if sosu[i] and sosu[n-i]:
                print(f'{n} = {i} + {n-i}')
                break


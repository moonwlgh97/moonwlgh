import sys

g = [0] * 1000001
f = [0] * 1000001

for i in range(1,1000001):
    j =1
    while(i*j <= 1000000):
        f[i*j] += i
        j +=1
    g[i] = g[i-1]+ f[i]



T = int(input())

for _ in range(T):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(g[a]) + "\n")
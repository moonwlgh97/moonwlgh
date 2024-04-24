li=[]

while(1):
    try:
        n = int(input())
        li.append(n)
    except:
        break

target_li = sorted(li)
target = sum(li) - 100

for i in range(len(target_li)):
    for j in range(i+1, len(target_li)):
        if target_li[i] + target_li[j] == target:
            a = target_li[i]
            b = target_li[j]
            break


for i in target_li:
    if i == a or i ==b :
        continue
    else:
        print(i)



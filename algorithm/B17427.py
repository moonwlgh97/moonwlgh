n = int(input())


# 시간초과
# def getValue(num):
#     value = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             value += i
#
#         else:
#             continue
#
#     return value
#
#
# cnt = 0
#
# for i in range(1, n+1):
#     cnt += getValue(i)
#
# print(cnt)

cnt = 0

for i in range(1, n+1):

    cnt += (n//i) *i

print(cnt)




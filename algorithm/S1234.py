


for tc in range( 1, 11):

    n, num = input().split()
    x = list(num)
    stack =[]

    for i in x:

     if len(stack) == 0:
         stack.append(i)


     else:
         if stack[-1] == i:
             stack.pop()

         else:
             stack.append(i)

    print(f'#{tc}' ,' ',end='')
    for i in range(len(stack)):
        print(stack[i],end='')
    print()

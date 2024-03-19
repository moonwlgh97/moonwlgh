T = int(input())


for tc in range(1,T+1):
    words = input()
    reverse_words = words[::-1]

    ans = 0

    if words == reverse_words:
        ans =1


    print(f'#{tc}', ans)


E, S, M = map(int, input().split())

cnt = 1
e, s, m = 1, 1, 1  # 초기값 설정

while True:
    if e == E and s == S and m == M:
        break

    e += 1
    s += 1
    m += 1
    cnt += 1

    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(cnt)

a, b, c = map(int, input().split())

ans = 0
start = a

while True:
    if c % start == 0:
        ans += 1
    start += 1
    if start > b:
        break

print(ans)

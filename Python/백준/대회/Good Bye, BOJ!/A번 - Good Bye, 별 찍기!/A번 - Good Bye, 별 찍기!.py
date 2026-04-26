import sys

n = int(sys.stdin.readline().rstrip())

k = n * 2 - 1

for i in range(n * 2):
    print(' ' * k + '*', end="")
    k -= 1
    if i < n:
        print(' ' * n, end="")
    else:
        print(' ' * (n + ((i - n) * 2) + 1), end="")
    print('*', end="")
    if i < n:
        print(' ' * (i * 2 + 1), end="")
    else:
        print(' ' * ((n * 2 - 1 - i) * 2 + 1), end="")
    print('*')

import sys

s = sys.stdin.readline().rstrip()
set_s = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        set_s.add(s[i:j+1])

print(len(set_s))
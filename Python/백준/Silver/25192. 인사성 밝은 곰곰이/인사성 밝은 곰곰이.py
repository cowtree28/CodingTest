import sys

n = int(sys.stdin.readline().rstrip())

answer = 0
emoji = set()
for _ in range(n):
    chat = sys.stdin.readline().rstrip()
    if chat == "ENTER":
        answer += len(emoji)
        emoji = set()
        continue
    emoji.add(chat)

answer += len(emoji)
print(answer)

import sys
input = sys.stdin.readline

N = int(input())
bear_string = list(input().strip())
process_stack = []
day = 0

for c in bear_string:
    if len(process_stack) == 0 or c == process_stack[-1]:
        process_stack.append(c)
    else:
        process_stack.pop()
    day = max(day, len(process_stack))

if process_stack:
    print(-1)
else:
    print(day)

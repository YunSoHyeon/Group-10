import sys
input = sys.stdin.readline

N, K = map(int, input().split())
score = {0: 0}

for i in range(N):
    input_W, input_V = map(int, input().split())
    tmp = {}

    for w, v in score.items():
        if input_W + w <= K and input_V + v > score.get(input_W + w, 0):
            tmp[input_W + w] = input_V + v
    score.update(tmp)

print(max(score.values()))

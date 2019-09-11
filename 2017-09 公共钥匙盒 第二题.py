import pandas as pd
n, k = list(map(int, input().split()))
timeline = {}
for i in range(k):
    w, s, c = list(map(int, input().split()))
    if s not in timeline:
        timeline[s] = []
    timeline[s].append(w)
    timeline[s].sort()
    if s + c not in timeline:
        timeline[s + c] = []
    timeline[s+c].append(-(n - w))
    timeline[s+c].sort()

box = [i for i in range(1,n + 1)]

for key in sorted(timeline.keys()):
    for i in timeline[key]:
        if i <= 0:
            box[box.index(0)] = n + i
        else:
            box[box.index(i)] = 0
        print(' '.join(map(str,box)))
print(' '.join(map(str,box)))
 
# https://www.acmicpc.net/problem/2024

from sys import stdin

END = int(stdin.readline())
segments = [
    tuple(map(int, line.split()))
    for line
    in stdin.readlines()
]

segments.sort()

count = 0
checkpoint = 0
first = True
end = -1

for seg in segments:
    if seg[0] > checkpoint:
        end = checkpoint = max(end, checkpoint)
        first = True

    if seg[0] <= checkpoint and checkpoint < END:
        if first:
            first = False
            count += 1

        end = max(end, seg[1])

if end >= END:
    print(count)
else:
    print(0)

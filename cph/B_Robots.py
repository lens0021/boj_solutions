for _ in range(int(input())):
  max_h, max_w = map(int, input().split())
  robots = []
  for h in range(max_h):
    line = input()
    for w, ch in enumerate(line):
      if ch == 'R':
        # Push an element to robots
        robots.append((h, w))
  min_w = min([t[1] for t in robots])
  min_h = min([t[0] for t in robots])
  print('YES' if (min_h, min_w) in robots else 'NO')

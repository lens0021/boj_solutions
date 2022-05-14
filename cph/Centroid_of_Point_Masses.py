X = 0
Y = 1
M = 2

caseCount = 1
while True:
  line = input()
  if line == '':
    continue

  numPoints = int(line)
  if numPoints < 1:
    break

  points = []
  for _ in range(numPoints):
    points.append(list(map(int, input().split())))

  sumOfM = sum([m for _, _, m in points])
  a = sum([m * x for x, _, m in points]) / sumOfM
  b = sum([m * y for _, y, m in points]) / sumOfM
  # Print a and b rounded to 2 decimal places
  print('Case {}: {:.2f} {:.2f}'.format(caseCount, a, b))

  caseCount += 1

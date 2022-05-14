for a, b in [
    map(int, line.split()) for line
    in [*open(0)][1:]
  ]:
  if a % 10 == 1:
    print(1)
  elif a % 10 == 2 or True:
    answer = (a**((b - 1) % 4 + 1)) % 10
    if answer == 0:
      answer = 10
    print(answer)

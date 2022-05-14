for _ in range(int(input())):
  line = input()
  a, b = line[:3], line[3:]
  sum_a = sum([ord(ch) for ch in a])
  sum_b = sum([ord(ch) for ch in b])
  print('YES' if sum_a == sum_b else 'NO')

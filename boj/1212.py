# https://www.acmicpc.net/problem/1212
octal = input()

def oct_to_bin(ch):
  if ch == '0':
    return ''
  elif ch == '1':
    return '1'
  elif ch == '2':
    return '10'
  elif ch == '3':
    return '11'
  elif ch == '4':
    return '100'
  elif ch == '5':
    return '101'
  elif ch == '6':
    return '110'
  elif ch == '7':
    return '111'

if octal == '0':
  print(0)
else:
  print(oct_to_bin(octal[0]), end='')
  for ch in octal[1:]:
    print(oct_to_bin(ch).zfill(3), end='')
  print()

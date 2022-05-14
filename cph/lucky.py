import numbers
import sys
import os

for line in sys.stdin.read().splitlines()[1:]:
  num1 = sum(map(int, line[:3]))
  num2 = sum(map(int, line[3:]))
  print( 'YES' if num1 == num2 else 'NO' )

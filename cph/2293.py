# https://www.acmicpc.net/submit/2293
from sys import stdin, stdout
from typing import List

def init_partition(n: int) -> list[int]:
  # The number of making zero is always 1.
  # Others will be set from other places than here.
  return [1] + [0] * (n)

def create_parttern_map(coins: List[int], sum: int) -> List[int]:
  m = init_partition(sum)

  for coin_value in coins:
    for larger_values in range(coin_value, sum + 1):
      m[larger_values] += m[larger_values - coin_value]

  return m

def debug_print_partten_map(m: List[int]):
  for i, num in enumerate(m):
    print(f'{i}를 만드는 방법은 {num} 가지가 있습니다.')


if __name__ == '__main__':
  FINAL_SUM = int(stdin.readline().split()[1])
  coins = [int(v) for v in stdin.read().splitlines()]
  stdout.write(str(create_parttern_map(coins, FINAL_SUM)[-1]) + '\n')
  # debug_print_partten_map([1, 1, 2, 3])

def test_init_partition():
  assert init_partition(5) == [1, 0, 0, 0, 0, 0]

def test_create_parttern_map():
  assert create_parttern_map([1, 2, 3], 0) == [1]
  assert create_parttern_map([1, 2, 3], 1) == [1, 1]
  assert create_parttern_map([1, 2, 3], 2) == [1, 1, 2]
  assert create_parttern_map([1, 2, 3], 3) == [1, 1, 2, 3]
  assert create_parttern_map([1, 2, 3], 4) == [1, 1, 2, 3, 4]
  assert create_parttern_map([1, 2, 3], 5) == [1, 1, 2, 3, 4, 5]

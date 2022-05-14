# https://www.acmicpc.net/problem/1065

def helper() -> int:
  st = input()
  num = int(st)

  if num < 100:
    return num
  three_nums = [
    111,
    123,
    135,
    147,
    159,
    210,
    222,
    234,
    246,
    258,
    321,
    333,
    345,
    357,
    369,
    420,
    432,
    444,
    456,
    468,
    531,
    543,
    555,
    567,
    579,
    630,
    642,
    654,
    666,
    678,
    741,
    753,
    765,
    777,
    789,
    840,
    852,
    864,
    876,
    888,
    951,
    963,
    975,
    987,
    999,
  ]
  if num in three_nums:
    return 99 + three_nums.index(num) + 1

  three_nums.append(num)
  three_nums.sort()

  return 99 + three_nums.index(num)

print(helper())

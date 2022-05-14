for _ in range(int(input())):
  h, w = map(int, input().split())
  board = [
    list(map(int, input().split()))
    for _ in range(h)
  ]

  ct = 0
  for i in range(h):
    for j in range(w):
      ct += 1
      stretch = 1
      while (
        0 <= i - stretch < h and
        0 <= i + stretch < h and
        0 <= j - stretch < w and
        0 <= j + stretch < w
        ):
          if (board[i - stretch][j] == board[i + stretch][j] and
            board[i][j - stretch] == board[i][j + stretch]):
            ct += 1
          stretch += 1

  print(ct)

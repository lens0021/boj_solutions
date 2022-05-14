# https://www.acmicpc.net/problem/1018
from sys import stdin
from math import inf


def helper(board):
  '''Calculate minimun number of cells should be colored'''
  return 0


rows, cols = map(int, stdin.readline().split())
W, H = 8, 8
board = stdin.read().splitlines()

answer = inf
for starting_row in range(rows - H + 1):
  for starting_col in range(cols - W + 1):
    cropped_board = [col for col in board[starting_row:starting_row + H][starting_col + W]]
    answer = min(answer, helper(cropped_board))


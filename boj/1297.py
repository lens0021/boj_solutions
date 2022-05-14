# https://www.acmicpc.net/problem/1297
from math import sqrt

diagonal, w, h = map(int, input().split())
print(int((diagonal * w) // sqrt(w*w+h*h)))
print(int((diagonal * h) // sqrt(w*w+h*h)))

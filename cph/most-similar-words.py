import math

def diffOfWords(word1, word2):
  return sum(abs(ord(c1) - ord(c2)) for c1, c2 in zip(word1, word2))


for _ in range(int(input())):
  numOfWords = int(input().split()[0])
  words = [input() for _ in range(numOfWords)]
  minimum = math.inf
  for i in range(numOfWords):
    for j in range(i + 1, numOfWords):
      diff = diffOfWords(words[i], words[j])
      minimum = min(minimum, diff)
  print(minimum)






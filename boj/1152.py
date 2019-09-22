# https://www.acmicpc.net/problem/1152

msg = input().strip()
print(0 if msg == '' else msg.count(' ')+1)

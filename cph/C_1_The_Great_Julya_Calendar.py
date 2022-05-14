def largest_digit_in_number(n):
  return max(int(digit) for digit in str(n))

magic_number = int(input())
tasks = 0
while magic_number != 0:
  magic_number = magic_number - largest_digit_in_number(magic_number)
  tasks += 1

print(tasks)


# dp = {}

# def solve(n):
#   if n < 10:
#     return 1
#   else:
#     if n not in dp:
#       dp[n] = solve(n - largest_digit_in_number(n)) + 1
#     return dp[n]


# print(solve(int(input())))

# https://www.acmicpc.net/problem/2742

# print(
#     '\n'.join(
#         map(
#             str,
#             range(int(input()), 0, -1)
#         )
#     )
# )


print('\n'.join(map(str, [n for n in range(int(input()), 0, -1)])) + '\n')

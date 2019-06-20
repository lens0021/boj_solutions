# https://www.acmicpc.net/problem/11590
# The number of teleportations a Loda can make depends on one special
# subsequence (not necessarily consecutive) of these strings.
# Strings xi and xj (i < j) can both be in that sequence if and only if string
# xj both starts with and ends with string xi. The number of teleportations a
# Loda can make is the length of the longest described subsequence.

# Thanks for Adela https://github.com/love-adelar/algorithm/blob/16d6fa0d0da7d1973b9f13fba1fea85f58d22cac/acmicpc/acmicpc11590/acmicpc11590.py


import sys


def log(msg, end='\n'):
    if False:
        print(msg, end=end)


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.subtree_dict = {}
        self.number_of_prefixes = 0

    def add_with_check(self, key):
        log(f'"{key}" 추가 시작:')
        node = self
        number_of_prefixes = 0

        for i, ch in enumerate(key):
            log(f'  {ch}에 대해', end=' ')

            if ch not in node.subtree_dict:
                log(f'서브트리({list(node.subtree_dict.keys())})에', end=' ')
                node.subtree_dict[ch] = TrieNode()
                log(f'{ch}가 없으므로 새로 생성({list(node.subtree_dict.keys())})')

            # 서브트리로 이동
            node = node.subtree_dict[ch]
            log('  서브트리로 이동')

            if node.is_end and key[:i+1] == key[-i-1:]:
                number_of_prefixes = max(
                    number_of_prefixes,
                    node.number_of_prefixes
                )

        node.is_end = True
        node.number_of_prefixes = number_of_prefixes + 1

        return number_of_prefixes+1


input_length = int(sys.stdin.readline())
previous_sequence_of = [None for _ in range(input_length)]

if input_length == 1:
    print(1)
else:
    trie = TrieNode()

    print(max([
        trie.add_with_check(sys.stdin.readline().rstrip())
        for _ in range(input_length)
    ]))

# Thanks for Adela https://github.com/love-adelar/algorithm/blob/16d6fa0d0da7d1973b9f13fba1fea85f58d22cac/acmicpc/acmicpc11590/acmicpc11590.py

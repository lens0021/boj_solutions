# https://www.acmicpc.net/problem/11590
# The number of teleportations a Loda can make depends on one special
# subsequence (not necessarily consecutive) of these strings.
# Strings xi and xj (i < j) can both be in that sequence if and only if string
# xj both starts with and ends with string xi. The number of teleportations a
# Loda can make is the length of the longest described subsequence.

import sys


def log(msg, end='\n'):
    if True:
        print(msg, end=end)


class TrieNode:
    def __init__(self):
        self.is_end = 0
        self.subtree_dict = {}

    def add_with_check(self, key):
        log(f'"{key}" 추가 시작:')
        found_count = 0
        node = self
        for i, ch in enumerate(key):
            log(f'{ch}에 대해', end=' ')

            if ch not in node.subtree_dict:
                log(f'서브트리({list(node.subtree_dict.keys())})에', end=' ')
                node.subtree_dict[ch] = TrieNode()
                log(f'{ch}가 없으므로 새로 생성({list(node.subtree_dict.keys())})')

            # 서브트리로 이동
            node = node.subtree_dict[ch]
            log('서브트리로 이동')

            if node.is_end > 0 and key[:i+1] == key[-i-1:]:
                log(f'추가:{node.is_end}')
                found_count += node.is_end

        node.is_end += 1

        return found_count+1


trie = TrieNode()

input_length = int(sys.stdin.readline())
if input_length == 1:
    print(1)
else:
    print(max([
        trie.add_with_check(sys.stdin.readline().rstrip()) for _ in
        range(input_length)
    ]))

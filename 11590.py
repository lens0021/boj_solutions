# https://www.acmicpc.net/problem/11590
# The number of teleportations a Loda can make depends on one special
# subsequence (not necessarily consecutive) of these strings.
# Strings xi and xj (i < j) can both be in that sequence if and only if string
# xj both starts with and ends with string xi. The number of teleportations a
# Loda can make is the length of the longest described subsequence.

import sys

Debug = False


def log(msg, end='\n'):
    if Debug:
        print(msg, end=end)


class TrieNode:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.subtree_dict = {}

    def add_with_check(self, key):
        log(f'"{key}" 추가 시작:')
        found_prefix = False
        node = self
        for i, ch in enumerate(key):
            is_last_character = i == len(key)-1
            log(f'{i}번 참조', end='')
            if is_last_character:
                log('이자 마지막 글자 ', end='')
            log(f'{ch}에 대해')

            if ch not in node.subtree_dict:
                log(f'서브트리({list(node.subtree_dict.keys())})에 ')
                log(f'{ch}가 없으므로 새로 생성')
                node.subtree_dict[ch] = TrieNode(is_end=is_last_character)

            log(f'현재 서브트리 구성: {list(node.subtree_dict.keys())}')
            # 서브트리로 이동
            node = node.subtree_dict[ch]

            if not is_last_character and node.is_end:
                found_prefix = True
                log('    찾은 걸로 표시')

        return found_prefix


forword_trie = TrieNode(False)
reversed_trie = TrieNode(False)
count = 0

for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()

    forword = forword_trie.add_with_check(string)
    # reverse = reversed_trie.add_with_check(string[::-1])

    if forword:
        count += 1

print(count)

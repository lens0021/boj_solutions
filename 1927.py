# https://www.acmicpc.net/problem/1927
import sys

number_of_numbers = int(sys.stdin.readline())

heap = []
#    0
#  1   2
# 3 4 5 6


def parent_of(index):
    return (index-1)//2


def left_child_of(index):
    return index*2+1


for _ in range(number_of_numbers):
    number = int(sys.stdin.readline())

    if number == 0:
        if not heap:
            print(0)
        else:
            # Pop and print number from heap
            print(heap[0])
            temp = heap.pop()

            parent = 0
            child = left_child_of(parent)

            while child < len(heap):
                # (index of the left child + 1) is index of the right child
                if child+1 < len(heap) and heap[child+1] < heap[child]:
                    child += 1

                if temp <= heap[child]:
                    break

                heap[parent] = heap[child]
                parent = child
                child = left_child_of(child)

            if parent < len(heap):
                heap[parent] = temp
    else:
        # Push number to heap
        heap.append(number)
        index = len(heap) - 1
        while index > 0 and number < heap[parent_of(number)]:
            heap[index] = heap[parent_of(number)]
            index = parent_of(number)
        heap[index] = number

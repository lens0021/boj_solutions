# https://www.acmicpc.net/problem/12015
import sys

sys.stdin.readline()
progression = map(int, sys.stdin.readline().split())
arr = []

for num in progression:
    if not arr:
        arr.append(num)
    elif len(arr) == 1 and num < arr[0]:
        arr[0] = num
    else:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (high + low)//2

            if num < arr[mid]:
                high = mid-1
            elif num > arr[mid]:
                low = mid+1
            else:
                low = mid
                break

        if arr[low] == num:
            pass
        elif arr[low] > num:
            arr[low] = num
        else:
            if low+1 >= len(arr) - 1:
                arr.append(num)
            else:
                arr[low+1] = num

print(len(arr))

# binary search using itarative method

def binary_itarative(List, item):
    low = 0
    high = len(List) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if List[mid] < item:
            low = mid + 1
        elif List [mid] > item:
            high = mid - 1
        else:
            return mid
    return -1

List = [10, 20, 30, 34, 45, 56, 78, 90]
item = 34

result = binary_itarative(List, item)
if result != -1:
    print("Element is present at index: ", result)
else:
    print("Element is Not present in list")

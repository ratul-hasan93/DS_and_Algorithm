# binary search using itarative method

# def binary_itarative(List, item):
#     low = 0
#     high = len(List) - 1
#     mid = 0
#     while low <= high:
#         mid = (high + low) // 2
#         if List[mid] < item:
#             low = mid + 1
#         elif List [mid] > item:
#             high = mid - 1
#         else:
#             return mid
#     return -1

# List = [10, 20, 30, 34, 45, 56, 78, 90]
# item = 34

# result = binary_itarative(List, item)
# if result != -1:
#     print("Element is present at index: ", result)
# else:
#     print("Element is Not present in list")

def ita(arr, n):
    l = 0
    h = len(arr) -1
    m = 0

    while l <= h:

        m = (h+l) // 2
        
        if arr[m] < n:
            l = m + 1
        elif arr [m] > n:
            h = m -1
        else:
            return m
    
    return 0

arr = [1,2,3,4,5,6,7,8,9,10]
n = 76
hudai = ita(arr, n)

if hudai != 0:
    print("present: ", hudai)
else:
    print("not present")

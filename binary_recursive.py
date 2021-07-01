# binary searching character type use recursive function

def binary_char(arr, start, end, x):
    if end >= start:
        mid = start + (end - start)//2
        if arr [mid] == x:
            return mid
        elif arr [mid] > x:
            return binary_char(arr, start, mid-1, x)
        elif arr [mid] < x:
            return binary_char(arr, mid+1, end, x)

    return -1

arr = ["A", "B", "D", "F", "L", "M", "N", "O"]
x = "N"

result = binary_char(arr, 0, len(arr)-1 ,x)
if result != -1:
    print("Element is present at index: ", result)
else:
    print("Element is not present in array")
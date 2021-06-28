# Linear search in python

def linear(arr, n, search):
    for L in range (0, n):
        if(arr[L] == search):
            return L
    return -1

arr = [10, 20, 30, 40, 60]
n = len(arr)
search = 60

index = linear(arr, n, search)
if (index == -1):
    print('searching not found')
else:
    print('searching found at index', index)


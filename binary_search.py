# binary search in array

def binary(List, item):
    low = 0
    high = len(List) -1
    
    while low <= high:

        mid = (low + high) // 2
        
        if List[mid] == item:
            print("value found at list", mid)
            return
        
        if List [mid] < item:
            low = mid + 1
        
        if List[mid] > item:
            high = mid - 1

    print("oops! value not found at list")

List = [10, 20, 30, 40, 50, 60, 75, 80,90]
binary(List, item = 90)


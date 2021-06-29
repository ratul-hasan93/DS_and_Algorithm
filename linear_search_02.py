#Linear search while loop

Positon = -1

def search(List, Item):

    i = 0

    while i<len(List):
        if List[i] == Item:
           globals()["Positon"] = i
           return True
        i = i + 1
    return False

List = [20, 34, 45, 54, 66, 32]
Item = 32

if search(List, Item):
    print("found at index:", Positon)
else:
    print("Not found")

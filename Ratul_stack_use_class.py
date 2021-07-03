# stack using class method

class STACK:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def isEmpty(self):
        return len(self.elements) == 0

    # def size(self):
        # return len(self.elements)



if __name__ == '__main__':
    stack = STACK()
    
    ## checking isEmpty method --> true
    print(stack.isEmpty())

    ##pushing the elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    ## again checking isEmpty method --> false
    print(stack.isEmpty())

    ## printing the topmost element of the stack-->5
    print(stack.peek())
    
    ## popping the topmost element -> 5
    stack.pop()
    
    ## checking the topmost element using peek method -> 4
    print(stack.peek())

    ## popping  all the element
    stack.pop()
    stack.pop() 
    stack.pop() 
    stack.pop() 

    ## checking the isEmpty method for the last time -> true
    print(stack.isEmpty())






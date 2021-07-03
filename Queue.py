# Queue data structure using class

class QUEUE:
    
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)
        return data

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]
    
    def rear(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0


if __name__ == '__main__' :

    queue = QUEUE()

    # checking isEmpty method --> true
    print(queue.isEmpty())

    # adding the items
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(7)


    # again checking  isEmpty method --> false
    print(queue.isEmpty())

    # printing the front and rear method--> 1, 7
    print(queue.front(), end = '   ')
    print(queue.rear())

    # removing item --> 1
    queue.dequeue()

    # printing the front and rear method --> 2, 7
    print(queue.front(), end = '   ')
    print(queue.rear())

    # removing items
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    # checking isEmpty method for the last time --> True or False
    print(queue.isEmpty())







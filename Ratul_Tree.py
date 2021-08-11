# Tree implementation post-rder, pre-order, in-order

"""
              5
            /   \
           4     8
         /  \      \
        2   10      9
            / \    /  \
           6   1  3    7

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


def create_tree():
    five = Node(5)
    four = Node(4)
    eight = Node(8)
    five.add_left(four)
    five.add_right(eight)
    
    two = Node(2)
    ten = Node(10)
    four.add_left(two)
    four.add_right(ten)

    six = Node(6)
    one = Node(1)
    ten.add_left(six)
    ten.add_right(one)

    nine = Node(9)
    eight.add_right(nine)

    three = Node(3)
    seven = Node(7)
    nine.add_left(three)
    nine.add_right(seven)
    # return root node
    return five


def pre_order(node):
    print(node.data, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.data, end=' ')

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.data, end=' ')
    if node.right:
        in_order(node.right)

if __name__ == "__main__":
    tree = create_tree()
    print(tree.data)
    print('\n')

    pre_order(tree)
    print('\n')
    post_order(tree)
    print('\n')
    in_order(tree)
    print('\n')
# stack use function

def STACK_fn():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False

def push(stack, insert_v):
    stack.append(insert_v)

def peek(stack):
    return stack[-1]

def pop(stack):
    if isEmpty(stack):
        return "stack is Empty"

    return stack.pop()


stack = STACK_fn()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
print("after insert", stack)

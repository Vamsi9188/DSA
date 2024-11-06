stack=[]
maxSize=5

def push(x):
    if len(stack)==maxSize:
        print("Stack Overflow Exception")
        return 
    stack.append(x)

def pop():
    if stack:
        return stack.pop()
    print("Stack Underflow Exception")
    return -1

def isEmpty():
    return not bool(stack)

def top():
    return None if isEmpty() else stack[-1]

print(push(5))
print(push(4))
print(push(5))
print(push(4))
print(push(5))
print(push(4)) # Error
print(isEmpty())
print(pop())
print(top())
print(pop())
print(top())
print(pop())
print(top())
print(pop())
print(top())
print(pop())
print(top())
print(pop())
print(top())


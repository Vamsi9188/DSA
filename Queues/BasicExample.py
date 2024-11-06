from collections import deque
queue=deque()
maxSize=4

def push(x):
    if len(queue)==maxSize:
        print("Overflow Error",x)
        return 
    queue.append(x)

def pop():
    if not queue:
        print("Underflow Error")
        return None
    return queue.popleft()

print(push(5))
print(push(4))
print(push(5))
print(push(4))
print(push(5))
print(push(4)) #Error

print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())


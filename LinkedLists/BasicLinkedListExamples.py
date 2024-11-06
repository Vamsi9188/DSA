# ======================== LINKED LISTS ============================== #
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return f"{self.data=} {self.next=}"
a=Node(3)
b=Node(4)
a.next=b
b.next=None
print(a)
print(a.data)
print(b)
print(b.data)


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return f"{self.data=} {self.next}"
def countNodes(head):
    count=0
    while head:
        count += 1
        head=head.next
    print("Count Linked List:",count)
    return count
a=Node(3)
b=Node(4)
c=Node(5)
a.next=b
b.next=c
c.next=None
print(a)
print(b)
countNodes(a)
countNodes(b)
countNodes(c)
countNodes(None)
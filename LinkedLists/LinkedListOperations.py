class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print(None)
def countNodes(head):
    count=0
    while head:
        count += 1
        head=head.next
    print("The total nodes in LL:",count)
    return count
# Insert At Begining
def insertAtBegining(head,num):
    # return Node(head,num)
    node=Node(num)
    node.next=head
    return node
# Insert At End
def insertAtEnd(head,num):
    node=Node(num)
    if not head:
        return node
    ptr=head
    while ptr.next!=None:
        ptr=ptr.next
    ptr.next=node
    return head
# Insert At Position
def insertAtPosition(head,num,pos):
    if not head or pos==0:
        return Node(num,head)
    i=0
    ptr=head
    while ptr.next and i<pos-1:
        ptr=ptr.next
        i+=1
    node=Node(num)
    node.next=ptr.next
    ptr.next=node
    return head
# Delete At Begining
def deleteAtBegining(head):
    if head:
        return head.next
    return None
# Delete At End
def deleteAtEnd(head):
    if not head or not head.next:
        return None
    ptr=head
    while ptr.next.next:
        ptr=ptr.next
    ptr.next=None
    return head
# Delete At Position
def deleteAtPosition(head,pos):
    if pos==0 and head:
        return head
    i=0
    ptr=head
    while ptr and i<pos-1:
        ptr=ptr.next
        i+=1
    if ptr and ptr.next:
        ptr.next=ptr.next.next
    return head

head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
printLL(head)
countNodes(head)
head=insertAtBegining(head,0)
printLL(head)
head=insertAtEnd(head,6)
printLL(head)
head=insertAtPosition(head,12,4)
printLL(head)
head=deleteAtBegining(head)
printLL(head)
head=deleteAtEnd(head)
printLL(head)
head=deleteAtPosition(head,3)
printLL(head)
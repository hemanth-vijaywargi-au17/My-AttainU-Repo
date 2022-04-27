class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def printlist(head):
    if head is None:
        print("LL is Empty")
    else:
        cur = head
        while cur != None:
            print(cur.val, end="  ")
            cur = cur.next
    print()


print("Linked List Reversal Iteratively :")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printlist(head)


def reverse_ll(head):
    prev = None
    cur = head

    while cur != None:
        next = cur.next

        cur.next = prev

        prev = cur
        cur = next

    return prev  # New Head of the Linked List


printlist(reverse_ll(head))

print("Linked List Reversal Recursively :")
head = Node(45)
head.next = Node(5)
head.next.next = Node(67)
head.next.next.next = Node(90)
printlist(head)


def reverse_ll_rec(cur, prev=None):
    if cur is None:
        return prev

    next = cur.next

    cur.next = prev

    return reverse_ll_rec(next, cur)


printlist(reverse_ll_rec(head))

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    cur = head
    while cur != None and cur.next != None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def printlist(head):
    if head is None:
        print("LL is Empty")
    else:
        cur = head
        while cur != None:
            print(cur.val, end="  ")
            cur = cur.next
    print()


if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

    print("Original :")
    printlist(head)

    print("Duplicates Removed :")
    printlist(deleteDuplicates(head))
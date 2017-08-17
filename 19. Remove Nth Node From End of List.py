def  removeNthFromEnd(self,head,n):
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    while n > 0:
        fast = fast.next
        n-=1
    while fast.next:
        fast=fast.next
        slow=slow.next
    slow.next = slow.next.next
    return dummy.next

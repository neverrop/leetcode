from Queue import PriorityQueue
def merge(self,lists):
    q = PriorityQueue()
    dummy  = ListNode(None)
    curr = dummy
    for node in lists:
        if node : q.put((node.val,node))
    while q.qsize()>0:
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next: q.put((curr.next.val,curr.next))
    return dummy.next
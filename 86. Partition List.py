class ListNode:
    def __init__(self, initdata):
        self.val = initdata
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.val = newdata

    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, li):
        if isinstance(li, int):
            li = [li]
        for item in li:
            current = self.head
            previous = None
            stop = False
            while current != None and not stop:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()
            temp = ListNode(item)
            if previous == None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def tolist(self):
        p = self.head
        re = []
        while p != None:
            re.append(p.val)
            p = p.next
        return re

l = OrderedList()
l.add([2,1])
h = l.head

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pre,dummy = ListNode(0),ListNode(1)
        p1,p2 = pre,dummy
        while head:
            if head.val<x:
                pre.next = head
                pre,head = head,head.next
            else:
                dummy.next = head
                dummy,head = head,head.next
        # dummy.next = None
        pre.next = p2.next
        return p1.next

Solution().partition(h,2)
print l.tolist()
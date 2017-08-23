class ListNode:
    def __init__(self,initdata):
        self.val = initdata
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.val = newdata

    def setNext(self,newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
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

    def add(self,li):
        if isinstance(li,int):
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
        while p!=None:
            re.append(p.val)
            p=p.next
        return re

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                p.next = head
            else:
                p = p.next
                head = head.next
        return dummy.next

h = OrderedList()
h.add([1,1,2,2,3,4,4,5,6,7,7])
hh = h.head
t = Solution().deleteDuplicates(hh)

print t.tolist()
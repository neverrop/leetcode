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

    def tolist(self):
        p = self
        re = []
        while p!=None:
            re.append(p.val)
            p=p.next
        return re

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

l = OrderedList()
l.add([1,2,3,4,5,6])
h = l.head

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre= ListNode(0)
        p = pre
        pre.next = head
        c = 1
        while c<m:
            pre = head
            head = head.next
            c += 1
        p1 = pre
        p2 = head
        pre = None
        while c>=m and c<=n:
            curr = head.next
            head.next = pre
            pre = head
            head = curr
            c+=1
        p1.next = pre
        p2.next = curr
        return p.next

Solution().reverseBetween(h,1,3)
print l.tolist()
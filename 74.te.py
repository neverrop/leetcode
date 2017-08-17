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
        p,tmp = head,head
        while p and p.next:
            if p.next.val!=p.val and (p.next.next and p.next.val != p.next.next.val):
                p = p.next
            if p.next.val == p.val:
                tmp = p
                while tmp.next and tmp.next.val == tmp.val:
                    tmp = tmp.next
                head = tmp.next
                p = tmp.next
                tmp.next = None
            else:
                tmp = p
                while tmp.next.next and tmp.next.val == tmp.next.next.val:
                    tmp = tmp.next
                p.next = tmp.next.next
                p = p.next
        return head

h = OrderedList()
h.add([1,2,2,3,3,5,6])

hh =h.head
Solution().deleteDuplicates(hh)

print(h.tolist())

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

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

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

def print_list(node):
    li = []
    while node:
        li.append(node.data)
        node = node.next
    print li

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p1 = head
        p = head
        length =1
        if k==0 or (not head) or (not head.next):
            return head
        while p.next:
            p = p.next
            length+=1
        k = k%length
        if k==0:
            return head
        for i in range(length -k-1):
            p1 = p1.next
        a = p1.next
        p.next = head
        p1.next = None
        return a

l= OrderedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)

n = l.head
print n.getData()
print_list(n)
print_list(Solution().rotateRight(n,5))
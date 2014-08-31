
class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.getNext()
        return count

    def search(self, item):
        cur = self.head
        found = False
        while cur != None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while not found:
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        # Found it
        if prev == None:
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext())


class Node(item):

    def __init__(self, item):
        self.data = item
        self.next = none

class LinkedList:

    def __init__(self):
        seld.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        cur = self.head
        prev = None
        found = False

        while cur != None and not found:
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        if prev == None:
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext()

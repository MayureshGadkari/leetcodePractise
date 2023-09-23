##create a linkedlist

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self,data):
        #new_node = node(data)

        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = node(data)

    def printll(self):
        if self.head is None:
            print("hi")
        else:
            itr = self.head
            ll = ''
            while itr:
                ll += str(itr.data)+'-->'
                itr = itr.next
            print(ll)

output = LinkedList()
output.insertEnd(5)
output.insertEnd(10)
output.insertStart(3)
output.insertStart(5)
output.printll()

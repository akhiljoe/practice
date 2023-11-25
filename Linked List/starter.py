class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return

    
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        counter_index = 0
        current_node = self.head
        if index ==0:
            self.insertAtBegin(data)
            return
        while (current_node is not None) and (counter_index<index-1):
            current_node = current_node.next
            counter_index +=1
        
        if current_node is not None:
            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
        else:
            print("Index not present!")    
    
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node


    def updateNode(self, val, index):
        current_node = self.head
        count_index = 0
        if index==0:
            current_node.data = val
        while (current_node is not None) and count_index<index:
            current_node = current_node.next
            count_index+=1
        
        if current_node is not None:
            current_node.data = val
        else:
            print("Index not Present!")


    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def remove_last_node(self):
        current_node = self.head
        while (current_node.next.next) is not None:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        counter_index = 0
        current_node = self.head
        if index==0:
            self.remove_first_node()
        while (current_node is not None) and (counter_index<index-1):
            current_node = current_node.next
            counter_index+=1
        if current_node is not None:
            current_node.next = current_node.next.next
            return
        else:
            print("Index not present!!")
    
    def printll(self):
        current_node = self.head
        while current_node:
            if current_node.next is None:
                print(f"{current_node.data}")
            else:
                print(f"{current_node.data} --> ",end="")
            current_node = current_node.next
        
        
if __name__ == "__main__":
    print("\n")
    
    llist = LinkedList()
    llist.insertAtBegin(8)
    llist.insertAtBegin(7)
    llist.insertAtBegin(9)
    llist.insertAtBegin(1)
    llist.insertAtBegin(2)
    llist.printll()
    # llist.insertAtIndex("4", 1)
    llist.insertAtEnd(11)
    llist.printll()
    llist.updateNode(100, 3)
    llist.printll()
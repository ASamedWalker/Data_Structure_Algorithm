# Build the linkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
            self.tail = new_value
        else:
            self.tail.next = new_value
            self.tail = new_value
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


mylinkedlist = Linkedlist(2)
mylinkedlist.append(1)

print("There first element in the object is:")
mylinkedlist.print_list()

# mylinkedlist.prepend(1)
# mylinkedList.append(6)
# mylinkedList.append(7)
print("------------------------")
print(mylinkedlist.pop_first())
print(mylinkedlist.pop_first())
print(mylinkedlist.pop_first())


# print("After appending the new object values are:")
mylinkedlist.print_list()
# print("------------------------")
# print("We now want to pop the out items in the list:")
# print(f"{mylinkedList.pop()}")
# print(f"{mylinkedList.pop()}")
# print(f"{mylinkedList.pop()}")
# print(f"{mylinkedList.pop()}")
# print(f"{mylinkedList.pop()}")

# print(f"{mylinkedList.pop()}")

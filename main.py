# Class implementation of a singly linked list convention head -> tail
# Node class holds the data and the pointer to the next object
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Class for managing the list and the head
# Camel case for naming classes instead of snake case like for functions and variables
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    # iterator explain yield?
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        size = self.size
        return size


#############################################################################################
# In class part #############################################################################

    def clear(self):
        self.head = None
        self.head = None
        self.size = 0

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def delete(self, data):
        current = self.head
        prev = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                    self.size -= 1
                    return
            prev = current
            current = current.next


if __name__ == '__main__':

    linked_list = SinglyLinkedList()
    linked_list.append("first")
    linked_list.append("second")
    linked_list.append("third")
    linked_list.append("fourth")

    for word in linked_list.iter():
        print(word)

    print(linked_list.get_size())

    linked_list.delete("second")

    for word in linked_list.iter():
        print(word)

    print(linked_list.get_size())
    print(linked_list.search("fourth"))
    print(linked_list.search("test"))

    linked_list.clear()

    for word in linked_list.iter():
        print(word)

    print(linked_list.get_size())

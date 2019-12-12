class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node):
        node.next = self.head
        self.head = node

    def sortedPush(self, node):
        if self.head is None:
            self.head = node
        elif self.head.value < node.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                if current.value > node.value > current.next.value:
                    node.next = current.next
                    current.next = node
                else:
                    current = current.next
            if current.next is None and node.next is None:
                current.next = node

    def print(self):
        value_to_print = self.head
        while value_to_print:
            print(value_to_print.value, end="->")
            value_to_print = value_to_print.next


list = LinkedList()
new_node = Node(5)
list.push(new_node)
new_node = Node(7)
list.push(new_node)
new_node = Node(11)
list.push(new_node)
new_node = Node(13)
list.push(new_node)
new_node = Node(21)
list.push(new_node)
new_node = Node(30)
list.push(new_node)

new_node = Node(1)
list.sortedPush(new_node)
new_node = Node(15)
list.sortedPush(new_node)
new_node = Node(16)
list.sortedPush(new_node)
new_node = Node(2)
list.sortedPush(new_node)

print("Create Linked List")
list.print()

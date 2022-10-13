
from icecream import ic


class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None


class LinkedList:
    def __init__(self, head_value=None):
        self.head_value = head_value

    def print_linked_list(self):
        ic("*************************************")
        node = self.head_value
        while node:
            ic(node.data_value)
            node = node.next_value
        ic("*************************************")

    def add_node_at_beginning(self, new_node):
        new_node.next_value = self.head_value
        self.head_value = new_node

    def add_node_at_endning(self, new_node):
        if not self.head_value:
            self.head_value = new_node
        iternation_node = self.head_value
        while iternation_node.next_value:
            iternation_node = iternation_node.next_value
        iternation_node.next_value = new_node


if __name__ == '__main__':
    node1 = Node("Mumbai")
    node2 = Node("Dehli")
    node3 = Node("Banglore")
    node4 = Node("Gujarat")
    node5 = Node("Chennai")
    node1.next_value = node2
    node2.next_value = node3
    intial_linked_list = LinkedList(node1)
    intial_linked_list.print_linked_list()
    intial_linked_list.add_node_at_beginning(node4)
    intial_linked_list.print_linked_list()
    intial_linked_list.add_node_at_endning(node5)
    intial_linked_list.print_linked_list()

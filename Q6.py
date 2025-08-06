class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        # Case 2: Insert before the head (i.e., new min or max)
        if data < head.data:
            # Find the last node to update its next
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node  # New node becomes the new head

        # Case 3: Insert in between or at the end
        current = head
        while (current.next != head and current.next.data < data):
            current = current.next

        # Insert new node after current
        new_node.next = current.next
        current.next = new_node

        return head  # Head doesn't change in this case


class Solution:
    def reverseDLL(self, head):
        if head is None:
            return None
        
        current = head
        temp = None
        
        while current is not None:
            # Swap prev and next
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            # Move to the next node in the original list
            current = current.prev
        
        # After the loop, temp will be at the node before the new head
        if temp:
            head = temp.prev
        
        return head


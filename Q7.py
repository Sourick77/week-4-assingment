class Solution:
    def isCircular(self, head):
        if head is None:
            return True  # An empty list is considered circular
        
        temp = head.next
        while temp is not None and temp != head:
            temp = temp.next
            
        return temp == head


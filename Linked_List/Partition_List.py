class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        current = head  
        
        less_dummy = ListNode(0)   
        less_tail = less_dummy     
        
        greater_dummy = ListNode(0)
        greater_tail = greater_dummy 
        
        while current:
            if current.val < x:
               
                less_tail.next = ListNode(current.val)
                less_tail = less_tail.next 
            else:
               
                greater_tail.next = ListNode(current.val)
                greater_tail = greater_tail.next 
            current = current.next  
        less_tail.next = greater_dummy.next
        
        return less_dummy.next
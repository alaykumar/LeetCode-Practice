# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        curr = head
        
        # While loop to iterate through the LL
        while(curr):
            
            # If the current node value is 0 then set sum to 0
            # set the current node to a temporary node 'target'
            # then increase the current node 
            if(curr.val == 0):
                sum = 0
                target = curr
                curr = curr.next

                # if the node value is not 0 then add it to the sum
                # until a 0 is reached
                while(curr.val != 0):
                    sum += curr.val
                    curr = curr.next
                
                # Once a 0 is reached, append the sum to the value at the target node
                target.val = sum

                # if the next node exists then target is equal to the current
                # node then run the loop again
                if(curr.next):
                    target.next = curr
                # if the next value is the tail then break the loop and return the head
                else:
                    target.next = None
                    break

        return head







        

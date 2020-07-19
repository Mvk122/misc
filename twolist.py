# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def iterate_through_list(linkedList):
            returnlist = []
            next2 = linkedList
            while next2 != None:
                returnlist.append(next2.val)
                next2 = next2.next
            return returnlist 
        
        def convert_list_to_Linked_list(normallist):
            if len(normallist) == 1:
                return ListNode(normallist[0])
            return ListNode(normallist[0], convert_list_to_Linked_list(normallist[1:]))
        
        def list_to_int(lst):
            return int(''.join([str(i) for i in lst]))

        l1 = iterate_through_list(l1)
        l1.reverse()
        l2 = iterate_through_list(l2)
        l2.reverse()
        int3 = list_to_int(l1) + list_to_int(l2)
        l3 = [int(i) for i in str(int3)]
        l3.reverse()
        
        return convert_list_to_Linked_list(l3)
                

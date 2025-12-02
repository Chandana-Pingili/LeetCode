# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=temp=ListNode()
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                node=ListNode(list1.val)
                temp.next=node
                temp=node
                list1=list1.next
            elif list1.val>list2.val:
                node=ListNode(list2.val)
                temp.next=node
                temp=node
                list2=list2.next
            else:
                node=ListNode(list2.val)
                temp.next=node
                temp=node
                list2=list2.next
                node=ListNode(list1.val)
                temp.next=node
                temp=node
                list1=list1.next
        if list1 != None:
            temp.next = list1
    
        if list2 != None:
            temp.next = list2
            
        return head.next


    
        
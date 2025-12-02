# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        num1=[]
        num2=[]
        n1=0
        n2=0

        while temp1.next:
            num1.append(temp1.val)
            temp1=temp1.next
        num1.append(temp1.val)    
        num1.reverse()
        #print(num1)
        while temp2.next:
            num2.append(temp2.val)
            temp2=temp2.next
        num2.append(temp2.val)
        num2.reverse()
        #print(num2)
        for i in num1:
            n1=n1*10+i
        for j in num2:
            n2=n2*10+j
        result=n1+n2
        l=[]
        if result==0:
            l.append(0)
        else:
            while result>0:
                l.append(result%10)
                result=result//10
        print(len(l))
        print(l)
        
        start=ListNode()
       
        temp=start
      
        for i in range(len(l)):
            temp.next=ListNode(l[i])

            temp=temp.next
       
        l3=start.next
        return l3
        


        
        
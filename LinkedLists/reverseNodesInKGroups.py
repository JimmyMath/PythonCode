#Note: Your solution should have O(n) time complexity, where n is the number of element in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

#Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

#You may not alter the values in the nodes - only the nodes themselves can be changed.

#Example

#For l = [1, 2, 3, 4, 5] and k = 2, the output should be reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
#For l = [1, 2, 3, 4, 5] and k = 1, the output should be reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
#For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] linkedlist.integer l

#A singly linked list of integers.

#Guaranteed constraints:
#1 ≤ list size ≤ 10**4,
#-10**9 ≤ element value ≤ 10**9.

#[input] integer k

#The size of the groups of nodes that need to be reversed.

#Guaranteed constraints:
#1 ≤ k ≤ l size.

#[output] linkedlist.integer

#The initial list, with reversed groups of k elements.


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseNodesInKGroups(l, k):
    if k == 1:
        return l
    r,i = l.next,1
    while r:
        r = r.next
        i = i+1
    if i < k:
        return l
    dummy, n = ListNode(None), None
    for j in range(k):
        m = l.next
        l.next = n
        n = l
        dummy.next = l
        l = m
    if i == k:
        return dummy.next
    s = dummy.next.next
    for a in range(k-2):
        s=s.next
    s.next=reverseNodesInKGroups(l, k)
    return dummy.next
        
        
    

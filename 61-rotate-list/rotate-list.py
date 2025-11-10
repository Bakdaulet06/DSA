# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        nums = []
        n = 0
        while head:
            n += 1
            nums.append(head.val)
            head = head.next
        k = k % n
        nums = nums[-k:] + nums[:-k]

        res = ListNode()
        reshead = res
        for num in nums:
            res.next = ListNode(num)
            res = res.next
        return reshead.next
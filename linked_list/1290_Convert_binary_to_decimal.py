# class listNode:
#     def __init__(self,value=0,next=None):
#         self.value = value
#         self.next = next
#
# def transverse_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.value,"--->")
#         current= current.next
# #head = listNode(1, listNode(2, listNode(3, listNode(4))))
# head = listNode(1)
# head.next = listNode(2)
# transverse_linked_list(head)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def getDecimalValue(head):
    result = 0
    current = head

    while current is not None:
        # Update result by shifting left and adding the current node's value
        result = (result << 1) | current.value

        # Move to the next node
        current = current.next

    return result

# Example usage:
# Assuming you have a linked list: 1 -> 0 -> 1 -> None
head = ListNode(1, ListNode(0, ListNode(1)))

result = getDecimalValue(head)
print(result)


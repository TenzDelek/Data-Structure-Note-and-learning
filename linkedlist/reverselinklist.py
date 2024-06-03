class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head: Node) -> Node:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def print_linked_list(self, head: Node):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> None
    length=int(input("enter the size of the linkedlist: "))
    print("Enter the values of the nodes:")
    headnode=int(input("enter the headnode:"))
    head=Node(headnode)

    curr=head
    for i in range(length-1):
        nodeval=int(input("enter the val:"))
        curr.next=Node(nodeval)
        curr=curr.next
    solution = Solution()
    
    # Print original linked list
    print("Original linked list:")
    solution.print_linked_list(head)

    # Reverse the linked list
    reversed_head = solution.reverse_linked_list(head)

    # Print reversed linked list
    print("\nReversed linked list:")
    solution.print_linked_list(reversed_head)

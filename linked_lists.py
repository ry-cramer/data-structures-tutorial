'''
Program that implements a LinkedList class
- Insertions at head and elsewhere on the linked list
- Deletions at head and elsewhere on the linked list

Written by Reb Cramer on November 29, 2021
'''

class LinkedList:

    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
    
    def insert_head(self, value):
        '''
        Inserts a new head for linked list.
        '''
        new_node = LinkedList.Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
            

    def insert_middle_tail(self, value, prev_value):
        '''
        Inserts a new node after the first occurrence of the prev_value.
        '''
        new_node = LinkedList.Node(value)

        curr = self.head
        while curr is not None:
            if curr.data == prev_value:
                new_node.next_node = curr.next_node
                curr.next_node = new_node
                break
            curr = curr.next_node

    
    def delete_head(self):
        '''
        Deletes head node and sets the next node as head node.
        '''
        if self.head is not None:
            if self.head.next_node is not None:
                self.head = self.head.next_node
            else:
                self.head = None

    def delete_middle_tail(self, value):
        '''
        Deletes first node with the specified value.
        '''
        curr = self.head
        while curr is not None:
            if curr.next_node.data == value:
                curr.next_node = curr.next_node.next_node
                break
            curr = curr.next_node

    def __iter__(self):
        """
        Iterate through LinkedList
        """
        curr = self.head
        while curr is not None:
            yield curr.data 
            curr = curr.next_node

    def __str__(self):
        output = 'LinkedList: '
        for i in self:
            output += str(i)
            output += ' '
        return output

ll = LinkedList()
ll.insert_head(5)
ll.insert_middle_tail(3, 5)
ll.insert_middle_tail(6, 3)
ll.insert_head(9)
ll.insert_middle_tail(8, 3)
print(ll) # Expected output: LinkedList: 9 5 3 8 6

ll.delete_head()
ll.delete_middle_tail(6)
ll.delete_middle_tail(3)
print(ll) # Expected output: LinkedList: 5 8
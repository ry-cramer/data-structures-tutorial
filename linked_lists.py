'''
Program that implements a LinkedList class
- Insertions at head and elsewhere on the linked list
- Deletions at head and elsewhere on the linked list

Written by Reb Cramer on November 29, 2021
'''

class LinkedList:

    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, value):
        '''
        Inserts a new head for linked list.
        '''
        new_node = LinkedList.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_tail(self, value):
        '''
        Inserts a new tail for linked list.
        '''
        new_node = LinkedList.Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def insert_middle(self, value, prev_value):
        '''
        Inserts a new node after the first occurrence of the prev_value.
        '''
        new_node = LinkedList.Node(value)

        curr = self.head
        while curr is not None:
            if curr.data == prev_value:
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node
                break
            curr = curr.next

    
    def delete_head(self):
        '''
        Deletes head node and sets the next node as head node.
        '''
        if self.head is not None:
            if self.head.next != self.tail:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None

    def delete_tail(self):
        '''
        Deletes tail node and sets the previous node as tail node.
        '''
        if self.tail is not None:
            if self.tail.prev != self.head:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None

    def delete_middle(self, value):
        '''
        Deletes first node with the specified value.
        '''
        curr = self.head
        while curr is not None:
            if curr.data == value:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                break
            curr = curr.next

    def __iter__(self):
        """
        Iterate through LinkedList
        """
        curr = self.head
        while curr is not None:
            yield curr.data 
            curr = curr.next

    def __str__(self):
        output = 'LinkedList: '
        for i in self:
            output += str(i)
            output += ' '
        return output

ll = LinkedList()
ll.insert_head(5)
ll.insert_tail(3)
ll.insert_middle(6, 5)
ll.insert_head(9)
ll.insert_middle(8, 5)
ll.insert_tail(4)
print(ll) # Expected output: LinkedList: 9 5 8 6 3 4

ll.delete_head()
ll.delete_middle(6)
ll.delete_middle(3)
print(ll) # Expected output: LinkedList: 5 8 4

ll.delete_tail()
print(ll) # Expected output: LinkedList: 5 8
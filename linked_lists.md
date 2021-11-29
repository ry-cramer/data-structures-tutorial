# Linked Lists

An array in python is organized by each index of the list containing a value. That index is used to represent that value in the list and can be used to insert, delete, or find a value in the list. A **linked list** is organized a bit differently; not by indexes pointing to specific values, but each value pointing to the next value in the list.

## The Concept

Here's an example of how a standard array is structured and saved in memory:

![](array.jpg)

Each value is saved at a specific location in the list, which is represented by the index. Let's call one position in the array a **node**. For example, the value `7` is at index 0, and the value `98` is at index 4. if you want to see what value is stored third in the list, you search for the value with `value = array[2]`, which will return the value `6`.

In contrast, let's look at how a linked list is stored in memory:

![](single_linked_list.png)

A linked list is made up of nodes as well, but instead of containing the value and its position in the list, the node contains the value and a **pointer** to the next node in the linked list. For example, let's say we have a linked list with the numbers 3, 7, 5, 8, and 1. If I want to find the third value in the list, I have to start at the first node: 3. That node then points me to the next node: 7. Then that node finally points me to the node I'm looking for, and we can see that the value is 5. Instead of searching a specific position for a value, we have to **traverse** the linked list until we arrive at the value.

### Doubly Linked Lists

A **singly linked list** works exactly as we described above, but a **doubly linked list** is slightly more useful in different contexts. This linked list works the same as the singly linked list, but instead of a node pointing only to the next node, a node will contain the value, a pointer to the next node, *and a pointer to the previous node*. This allows the user to traverse both ways through a linked list, as well as manipulate the **tail** of the list (the last node of the list) as easily as the **head** (the first node of the list).

Here's a picture for reference:

![](double_linked_list.png)

A singly linked list is less complicated to implement and less memory consuming than a doubly linked list because it stores less information in each node, but a doubly linked list allows for certain operations to be done faster, like insertion and deletion, and allows you to traverse both forwards and backwards through the list. There are other pros and cons to each that you can look up on other sites if you have specific questions.

## Common Operations

### Traversing

In a singly linked list, we can only traverse forward through the list. This is a simple operation. 

```python
def traverse(self):
	curr = self.head
	while curr is not None:
		print(curr.data)
		curr = curr.next
```

This is a class function with a `head` attribute, which we use to access the linked list. Each node (including the head) is of the Node class, which stores its value (`data`) and its pointer (`next`). To traverse the list, start at the head, then open a loop to detect when the linked list is over. Print the value of the node, then change the current node to the node it's pointing to. Since the tail of the linked list points to None, the loop will end when current becomes None.

### Insertion

There are two main steps to complete insertions to the middle or end of a singly linked list: find the node to insert the new node after, and change the pointers of that node and the new node to point to the proper places in the list. The first step can be completed by providing the node to insert after, but the second is slightly more complicated. 

1. Change the pointer of the new node to point to the node that was after the previous node
2. Change the pointer of the previous node to point to the new node

To insert to the head, there is a different but easier process. No need to find the place to put the node--we just need to make the node's pointer the old head and make it the new head.

### Deletion

This operation is very similar to the insertion operation; we only need to find the node to delete, and then make the previous node's pointer the node after the node to be deleted. The node is effectively lost from memory.

To delete the head, just make the second node the head node. We don't need to do anything else, since no other node points to the head node.

## Array or Linked List: Which is Better?

Arrays and linked lists both have pros and cons. First of all is their time complexity (Big O):

|                     | Array   | Linked List   |
|:--------------------|:--------|:--------------|
| Inserting at Head   | O(n)    | O(1)          |
| Inserting in Middle | O(n)    | O(n)          |
| Inserting at Tail   | O(1)    | O(1)          |
| Deleting at Head    | O(n)    | O(1)          |
| Deleting in Middle  | O(n)    | O(n)          |
| Deleting at Tail    | O(1)    | O(1)          |

As you can see, linked lists have a faster performance for inserting and deleting at the head. They also are generally faster at insertions and deletions because they only need to readjust the pointers of the nodes involved, whereas arrays need to be increased in size and all their elements shifted over one.

Thus, if quick insertions and deletions are important, then a linked list is the way to go, especially for queues, where all insertions happen at the end and deletions happen at the front.

However, the location and order of items in a dynamic array is not as hard to change or obtain in an array as in a linked list. This means that switching positions of items in an array, or returning a random item from the array is easier in an array than in a linked list. An array also costs slightly less memory than a linked list because it isn't storing pointers in its nodes.

In general, linked lists should be used in queues and situations where the size of the data changes often. Arrays are better for smaller sets of data where the size is more constant or where changing positions of data or generating random choices of items in the group is important.

## Problem to Solve

Implement functions to delete and insert values into a linked list for a LinkedList class. The code below is provided for you to use to start your program:

```python
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
        pass
            

    def insert_middle_tail(self, value, prev_value):
        '''
        Inserts a new node after the first occurrence of the prev_value.
        '''
        pass

    
    def delete_head(self):
        '''
        Deletes head node and sets the next node as head node.
        '''
        pass

    def delete_middle_tail(self, value):
        '''
        Deletes first node with the specified value.
        '''
        pass

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
```

Make sure to run the program when you are done and check the tests for the proper output.

Here is a [solution](linked_lists.py) to the problem. Note that your solution may look different, but that does not mean it is wrong. If your program passes all the tests required to complete the task, it is a valid solution. This is just one valid solution.
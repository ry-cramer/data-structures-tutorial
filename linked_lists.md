# Linked Lists

An array in python is organized by each index of the list containing a value. That index is used to represent that value in the list and can be used to insert, delete, or find a value in the list. A **linked list** is organized a bit differently; not by indexes pointing to specific values, but each value pointing to the next value in the list.

## The Concept

Here's an example of how a standard array is structured and saved in memory:

![](array.jpg)

Each value is saved at a specific location in the list, which is represented by the index. For example, the value `7` is at index 0, and the value `98` is at index 4. if you want to see what value is stored third in the list, you search for the value with `value = array[2]`, which will return the value `6`.

In contrast, let's look at how a linked list is stored in memory:

![](single_linked_list.png)

A linked list is made up of **nodes**, which are objects that contain the value and a **pointer** to the next node in the linked list. For example, let's say we have a linked list with the numbers 3, 7, 5, 8, and 1. If I want to find the third value in the list, I have to start at the first node: 3. That node then points me to the next node: 7. Then that node finally points me to the node I'm looking for, and we can see that the value is 5. Instead of searching a specific position for a value, we have to **traverse** the linked list until we arrive at the value.

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

For doubly linked lists, we are able to traverse both ways through the list. The program to do traverse backwards is the exact same as the program to traverse forwards, just with head swapped out with tail and next swapped out with previous.

```python
def traverse_reverse(self):
	curr = self.tail
	while curr is not None:
		print(curr.data)
		curr = curr.prev
```

### Insertion

There are two main steps to complete insertions to the middle or end of a singly linked list: find the node to insert the new node after, and change the pointers of that node and the new node to point to the proper places in the list. The first step can be completed by providing the node to insert after, but the second is slightly more complicated. 

1. Change the pointer of the new node to point to the node that was after the previous node
2. Change the pointer of the previous node to point to the new node

To insert to the head, there is a different but easier process. No need to find the place to put the node--we just need to make the node's pointer the old head and make it the new head. 

For doubly linked lists, we have to have an extra step for all insertions, dealing with the pointer to the previous node. The steps for insertion to the middle, after finding the node to insert after, are this:

1. Change the pointers of the new node to point to the node it is being inserted after and the node it's being inserted before
2. Change the "next" pointer to the previous node to point to the new node
3. Change the "previous" pointer of the next node to point to the new node

To insert at the head, we just need to make the new node's "next" pointer the old head, make the old head's "previous" pointer the new node, and make the new node the new head. The process is exactly the same but reversed for inserting at the tail: make the new node's "previous" pointer the old tail, make the old tail's "next" pointer the new node, and make the new node the new tail.

### Deletion

This operation is very similar to the insertion operation; we only need to find the node to delete, and then make the previous node's pointer the node after the node to be deleted. The node is effectively lost from memory.

To delete the head, just make the second node the head node. We don't need to do anything else, since no other node points to the head node.

For doubly linked lists, we need to change two pointers: the previous node's "next" pointer, and the next node's "previous" pointer. At the head, we just have to make the next node the new head and change its previous pointer to None. At the tail, we make the previous node the new tail and change its "next" pointer to None.

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

## Example: Queue

Imagine a line of people are waiting in a line to pick up free ice cream. The rule is that one person can get one ice cream cone when they reach the front of the line, but some people want more than one ice cream. So, they get back in line once they have received their ice cream to get another one. Assume it takes one second for a person to grab their ice cream and get back in line if they want another one. How can we find out how long it will take for a certain person to get all of the ice cream they want?

```python
from collections import deque

class Person:

    def __init__(self, name, ice_cream):
        self.name = name
        self.ice_cream = ice_cream

def add_to_queue(name, ice_cream, queue):
    '''
    Adds a new person to the back of the ice cream queue.
    '''
    person = Person(name, ice_cream)
    queue.append(person)

def get_ice_cream(queue):
    '''
    Removes a person from the queue and adds them to the back if they still want more ice cream.
    '''
    queue[0].ice_cream -= 1
    if queue[0].ice_cream > 0:
        queue.append(queue[0])
    queue.popleft()

def find_time(index, queue):
    '''
    Finds time it takes for specified name to get all ice cream they want.
    '''
    # Allows us to operate on our queue without disturbing the original queue
    test_queue = deque()
    for item in queue:
        add_to_queue(item.name, item.ice_cream, test_queue)
    person = test_queue[index]
    seconds = 0
    while person in test_queue:
        get_ice_cream(test_queue)
        seconds += 1
    print(seconds)

queue = deque()
add_to_queue('Jasper', 3, queue)
add_to_queue('Penelope', 1, queue)
add_to_queue('Maverick', 4, queue)
add_to_queue('Lincoln', 2, queue)
find_time(0, queue) # Output: 8
find_time(1, queue) # Output: 2
find_time(2, queue) # Output: 10
find_time(3, queue) # Output: 7
```

This example uses the deque library, which provides a linked list class. The first thing the program does is add people to the line. It then finds the amount of seconds it takes for the person at the index specified to get all of their ice cream. Notice it does this by inserting a new tail if the person wanted more ice cream, which is an O(1) operation. It then popped the head of the deque, which unlike in an array is also an O(1) operation. The queue is where the linked list shines because of this efficiency. The find_time function still operates in O(n) time, but this is because of the iterating of the get_ice_cream function and not because of the enqueue and dequeue itself.

## Problem to Solve

Implement functions to delete and insert values into a doubly linked list for a LinkedList class. The code below is provided for you to use to start your program:

```python
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
        pass
            
    def insert_tail(self, value):
        '''
        Inserts a new tail for linked list.
        '''
        pass


    def insert_middle(self, value, prev_value):
        '''
        Inserts a new node after the first occurrence of the prev_value.
        '''
        pass

    
    def delete_head(self):
        '''
        Deletes head node and sets the next node as head node.
        '''
        pass

    def delete_tail(self):
        '''
        Deletes tail node and sets the previous node as tail node.
        '''
        pass

    def delete_middle(self, value):
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
```

Make sure to run the program when you are done and check the tests for the proper output.

Here is a [solution](linked_lists.py) to the problem. Note that your solution may look different, but that does not mean it is wrong. If your program passes all the tests required to complete the task, it is a valid solution. This is just one valid solution.
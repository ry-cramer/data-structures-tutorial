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
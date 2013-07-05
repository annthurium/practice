# problem ordering:
# 1. list.add
# 2. printList functions
# 3. removeFirst / removeAll
# 4. checkCycles
# 5. reverseList
#
# don't forget that it helps a lot to have a sheet of paper with what your
# data actually looks like when trying to make it into something else.
# People seem to think that using pictures is a crutch but that's just ego;
# keeping all this in your head is annoying and error prone.
class node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

  # returns the value of this node as a string
  def __str__(self):
    return "[%s]" % (self.data)

class list:
  def __init__(self):
    self.head = None

  # add a new element to the end of the list that contains 'value'
  def add(self, value):
    # self is a list
    position = self.head
    # loop through list iteratively
    # find the end
    while position.next != None:
      position = position.next

    # now position is at the end of the list
    # we need to put data where position is
    position.next = node(value)


  # remove the first node containing 'data' from this list
  def removeFirst(self, value):
    # start at the head of the list
    previous = None
    position = self.head

    # loop through list iteratively, checking for value
    while position != None:

      # check to see if node contains value
      if position.data == value:

        # if previous == None, we're at the beginning of the list
        # and must change self.head to point to the following node
        if previous == None:
          self.head = position.next

        # if we're not at the beginning of the list
        # change pointer from the previous node to point at the following node
        # effectively removing the node from the list
        else:
          previous.next = position.next

        # since we only want to remove the first instance, return
        return

      else:
        # change previous to current position for next loop iteration
        previous = position

       # change position to next position for next loop iteration
      position = position.next


  # remove all nodes containing 'value' from this list
  def removeAll(self, value):
    # start at the head of the list
    previous = None
    position = self.head

    # loop through list iteratively, checking for value
    while position != None:

      # check to see if node contains value
      if position.data == value:

        # if previous == None, we're at the beginning of the list
        # and must change self.head to point to the following node
        if previous == None:
          self.head = position.next

        # if we're not at the beginning of the list
        # change pointer from the previous node to point at the following node
        # effectively removing the node from the list
        else:
          previous.next = position.next

      else:
        # change previous to current position for next loop iteration
        previous = position

       # change position to next position for next loop iteration
      position = position.next



# Print the list in an iterative fashion
# If the list has "hello', 'world', 'testing' in it then it should print as:
# [hello] -> [world] -> [testing] -> None
def printListIterative(list):
  position = list.head
  while position != None:
    print position
    position = position.next
    if position == None:
      print "None\n"


# Print the list in a recursive fashion
# use the same output format as above
def printListRecursive(list):
  if list.head == None:
    print list.head
    return
  position = list.head
  print position
  list.head = position.next
  printListRecursive(list)










# checks a list for a 'cycle' returns true or false
# a cycle is a condition where an element of the lists points to a previous
# element as its next element
visited = set()
def checkCyclesRecursive(list):
  if list.head == None:
    print "False"
    return False

  position = list.head
  if position in visited:
    print "True"
    return True
  else:
    visited.add(position)
    list.head = position.next
    checkCyclesRecursive(list)




























# checks a list for a 'cycle' returns true or false
def checkCyclesIterative(list):
  # start at the head of the list
  position = list.head

  # make an empty list
  elements = set()

  # use while loop to loop through list
  while position != None:
    if position in elements:
      print "True"
      return True
    else:
      elements.add(position)
      position = position.next
  print "False"
  return False














# returns a new list that is reversed version of the list passed in
def reverseListIterative(fwd_list):

  # handle edge casees: list of size 1, list of size 0
  reversed_list = list()

  # loop through list

  position = fwd_list.head
  previous = None
  while position != None:
    new_node = node(data = position.data, next = previous)
    previous = position
    position = position.next

    if position.next == None:
      reversed_list.head = position

  return reversed_list



















# returns a new list that is reversed version of the list passed in
def reverseListRecursive(list):
  pass


def main():
  """Testing code and such."""
  linked_list = list()
  node1 = node('hello')
  node2 = node('world')
  node3 = node('testing')
  linked_list.head = node1
  node1.next = node2
  node2.next = node3
  node3.next = None

  linked_list_cycle = list()
  node_1 = node('your')
  node_2 = node('mom')
  node_3 = node('lol')
  linked_list_cycle.head = node_1
  node_1.next = node_2
  node_2.next = node_3
  node_3.next = node_1

  # printListIterative(linked_list)

  # value = 'hello'
  # other_value = 'yar'


  # # list.add(linked_list, value)

  # # printListIterative(linked_list)
  # # list.removeFirst(linked_list, value)
  # # printListIterative(linked_list)

  # # list.add(linked_list, value)
  # # list.add(linked_list, other_value)
  # # list.add(linked_list, value)
  # # printListIterative(linked_list)

  # list.removeFirst(linked_list, value)
  # printListIterative(linked_list)

  printListRecursive(linked_list)



  # checkCyclesIterative(linked_list)
  # checkCyclesIterative(linked_list_cycle)

  # checkCyclesRecursive(linked_list)
  # checkCyclesRecursive(linked_list_cycle)

  rever= reverseListIterative(linked_list)
  printListRecursive(rever)
if __name__ == '__main__':
  main()
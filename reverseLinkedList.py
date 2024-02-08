# A SIMPLE LINKED LIST
# In a linked list, each data item is embedded in a link. 
# A link represents one element of the overall list. 
# Each link holds some data and a way to get to the next link in the list.
import test_list


# Node of a Linked List
class MyListNode:
    def __init__(self, data, next=None):  # Constructor
        self.__data = data  # The data for this link
        self.__next = next  # Reference to next Link

    def getData(self):  # Return the datum stored in this link
        return self.__data

    def setData(self, data):  # Change the data in this Link
        self.__data = data

    def getNext(self):  # Return the next link
        return self.__next

    def setNext(self, link):  # Change the next link to a new Link
        if link is None or isinstance(link, MyListNode):  # Must be Node or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):  # Test if link is last in the chain
        return self.getNext() is None  # True if & only if no next Link

    def has_value(self, value):  # Compare the value with the node data
        if self.data == value:
            return True
        else:
            return False


## SIMPLE LINKED LIST
class MyLinkedList(object):  # A linked list of data elements
    def __init__(self):  # Constructor
        self.__head = None  # Reference to first Link

    def getHead(self):
        return self.__head  # Return the first link

    def setHead(self, node):  # Change the first link to a new Link
        """Set the node as the head.
         Raise an Exception if node is not an instance of class ListNode"""
        if node is None or isinstance(node, MyListNode):  # It must be None or
            self.__head = node  # a Link object
        else:
            raise Exception("First link must be Link or None")

    def isEmpty(self):
        """
        Returns whether the Linked List is empty or not
        """
        # we only have to check the head if is None or not
        return self.__head == None

    def insert(self, data):  # insert the specified element to the head of this list.
        """
        Create a new node at the head of the Linked List
        """
        node = MyListNode(data, self.getHead())  # What follows is the current list
        self.__head = node  # set the head of the Linked List to the new head

    def traverse(self,  # Apply a function to all items in list
                 func=print):  # with the default being to print
        link = self.getHead()  # Start with first link
        while link is not None:  # Keep going until no more links
            func(link.getData())  # Apply the function to the item
            link = link.getNext()  # Move on to next link

    def __reverse(self, node):
        ## ADD YOUR CODE HERE
        if node is None or node.getNext() is None:
            return node

            # Recursively reverse the rest of the list
        reversed_tail = self.__reverse(node.getNext())

        # Reverse the link between the current node and its next node
        node.getNext().setNext(node)
        node.setNext(None)

        # Return the new head of the reversed list (which was the tail of the original list)
        return reversed_tail

    def recursiveReverse(self):
        self.__head = self.__reverse(self.__head)

def main():
    test_list.test_reverse()

if __name__ == '__main__':
    main()
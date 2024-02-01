import reverseLinkedList as revll

def test_reverse():
    llist = revll.MyLinkedList()

    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)

    llist.recursiveReverse()
    array = []
    llist.traverse(array.append)

    assert array == [1, 2, 3, 4]

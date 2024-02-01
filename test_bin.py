import binarysearch as bs

def test_recBinary():

    arr = bs.OrderedArray(7)
    arr.insert(5)
    arr.insert(6)
    arr.insert(1)
    arr.insert(10)
    arr.insert(4)
    arr.insert(3)

    key = 3
    assert arr.findRec(key) == arr.find(key)
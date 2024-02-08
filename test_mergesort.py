import mergesort as ms

def test_sort():
    arr = [1,5,7,3,5,2,2,4]
    arr2 = ms.Mergesort(arr).getArray()
    assert arr2 == [1,2,2,3,4,5,5,7]

def test_sort2():
    arr = [1,2,2,3,1,2,2,4]
    arr2 = ms.Mergesort(arr).getArray()
    assert arr2 == [1,1,2,2,2,2,3,4]

def test_sort3():
    arr = [1,2,2,3,1,2,2]
    arr2 = ms.Mergesort(arr).getArray()
    assert arr2 == [1,1,2,2,2,2,3]
import test_bin


class OrderedArray(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__length = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__length  # Return number of items

    def get(self, n):  # Return the value at index n
        if n >= 0 and n < self.__length:  # Check if n is in bounds, and
            return self.__a[n]  # only return item if in bounds
        raise IndexError("Index " + str(n) + " is out of range")

    def search(self, key):
        idx = self.findRec(key)  # Search for a record by its key
        if idx < self.__length and self.__a[idx] == key:
            return self.__a[idx]  # and return element if found
        return -1

    def insert(self, item):  # Insert item into the correct position
        j = self.findRec(item)  # Find where item should go
        for k in range(self.__length, j, -1):  # Move bigger items right
            self.__a[k] = self.__a[k - 1]

        self.__a[j] = item  # Insert the item
        self.__length += 1  # Increment the size

    def delete(self, item):  # Delete any occurrence
        j = self.findRec(item)  # Try to find the item
        if j < self.__length and self.__a[j] == item:  # If found,
            self.__length -= 1  # One fewer at end
            for k in range(j, self.__length):  # Move bigger items left
                self.__a[k] = self.__a[k + 1]
                self.__a[k + 1] = None
            return True  # Return success flag
        return False  # Made it here; item not found

    def traverse(self, function=print):  # Traverse all elements
        for j in range(self.__length):  # and apply a function
            function(self.__a[j])

    def find(self, key):  # Find index at or just below key
        lower = 0  # in ordered list
        upper = self.__length  # Look between lo and hi

        while lower <= upper:
            mid = (lower + upper) // 2

            if (self.__a[mid] is not None):
                if self.__a[mid] == key:  # Did we find it?
                    return mid  # Return location of item
                elif self.__a[mid] < key:  # Is key in upper half?
                    lower = mid + 1  # Yes, raise the lo boundary
                else:
                    upper = mid - 1  # No, but could be in lower half
            else:
                return lower

        return lower  # Item not found, return insertion point instead

    def __findRec(self, key, lower, upper):  # Find index at or just below key
        ## ADD YOUR CODE HERE
        half = (lower+upper)//2
        if lower > upper:
            return lower

        if self.__a[half] == key:
            return half
        elif self.__a[half]>key:
            return self.__findRec(key,lower,half-1)
        else:
            return self.__findRec(key,half+1,upper)


    def findRec(self, key):
        lo = 0  # in ordered list
        hi = self.__length - 1  # Look between lo and hi
        return self.__findRec(key, lo, hi)


def main():
    test_bin.test_recBinary()


if __name__ == '__main__':
    main()

# Implement the mergesort algorithm on arrays
import test_mergesort


class Mergesort(object):         # An object to mergesort Arrays
   def __init__(self,            # Constructor takes the unordered
                unordered):       # array and orders its items by using  mergesort on their keys
      self.__arr = unordered     # Array starts unordered 
      n = len(unordered)         # Get number of items
      self.__work = []     # A work array of the same length
      self.mergesort(0, n)       # Call recursive sort on full array

   def getArray(self):
      return self.__arr

   def mergesort(self, lo, hi):
      if hi - lo > 1:  # Check if more than 1 element
         mid = (hi + lo) // 2  # Find the midpoint
         self.mergesort(lo, mid)  # Sort the first half
         self.mergesort(mid, hi)  # Sort the second half
         self.merge(lo, mid, hi)  # Merge the two halves


   def merge(self, lo, mid, hi): # Merge 2 sorted subranges of array
      n = 0                      # into work array which starts empty
      idxLo = lo                 # Use indices into lo and hi
      idxHi = mid                # subranges to track next items
      while (idxLo < mid and     # Loop until one of the subranges
             idxHi < hi):        # is empty
         itemLo = self.__arr[idxLo] # Get next items from the
         itemHi = self.__arr[idxHi] # two subranges
         if (itemLo <=  itemHi):
            self.__work.insert(n,itemLo) # Lo subrange is first so
            idxLo += 1           # copy item and advance to next
         else:
            self.__work.insert(n,itemHi)# Hi subrange is first so
            idxHi += 1           # copy item and advance to next
         n += 1                  # One more item now in work array

      while idxLo < mid:         # Loop to copy remaining lo 
         self.__work[n]= self.__arr[idxLo]
         idxLo += 1
         n += 1

      while n > 0:               # Copy sorted work array contents
         n -= 1  
         self.__arr[lo + n] = self.__work[n]

def main():
   test_mergesort.test_sort()
   test_mergesort.test_sort2()
   test_mergesort.test_sort3()


if __name__ == '__main__':
   main()
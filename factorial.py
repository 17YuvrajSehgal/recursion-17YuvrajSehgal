# Compute factorial numbers
import test_fact


def factorial(n):
   ## ADD YOUR CODE HERE
   if n==1 or n==0:
      return 1
   return n*factorial(n-1)

def main():
   test_fact.test_fact()
   test_fact.test_fact1()
   test_fact.test_fact3()


if __name__ == '__main__':
    main()
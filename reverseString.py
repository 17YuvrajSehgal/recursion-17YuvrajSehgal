import test_reverseString


def reverse(string):
    '''reverse a string using recursion'''
    ## ADD YOUR CODE HERE
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:])+string[0]

def main():
    test_reverseString.test_reverse()
if __name__ == '__main__':
    main()
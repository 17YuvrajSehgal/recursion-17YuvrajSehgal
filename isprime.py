import test_isprime


def isPrime(n, divisor = 2):
    ## ADD YOUR CODE HERE
    if n==divisor:
        return True

    elif n%divisor==0:
        return False

    return isPrime(n,divisor+1)

def main():
    test_isprime.test_isPrime()
    test_isprime.test_isPrime2()
    test_isprime.test_isPrime3()


if __name__ == '__main__':
    main()
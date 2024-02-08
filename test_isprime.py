import isprime as ip

def test_isPrime():
    n = 10
    assert ip.isPrime(n) == False

def test_isPrime2():
    n = 123
    assert ip.isPrime(n) == False
    
def test_isPrime3():
    n = 17
    assert ip.isPrime(n) == True

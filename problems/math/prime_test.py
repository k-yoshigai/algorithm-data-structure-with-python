import prime


def test_generate_primes():
    assert prime.generate_primes(2) == [2]
    assert prime.generate_primes(5) == [2, 3, 5]


def test_is_prime():
    assert prime.is_prime(0) == False
    assert prime.is_prime(1) == False
    assert prime.is_prime(2) == True
    assert prime.is_prime(3) == True
    assert prime.is_prime(4) == False

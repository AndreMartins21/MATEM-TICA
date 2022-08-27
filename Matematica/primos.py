def get_all_prime_numbers_to(num: int) -> list:
    print(f"Todos os números primos de 2 a {num}: ")
    primes = list(
        filter(lambda x: all(x%y != 0 for y in range(2, x)), range(2, num))
    )
    print(primes)
    return primes

get_all_prime_numbers_to(100)
def prime_number_checker(number):
    first_primes = [1, 2, 3]

    if number <= 0:
        return print('The number has to be higher than 0')
    elif number in first_primes:
        return print(f'{number} is a prime number.')

    max_number_to_test = round(number/2) + 1

    for i in range(max_number_to_test)[2::]:
        if number % i != 0:
            continue
        else:
            return print(f'{number} is not a prime number.')
    return print(f'{number} is a prime number.')





number_t = int(input("Type the number. "))
prime_number_checker(number_t)

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def main():
    number = int(input())
    prime_number = check_prime(number)
    if prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
main()
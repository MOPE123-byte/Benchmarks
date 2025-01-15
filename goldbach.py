# Name: Mohmmad Parvez
# Collaborators: Looking up how to define a function, and except statement
# Notes: 

from sympy import isprime

print('Welcome to the Goldbach\'s Conjecture tester.')


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 ) + 1 ):
        if num % i == 0:
            return False
    return True

def find_goldbach_conjecture(even_num):
    if even_num <= 2 or even_num % 2 != 0:
        return None  

    for i in range(2, even_num // 2 + 1):
        if is_prime(i) and is_prime(even_num - i):
            return i, even_num - i
    return None  

while True:
    try:
        even_num = int(input("Enter an even number greater than 2: "))
        if even_num > 2 and even_num % 2 == 0:
            break
        else:
            print("Invalid input. You need to follow simple directions.")  #Challenge code
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        

primes = find_goldbach_conjecture(even_num)
if primes:
    print(f"The two prime numbers that add up to {even_num} are: {primes[0]} and {primes[1]}")
else:
    print("No such pair of prime numbers found.")
    print("This is a counterexample to Goldbach's conjecture.") #Challenge code
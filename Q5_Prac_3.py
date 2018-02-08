# q5_determine_prime.py

n = int(input("Enter number for prime verification: "))

d = 2
while d <= n:
    if n % d != 0:
        d = d + 1
    elif d == n:
        print(n, "is a prime number. Please try again.")
        break
    else:
        print(n, "is not a prime number. Please try again.")
        break
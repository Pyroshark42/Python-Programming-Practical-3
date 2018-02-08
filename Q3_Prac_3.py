# q3_find_gcd.py

def gcd(x, y):

    d = 2
    total = 1

    while d <= x and d <= y:
        if x % d == 0 and y % d == 0:
            total = total * d
            x = x / d
            y = y / d
        else:
            d = d + 1

    print(total)
    
print(gcd(24,16))
print(gcd(255,25))

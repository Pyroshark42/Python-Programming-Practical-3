#  q1_display_reverse.py

n = int(input("Enter desired number: "))
r = 0
while(n > 0):
    left = n %10
    r = (r *10) + left
    n = n //10
print("The number reversed is: %d" %r)
# q4_sum_series.py

def m(i):
    sum = 0
    for x in range(1,i):
        sum += x / (x + 1)
    return sum
def output(i):
    print("x\t\tm(x)")
    for x in range(1,i):
        print("{0}\t\t{1:.4f}".format(x - 1,m(x)))

n = int(input("Enter number of rows needed: "))
output(n)
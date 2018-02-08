# q7_convert_ms.py
n = int(input("Enter number of milliseconds to convert: "))

while n > 0:
    if n >= 1000:
        n1 = n - (n % 1000)
        sec = n1 / 1000
        break
    else:
        break

while sec > 0:
    if sec >= 60:
        sec1 = sec - (sec % 60)
        minute = sec1 / 60
        break
    else:
        break
while minute > 0:
    if minute >= 60:
        minute1 = minute - (minute % 60)
        hour = minute1 / 60
        break
    else:
        break

print (hour, ':', minute, ':', sec, sep='')
    
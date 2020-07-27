hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <=40:
    print(h*r)
else:
    extra_hours = h - 40
    extra_pay = extra_hours * r * 1.5
    total = (40 * r) + extra_pay
    print(total)

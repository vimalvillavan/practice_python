hrs = input("Enter hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("hours and rate should be numbers, please try running the program again")
    quit()

def computepay(h,r):
    if h <=40:
        return(h*r)
    else:
        extra_hours = h - 40
        extra_pay = extra_hours * r * 1.5
        total = (40 * r) + extra_pay
        return(total)

pay = computepay(h,r)
print ("Pay", pay)
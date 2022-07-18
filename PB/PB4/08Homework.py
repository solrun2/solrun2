import math
min_before_due = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
Rain = input("Is it raining (y/n)? ")
day_before_due = round(min_before_due / (60*24))
if day_before_due == 0 :
    print(">>> a half day before due")
    print(">>> I will do the assignment.")
elif day_before_due < 2 :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will do the assignment.")
elif day_before_due > 5 :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will not do the assignment.")
elif temp > 40 or (temp > 25 and (Rain=="Y" or Rain == "y")) :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will not do the assignment.")
else :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will do the assignment.")
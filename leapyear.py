year = int(input("Enter a Year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("%d is a Leap Year" %year)
        else:
            print("%d is not a Leap Year" %year)
    else:
        print("%d is a Leap Year" %year)
else:
    print("%d is not a Leap Year" %year)
            

    
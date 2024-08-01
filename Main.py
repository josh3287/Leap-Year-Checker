print("This is a leap year checker")
year = int(input("Enter a year: "))
def is_leap_year():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Yes", year, "is a Leap Year")
            else:
                print(year, "is not a Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")

is_leap_year()
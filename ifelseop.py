# a program to determine the driving eligibility by age
print("DRIVER AGE VERIFICATION")
print("...............................")
a= int(input("Enter the age of the driver (7 years to 100 years):" ))

if a>18 and a<=100:
    print("\nYou are eligible to drive")
elif a>=7 and a<18:
    print("\nYou are not eligible to drive")
elif a==18:
    print("\nPhysical Verification is required")
else:
    print("\nInvalid Age.....Please Enter age within the range")
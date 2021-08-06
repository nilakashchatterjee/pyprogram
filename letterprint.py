# ass6
# Printing first and last two letters of the given string
def letter(ltr):
    if len(ltr)<4:
        print("Enter a string with minimum 4 characters")
    elif len(ltr)==4:
        print(ltr)
    else:
        print(ltr[:2] + ltr[-2:])
a = input("Enter a string:")
letter(a)

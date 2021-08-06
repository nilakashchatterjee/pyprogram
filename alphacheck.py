#here we will check the input in alphabet or not
char = input("Enter a character: ") #taking user input

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') :
    print("It is an alphabet")
else:
    print("It is not an alphabet")
# here in this program we are encrypting the string by adding 5 to ascii value of every character
message = input("Enter a message: ")
encrypted= ""
for i in message:
    if i.isupper():
        # This condition is used, so that the ascii value is within 26 alphabets only.
        # Z = 90, cipher = 95 i.e. -> /, and we want alphabets 
        if ord(i) +5 > ord("Z"): 
            encrypted += chr(ord(i) + 5 - 26)
        else:
            encrypted += chr(ord(i) + 5)
    elif i.islower():
        if ord(i) +5 > ord("z") :
            encrypted += chr(ord(i) + 5 - 26)
        else:
            encrypted += chr(ord(i) + 5)
    elif i == " ":
        encrypted += " "

print("The Encrypted messege is:",encrypted)

decrypted =""
for i in encrypted:
    if i.isupper():
        # This condition is used, so that the ascii value is within 26 alphabets only.
        # Z = 90, cipher = 95 i.e. -> /, and we want alphabets 
        if ord(i) - 5 < ord("A"): 
            decrypted += chr(ord(i) - 5 + 26)
        else:
            decrypted += chr(ord(i) - 5)
    elif i.islower():
        if ord(i) - 5 < ord("a") :
            decrypted += chr(ord(i) - 5 + 26)
        else:
            decrypted += chr(ord(i) - 5)
    elif i == " ":
        decrypted += " "

print("The Decrypted messege is:",decrypted)
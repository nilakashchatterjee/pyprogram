#this program is to convert temperature from fahrenheit to celsius and vice versa
print("Enter your choice of conversion\n1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit ")
ch= input("\nYour choice:")
if ch=='1':
    temp = float(input("Enter the temperature in fahrenheit: "))
    print(f"Entered temperature: {temp}ºF")
    cel = (temp-32)*(5/9) #coversion of fahrenheit to celsius

    print("The temperature in celsius is %0.1fºC " %cel)
elif ch=='2':
    temp = float(input("Enter the temperature in celsius: "))
    print(f"Entered temperature: {temp}ºC")
    fah = (temp* 9/5) + 32 #coversion of celsius to fahrenheit

    print("The temperature in fahrenheit is %0.1fºF " %fah)
else:
    print("Enter a valid choice!!!!")
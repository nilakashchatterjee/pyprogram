# Python program to handle "list assignment index out of range" exception along with a "finally" block.
try:
    lst=[10,12,14,34,45]
    print(lst[5])
except IndexError:
    print("INDEX ERROR \nList index out of range")
finally:
    print("\nExecution of the final block")


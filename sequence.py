#ass6 
def sequence(k):
    n=0
    print("The sequence terms are:", end="")
    while k!=-1:
        x = n**2 + 1
        n+=1
        k-=1
        print(x,end=" ")
    
a = int(input("Enter the number of terms:"))
sequence(a)

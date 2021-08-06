class revword:
    def __init__(self,str1):
        self.str1 = str1
    
    def rev(self):
        self.str2= self.str1[::-1]
        return self.str2

s = input("Enter a string:")
sr = revword(s)
print("The reversed word is:",sr.rev())
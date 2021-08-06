#create a dictionary and taking input from user and returning the meaning of the word
#It will be a 5 words dictionary
print("Welcome To The Dictionary\n")

sample = {  "important":"Having great value or influence; very necessary",
            "crossover":"A point or place of crossing from one side to the other",
            "nemesis":"A punishment or defeat that somebody deserves and cannot avoid",
            "tutorial":"A lesson at a college or university for an individual student or a small group of students",
            "faith":"A strong belief or trust"
        }
print("Enter the word to be searched: ",end="")
search=input()
print("The meaning the of above word is: \n")
print(sample[search])
print("\nThank you for using the dictionary :D") 
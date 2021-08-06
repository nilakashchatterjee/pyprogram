# import os

# def find_files(filename, search_path):
#    result = []

#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#    return result

# print(find_files("rudra.png","/"))
import os


counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = input("What are you looking for?:> ")
thisdir = os.getcwd()
for r, d, f in os.walk("/"): # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
        	counter += 1
        	print(file, os.path.join(r))

print(f"Total {counter} files.")
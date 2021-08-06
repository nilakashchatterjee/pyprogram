import os

def searchfiles(extension, folder):
    with open("file.txt", "w") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    filewrite.write(f"{file} ->-> {r + file}\n")

searchfiles('.pdf', '/')
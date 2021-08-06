#program and practice dictionary functions 

d = {"nilakash":"xiaomi", "arun":"samsung", "ashish":"realme", "rohan":{2001:"apple", 2009:"motorola", 2015:"sony", 2020:"lg"}}
print(d["rohan"])
print(d["rohan"][2015])
d["pritam"] = "Micromax"
print(d)
del d["pritam"]
print(d)

d1= d.copy() #if copy function is not used then original dictionary is also affected
del d1["rohan"]
print(d1)

d1.update({"Roy":"Vivo"})
print(d1)

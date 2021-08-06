# import pandas as pd
l = [('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)]
# df = pd.DataFrame(l, columns=['city', 'rainfall'])

# output = []
# for c in df['city'].unique():
#     output += [(c, df[df['city'] == c]['rainfall'].mean())]

# print(output)
# l = [(1,2),(1,3),(2,3),(1,1),(3,8)]
l1 = []
i=0; j=0
while i < len(l):
    city = l[i][0]
    rain = l[i][1]
    # print(city)
    j  = i + 1
    c = 1
    while j < len(l):
        if city == l[j][0]:
            rain += l[j][1]
            c += 1
            l.pop(j)
        else:
            j += 1
    rain = rain/c
    l1.append((city, rain))
    i += 1
print(l1)
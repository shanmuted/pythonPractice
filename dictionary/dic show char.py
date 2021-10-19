a=[[1,["ocean","study","case"]],[2,["xx","yy"]]]
b={}
for i in range(len(a)-1):
    for j in a:
     b.update({j[i]:j[i+1]})
for j[i],j[i+1] in b.items():
        print(j[i+1])

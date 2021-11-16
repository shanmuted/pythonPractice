
g=[31,2,3,65,4]
for i in range(2,10):
  a= list(filter(lambda x:  ((x==i or x%i) and x!=1 ) ,g))
print(a)

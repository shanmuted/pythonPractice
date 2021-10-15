n="pYnative29@8496"
summ=0
count=0
for i in  n:
    if (i.isnumeric()):
      i=int(i)
      count+=1
      summ=summ+i
      #print(summ)
avg=summ/count
print(avg)

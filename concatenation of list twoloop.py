list1=["helo","hi"]
list2=["dear","sir","mam"]
newlist=[]
for i in range (len(list1)):
     for j in range(len(list2)):
         
        element=list1[i]+list2[j]
        newlist.append(element)
print(newlist)

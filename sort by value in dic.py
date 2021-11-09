dic={'a':"hello",'b':"1",'c':"jayalatha",'d':[1,2]}
x=dic.values()
a=list(x)
newdic={}
a.sort(key=len)
#print(a)
for i in a:
     for j,k in dic.items():
         if(i==k):
             newdic.update({j:i})
print(newdic)






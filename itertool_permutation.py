'''from itertools import permutations as pt
lt=[1,2,3]
x=list(pt(lt))
print(x)'''
from itertools import*
lt=[1,2,3]
x=list(permutations(lt))
print(x)
y=list(combinations(lt,2))
print(y)
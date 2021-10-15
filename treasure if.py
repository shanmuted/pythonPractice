a=input("left or right")
if(a=='right'):
  b=input("swim or wait")
  if(b=='swim'):
    c=input("yellow or other")
    if(c=='yellow'):
     print("win")
    else:
     print("loss")
  else:
    print("game over")
else:
    print("game over")

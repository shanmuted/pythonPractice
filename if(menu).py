a=input("veg or non veg?:\n")
if(a=='veg'):
  b=input("breakfast or lunch or dinner?:\n")
  if(b=='breakfast'):
    print("idly\n""dosa\n""pongal\n")
    c=input("yes:")
    if(c=='idly'):
         print("idly is available")
    elif(c=='dosa'):
         print("dosa is available")
    elif(c=='pongal'):
          print("pongal is available")
  elif(b=='lunch'):
    print("sambar\n""curd\n""lemon\n")
    d=input("yes:")
    if(d=='sambar'):
     print("sambar is available")
    elif(d=='curd'):
     print("curd is availablr")
    elif(d=='lemon'):
     print("lemon is available")
  elif(b=='dinner'):
    print("chapathi\n""dosa\n""poori\n")
    e=input("yes:")
    if(e=='chapathi'):
      print("chapathi is available")
    elif(e=='dosa'):
      print("dosa is available")
    elif(e=='poori'):
      print("poori is available")
    
elif(a=='non veg'):
    f=input("seafood or fastfood")
    if(f=='seafood'):
     print("fishcurr\n""briyani\n")
     g=input("yes:")
     if(g=='fishcurry'):
       print("fishcurry is available")
     elif(g=='briyani'):
       print("briyani is available")
    elif(f=='fastfood'):
     print("friedrice\n""parotta\n")
     h=input("yes:")
     if(h=='friedrice'):
        print("friedrice is available")
     elif(h=='parotta'):
        print("parotta is available")
        
else:
  print("out of stack")
      
      

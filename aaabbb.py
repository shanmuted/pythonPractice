series=input("enter the series:")
for i in range(0,len(series)-1,2):
    print(i,end= '')
    if(series[i].isalpha()):
        print(series[i]*int(series[i+1]),end = '')
    else:
        print(int(series[i]) * series[i+1],end='')
    
     

temp=int(input("enter the temperature"))
if temp<15:
    print("Given temperature is cold")
elif temp in range(15,25):
    print("Given temperature is warm")
else :
    print("Given temperature is hot")        


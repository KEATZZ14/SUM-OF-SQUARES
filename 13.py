n=int(input(""))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig**2
    n=n//10
print("The total sum of digits is:",tot)

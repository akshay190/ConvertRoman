def convertRoman(n):
    f19=['','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIV']
    s20=['','X','XX','XXX','XL','L',"LX",'LXX','LXXX','XC','C']
    t30=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']
    f40=['','M','MM','MMM','MV','V','VM','VMM','VMMM','MX','X']
    if(n<=19):
        print(f19[n])
    elif(n<=100):
        print(s20[n//10]+f19[n%10])
    elif(n<1000):
        print(t30[n//100]+s20[(n//10)%10]+f19[n%10])
    elif(n==1000):
        print("M")
    elif(n<=10000):
        print(f40[n//1000]+t30[(n//100)%10]+s20[(n//10)%10]+f19[n%10])

convertRoman(int(input("Enter A Number To Convert In Roman Number ")))

def most_frequent(a,l):
    di={}
    for lp in range(l):
        if(a[lp] in di):
            di[a[lp]]+=1
        else:
            di[a[lp]]=1
    si=len(di)
    print("The frequency in dercreasing order is : ")
    while(si>0):
        ma,a_ma=0,0
        for key,val in di.items():
            if (val>ma or(val==ma and key>a_ma)):
                a_ma,ma=key,val
        #print(a_ma,"-",ma)
        di.pop(a_ma)
        print(a_ma,"-",ma)
        
str=input("Enter a string :")
l=len(str)
a=list(str)
most_frequent(a,l)

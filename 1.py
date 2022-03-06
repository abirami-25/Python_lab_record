start_yr=int(input("Enter starting year : "))
end_yr=int(input("Enter ending year : "))
print ("leap years are : ")
for i in range(start_yr,end_yr):
    if ((i%4==0 and i%100!=0) or i%400==0):
        print (i)
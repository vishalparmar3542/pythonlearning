bikeprice=float(input("Enter Cost price of Bike: "))
tax=0
if bikeprice<=50000 :
    tax=5/100 * bikeprice
elif bikeprice<=100000:
    tax=2500 + (bikeprice-50000)*10/100
elif bikeprice>100000:
    tax=2500 + 5000+ ((bikeprice-100000) *15/100)

print("tax amount {}".format(tax))
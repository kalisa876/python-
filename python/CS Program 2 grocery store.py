item1 = int(input("Please enter the price of your first item: "))
item2 = int(input("Please enter the price of your second item: "))
item3 = int(input("Please enter the price of your third item: "))
price = int (input("Please enter the amount you are paying for your three items: "))
payment = (item1 + item2 + item3)
owe = (payment - price)
change = (price - payment)
if (price < payment):
    print ("You still owe" ,owe)
else:
    print("Thank you for your payment, your change will be" ,change)

def moneyA():
    enter_Money = int(input("How much money do you have: "))
    return enter_Money

def appleP():
    apple_Price = int(input("Enter the price of the apple: "))
    return apple_Price

def appleT(money, price):
    apple_Total = int(money//price)
    return apple_Total

def leftM(money, price):
    money_Left = money%price
    return money_Left

amount_Money = moneyA()
price_Apple = appleP()
total_Apple = appleT(amount_Money, price_Apple)
left_Money = float (leftM(amount_Money, price_Apple))
print(f"You can buy {total_Apple} apples and your change is {left_Money} pesos.")
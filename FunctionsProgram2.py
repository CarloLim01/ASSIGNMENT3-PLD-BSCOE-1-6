
def appleQ():
    apple_Question = int(input("How many apples do you want to buy? "))
    return apple_Question

def orangeQ():
    orange_Question = int(input("How many oranges do you want to buy? "))
    return orange_Question

def price(apple_Number, orange_Number):
    apple_Price = apple_Number * 20
    orange_Price = orange_Number * 25
    total = apple_Price + orange_Price
    return total 

apples = appleQ()
oranges = orangeQ()
total = price(apples, oranges)

print(f"The total amount is {total}")
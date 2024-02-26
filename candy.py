# creates a list called candies
candies = ["CADBURY Mini Eggs 10 oz", "DOVE Assorted Easter Candy Chocolate Spring Mix 22.6 oz", "Reese's Easter Chocolate Peanut Butter Creme Eggs Candy14.4 Oz", "STARBURST Original Jelly Beans Easter Candy"]
# creates a list of prices for the candies in the candies list
price = ["3 ", 12, "9 ", "6 "]
# list of items that the person wants to buy 
cart = []
# list of how much they pay for the items
pay = []
# asks the user for the amount of money they can spend on candy
# then it converts it an int and saves it in the variable money
money = int(input("How much money can you spend on candy? $"))

def Buy():
    item = int(input("What would you like to buy? "))
    buy = item - 1
    amount = int(input("How many would you like to buy?"))
    cart.append(candies[buy] + "  " + str(amount))
    cost = int(price[buy]) * amount
    pay.append(int(cost))
    R = input("Would you like anything else? ")
    if (R == "Y"):
        ListOfCandies()
        Buy()
    elif (R == "y"):
        ListOfCandies()
        Buy()
    elif (R == "Yes"):
        ListOfCandies()
        Buy()
    elif (R == "yes"):
        ListOfCandies()
        Buy()
    else:
        Buying()
def ListOfCandies():
    print()
    print("List of candies: ")
    print ()
    for i in range (0, 4):
        print (i + 1, "Price: " + str(price[i]),"Name: " + str(candies[i]))
def Buying():
    print("")
    print(cart)
    print("")
    total = int(sum(pay))
    print("Your total is: $" + str(total))
    if (money >= total):
        print("You have enough money to pay")
    else:
        print("You do not have enough money to pay")


ListOfCandies()
Buy()
print("")
input("Press enter to exit")
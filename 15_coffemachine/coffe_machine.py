from data_cm import MENU

class CoffeeMachine:
    def __init__(self):
        self.water = 800  # ml
        self.milk = 200  # ml
        self.coffee = 100  # g
        self.money = 0  # $
        self.on = True  # info if coffee machine is on or off

    # main prompt of coffee machine
    def promptCoffee(self):
        while self.on:
            coffeeType = input("What would you like? (espresso / latte / cappuccino): ").lower()
            if coffeeType == "espresso" or coffeeType == "latte" or coffeeType == "cappuccino":
                self.makeCoffee(coffeeType)
            elif coffeeType == "report":
                # leaves a report how many resources coffee machine still has
                print(f"Water: {self.water}")
                print(f"Milk: {self.milk}")
                print(f"Coffee: {self.coffee}")
                print(f"Money: {self.money}")
            elif coffeeType == "off":
                # switch off coffee machine
                self.on = False
                break
            else:
                # if command is not valid, tries again
                print("Invalid command.")
                continue

    # makes coffee
    def makeCoffee(self, what_coffee):
        # finds in menu how many ingredients are needed and cost of called coffee
        water = MENU[what_coffee]["ingredients"]["water"]
        milk = MENU[what_coffee]["ingredients"]["milk"]
        coffee = MENU[what_coffee]["ingredients"]["coffee"]
        cost = MENU[what_coffee]["cost"]

        # checks if there is enough resources
        if self.water - water < 0:
            print("Sorry, there is not enough water.")
        elif self.milk - milk < 0:
            print("Sorry, there is not enough milk.")
        elif self.coffee - coffee < 0:
            print("Sorry, there is not enough coffee.")
        # if there is enough resources to make a coffee, ask for money
        elif self.water - water >= 0 and self.milk - milk >= 0 and self.coffee - coffee >= 0:
            print("Insert how many coins do you have?")
            try:
                quarters = int(input("How many quarters do you have? "))
                dimes = int(input("How many dimes do you have? "))
                nickles = int(input("How many nickles do you have? "))
                pennies = int(input("How many pennies do you have? "))
            except:
                print("Invalid command. Trying again.")
                self.promptCoffee()
            money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            self.money += money
            # if change is not needed just make a coffee
            if money == cost:
                self.water -= water
                self.milk -= milk
                self.coffee -= coffee
                print(f"Here is your {what_coffee}. Enjoy!")
            # if customer gave more money than needed, offer a change
            elif money > cost:
                change = 0
                # round is workaround when subtracting float from int
                change_left = round(money - cost, 2)
                while change_left > 0.25 and quarters > 0:
                    change_left = round(change_left - 0.25, 2)
                    change = round(change + 0.25, 2)
                    quarters -= 1
                while change_left > 0.1 and dimes > 0:
                    change_left = round(change_left - 0.1, 2)
                    change = round(change + 0.1, 2)
                    dimes -= 1
                while change_left > 0.05 and nickles > 0:
                    change_left = round(change_left - 0.05, 2)
                    change = round(change + 0.05, 2)
                    nickles -= 1
                while change_left > 0.00 and pennies != 0:
                    change_left = round(change_left - 0.01, 2)
                    change = round(change + 0.01, 2)
                    pennies -= 1
                if change_left == 0:
                    print(f"Your change is {change}$.")
                else:
                    print(f"There are missing coins for full change. Your change is {change}$ and"
                          f" with missing {change_left - change}$.")
                self.water -= water
                self.milk -= milk
                self.coffee -= coffee
                self.money -= change
                self.money = round(self.money, 2)
                print(f"Here is your {what_coffee}. Enjoy!")
            # if not enough money, inform the customer and give money back
            elif money < cost:
                print("Sorry, that's not enough money. Money refunded.")
                self.money -= money

cm = CoffeeMachine()
cm.promptCoffee()



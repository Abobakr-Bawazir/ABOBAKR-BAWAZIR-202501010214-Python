# Function to calculate the total bill

def calculate_total(coffee, tea, sandwich):
    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00

    coffee_cost = coffee * coffee_price
    tea_cost = tea * tea_price
    sandwich_cost = sandwich * sandwich_price

    total = coffee_cost + tea_cost + sandwich_cost

    return total


# Function to print customer receipt

def print_receipt(name, coffee, tea, sandwich, total):

    print("\n===== RECEIPT =====")

    print("Customer :", name)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)

    print("-------------------")

    print("Total = RM {:.2f}".format(total))# Function to calculate the total bill


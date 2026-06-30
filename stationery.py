# Define stationery items with prices
stationery = {
    'Notebook': 80,
    'Pen': 20,
    'Pencil': 10,
    'Eraser': 5,
    'Scale': 15,
    'Marker': 50
}

# Greet
print("Welcome to Shivakanya Stationery Store")

customer_name = input("Enter customer name: ")

print("\nAvailable Items:")
print("Notebook: Rs80\nPen: Rs20\nPencil: Rs10\nEraser: Rs5\nScale: Rs15\nMarker: Rs50")

total_bill = 0

while True:
    item = input("\nEnter stationery item you want to buy = ")

    if item in stationery:
        quantity = int(input(f"Enter quantity for {item}: "))
        total_bill += stationery[item] * quantity
        print(f"{item} x {quantity} added to your bill")

    else:
        print(f"{item} is not available!")

    another = input("Do you want to add another item? (Yes/No): ")

    if another == "No":
        break

print(f"\nThank you, {customer_name}!")
print(f"Your total stationery bill is Rs {total_bill}")
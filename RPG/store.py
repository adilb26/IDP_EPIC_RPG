from utils import item_emojis

def store(user):
    print("\n--------------------------------------------------")
    items = {
        "1": ("Wooden Sword", 100),
        "2": ("Iron Sword", 300),
        "3": ("Basic Armour", 200),
        "4": ("Steel Armour", 400),
        "5": ("Life Potion", 20),
    }
    print("Store:")
    print(f"💰 Coins: {user['coin']}")
    for num, (item, cost) in items.items():
        print(f"{num}. {item_emojis[item]} {item}: {cost} coins")

    print("--------------------------------------------------")

    choice = input("Enter item number to buy: ").strip()
    if choice not in items:
        print("Invalid choice.")
        return

    item, cost = items[choice]

    if item == "Life Potion":
        quantity = int(input("Enter quantity: "))
        total_cost = cost * quantity

        if user["coin"] < total_cost:
            print("Insufficient coins.")
            return

        user["coin"] -= total_cost
        user["inventory"][item] = user["inventory"].get(item, 0) + quantity
        print(f"Bought {quantity} Life Potions.")
        return

    if user["coin"] < cost:
        print("Insufficient coins.")
        return

    user["coin"] -= cost
    user["inventory"][item] = user["inventory"].get(item, 0) + 1
    print(f"Bought {item}.")

    if item == "Wooden Sword":
        user["weapon"] = item
        user["attack"] = 12
        print("🗡️ Wooden Sword equipped! Attack increased.")

    elif item == "Iron Sword":
        user["weapon"] = item
        user["attack"] = 18
        print("⚔️ Iron Sword equipped! Attack increased.")

    elif item == "Basic Armour":
        user["armour"] = item
        user["defense"] = 8
        print("🛡️ Basic Armour equipped! Defense increased.")

    elif item == "Steel Armour":
        user["armour"] = item
        user["defense"] = 12
        print("🛡️ Steel Armour equipped! Defense increased.")
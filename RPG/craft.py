def craft(user):
    print("\n--------------------------------------------------")
    print("Crafting:")
    print("1. Wooden Sword (needs 5 🪵 Oak Logs)")
    print("2. Lucky Charm (needs 3 💎 Small Gems)")
    print("3. Exit")
    print("--------------------------------------------------")

    choice = input("Enter craft option: ").strip()

    if choice == "1":
        if user["inventory"].get("🪵 Oak Log", 0) < 5:
            print("Insufficient wood logs.")
            return

        user["inventory"]["🪵 Oak Log"] -= 5
        user["inventory"]["Wooden Sword"] = user["inventory"].get("Wooden Sword", 0) + 1
        user["weapon"] = "Wooden Sword"
        user["attack"] = 12
        print("🗡️ Crafted Wooden Sword! Attack increased.")

    elif choice == "2":
        if user["inventory"].get("Small Gem", 0) < 3:
            print("Insufficient gems.")
            return

        user["inventory"]["Small Gem"] -= 3
        user["inventory"]["Lucky Charm"] = user["inventory"].get("Lucky Charm", 0) + 1
        user["luck"] += 10
        print("✨ Crafted Lucky Charm! Luck increased.")

    else:
        print("Exiting crafting.")

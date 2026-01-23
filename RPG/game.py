import time
from user import load_user_data, save_user_data, register, login, delete_user
from combat import rpg_hunt, rpg_adventure, rpg_chop, reward
from inventory import view_inventory
from profile import view_profile
from store import store
from craft import craft
from utils import get_level, item_emojis

def start_game():
    user = None
    while user is None:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        choice = input("Enter your choice: ")
        if choice == '1':
            user = register()
        elif choice == '2':
            user = login()
        else:
            print("Invalid choice. Please enter 1 or 2.")

    users = load_user_data()
    current_user = users[user]
    current_user['username'] = user

    last_hunt_time = 0
    last_adventure_time = 0
    last_chop_time = 0
    last_reward_time = 0
    last_craft_time = 0

    while True:
        print("\nMenu:")
        print("1. 🎯 Hunt")
        print("2. 🗺️ Adventure")
        print("3. 🧪 Heal using Life Potion")
        print("4. 🎒 View Inventory")
        print("5. 👤 View Profile")
        print("6. 🏪 Store")
        print("7. 🪵 Chop Wood")
        print("8. 🎁 Reward")
        print("9. 🛠️ Craft")
        print("10. 🗑️ Delete User")
        print("11. 🚪 Exit")
        choice = input("Enter your choice: ")

        current_time = time.time()

        if choice == '1':
            if current_time - last_hunt_time < 10:
                print("You need to wait before hunting again.")
                continue
            level = get_level(current_user['xp'])
            if current_user['health'] > 0:
                rpg_hunt(level, current_user)
                if current_user['health'] <= 0:
                    print("You have no health left. Game over.")
                    break
                save_user_data(users)
                last_hunt_time = current_time
        elif choice == '2':
            if current_time - last_adventure_time < 30:
                print("You need to wait before going on an adventure again.")
                continue
            level = get_level(current_user['xp'])
            if current_user['health'] > 0:
                rpg_adventure(level, current_user)
                save_user_data(users)
                last_adventure_time = current_time
            else:
                print("You don't have enough health for an adventure.")
        elif choice == '3':
            if current_user['health'] == current_user['total_health']:
                print("You already have full health. You cannot use the Life Potion.")
            elif 'Life Potion' in current_user['inventory'] and current_user['inventory']['Life Potion'] > 0:
                current_user['health'] = current_user['total_health']
                current_user['inventory']['Life Potion'] -= 1
                print("You have been healed to full health.")
                save_user_data(users)
            else:
                print("You don't have any Life Potions.")
        elif choice == '4':
            view_inventory(current_user)
        elif choice == '5':
            view_profile(current_user)
        elif choice == '6':
            store(current_user)
            save_user_data(users)
        elif choice == '7':
            if current_time - last_chop_time < 0:
                print("You need to wait before chopping wood again.")
                continue
            rpg_chop(current_user)
            save_user_data(users)
            last_chop_time = current_time
        elif choice == '8':
            if current_time - last_reward_time < 20:
                print("You need to wait before claiming the reward again.")
                continue
            reward(current_user)
            save_user_data(users)
            last_reward_time = current_time
        elif choice == '9':
            if current_time - last_craft_time < 20:
                print("You need to wait before crafting again.")
                continue
            craft(current_user)
            save_user_data(users)
            last_craft_time = current_time
        elif choice == '10':
            delete_user(user)
            break
        elif choice == '11':
            print("Exiting the game.")
            save_user_data(users)
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        new_level = get_level(current_user['xp'])
        if new_level > current_user['level']:
            increase = (new_level - current_user['level']) * 15  # 15 per level up
            current_user['total_health'] += increase
            current_user['health'] += increase
            current_user['level'] = new_level
            print(f"🎉 You leveled up to Level {new_level}! Your total health increased by {increase}.")
            save_user_data(users)
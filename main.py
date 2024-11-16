def get_item(x):
    if x == 1:
        return '🍔 Cheeseburger'
    elif x == 2:
        return '🍟 Fries'
    elif x == 3:
        return '🥤 Soda'
    elif x == 4:
        return '🍦 Ice Cream'
    elif x == 5:
        return '🍪 Cookie'
    elif x == 6:
        return 'Happy Meal (🍔,🍟,🥤)'
    elif x == 7:
        return '🥗 Caesar Salad'
    else:
        return "Invalid option"

def welcome():
    print("Welcome to the Soda Bottle Opener Wala's diner!!")
    print("Here's your menu options:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")
    print("6. Happy Meal (🍔,🍟,🥤)")
    print("7. 🥗 Caesar Salad")

welcome()
option = int(input('What would you like to order? '))
print(get_item(option))

def main():
    fruit = input("Item: ")
    calorie_check(fruit)


def calorie_check(item):
    item = item.strip().lower().title()
    calorie = calorie_chart()
    if item in calorie:
        print(item)
        print("Calorie:", calorie[item])


def calorie_chart():
    calorie = {
        "Apple":"130",
        "Avocado":"50",
        "Banana":"110",
        "Cantaloupe":"50",
        "Grapefruit":"60",
        "Grapes":"90",
        "Honeydew Melon":"50",
        "Kiwifruit":"90",
        "Lemon":"15",
        "Lime":"20",
        "Nectarine":"60",
        "Orange":"80",
        "Peach":"60",
        "Pear":"100",
        "Pineapple":"50",
        "Plums":"70",
        "Strawberries":"50",
        "Sweet Cherries":"100",
        "Tangerine":"50",
        "Watermelon":"80"
    }
    return calorie
main()
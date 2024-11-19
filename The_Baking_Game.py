//This is a game created for baking and designing a cookie. This was created by MS Copilot by asking for it to create a game designed for baking and designing a cookie while adding in loops, conditons, and functions with some refinements along the way.

def display_baking_menu():
    print("Welcome to the Cookie Baking Game!")
    print("Choose your ingredients to bake the cookie:")
    print("1. Flour")
    print("2. Sugar")
    print("3. Butter")
    print("4. Eggs")
    print("5. Chocolate Chips")
    print("6. Finish baking")

def get_baking_ingredient(choice):
    ingredients = {
        1: "Flour",
        2: "Sugar",
        3: "Butter",
        4: "Eggs",
        5: "Chocolate Chips"
    }
    return ingredients.get(choice, None)

def bake_cookie():
    cookie = []
    while True:
        display_baking_menu()
        choice = int(input("Enter the number of your choice: "))
        if choice == 6:
            break
        ingredient = get_baking_ingredient(choice)
        if ingredient:
            cookie.append(ingredient)
            print(f"{ingredient} added to your cookie.")
        else:
            print("Invalid choice. Please try again.")
    return cookie

def display_design_menu():
    print("Now, let's design your cookie!")
    print("Choose your decorations:")
    print("1. Sprinkles")
    print("2. Icing")
    print("3. Chocolate Drizzle")
    print("4. Nuts")
    print("5. Finish designing")

def get_design_choice(choice):
    designs = {
        1: "Sprinkles",
        2: "Icing",
        3: "Chocolate Drizzle",
        4: "Nuts"
    }
    return designs.get(choice, None)

def design_cookie():
    design = []
    while True:
        display_design_menu()
        choice = int(input("Enter the number of your choice: "))
        if choice == 5:
            break
        decoration = get_design_choice(choice)
        if decoration:
            design.append(decoration)
            print(f"{decoration} added to your cookie.")
        else:
            print("Invalid choice. Please try again.")
    return design

def main():
    print("Let's bake a cookie!")
    cookie = bake_cookie()
    print("\nYour cookie is baked with the following ingredients:")
    for ingredient in cookie:
        print(f"- {ingredient}")

    print("\nLet's design your cookie!")
    design = design_cookie()
    print("\nYour cookie is designed with the following decorations:")
    for decoration in design:
        print(f"- {decoration}")

if __name__ == "__main__":
    main()

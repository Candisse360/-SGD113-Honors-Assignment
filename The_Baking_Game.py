//This is a game created for baking and designing a cookie. This was created by MS Copilot by asking for it to create a game designed for baking and designing a cookie while adding in loops, conditons, and functions with some refinements along the way.

                                                                                                                                                                                             using System;
using System.Collections.Generic;

class Program
{
    static void DisplayBakingMenu()
    {
        Console.WriteLine("Welcome to the Cookie Baking Game!");
        Console.WriteLine("Choose your ingredients to bake the cookie:");
        Console.WriteLine("1. Flour");
        Console.WriteLine("2. Sugar");
        Console.WriteLine("3. Butter");
        Console.WriteLine("4. Eggs");
        Console.WriteLine("5. Chocolate Chips");
        Console.WriteLine("6. Finish baking");
    }

    static string GetBakingIngredient(int choice)
    {
        Dictionary<int, string> ingredients = new Dictionary<int, string>
        {
            { 1, "Flour" },
            { 2, "Sugar" },
            { 3, "Butter" },
            { 4, "Eggs" },
            { 5, "Chocolate Chips" }
        };

        return ingredients.ContainsKey(choice) ? ingredients[choice] : null;
    }

    static List<string> BakeCookie()
    {
        List<string> cookie = new List<string>();
        while (true)
        {
            DisplayBakingMenu();
            int choice = int.Parse(Console.ReadLine());
            if (choice == 6)
                break;

            string ingredient = GetBakingIngredient(choice);
            if (ingredient != null)
            {
                cookie.Add(ingredient);
                Console.WriteLine($"{ingredient} added to your cookie.");
            }
            else
            {
                Console.WriteLine("Invalid choice. Please try again.");
            }
        }
        return cookie;
    }

    static void DisplayDesignMenu()
    {
        Console.WriteLine("Now, let's design your cookie!");
        Console.WriteLine("Choose your decorations:");
        Console.WriteLine("1. Sprinkles");
        Console.WriteLine("2. Icing");
        Console.WriteLine("3. Chocolate Drizzle");
        Console.WriteLine("4. Nuts");
        Console.WriteLine("5. Finish designing");
    }

    static string GetDesignChoice(int choice)
    {
        Dictionary<int, string> designs = new Dictionary<int, string>
        {
            { 1, "Sprinkles" },
            { 2, "Icing" },
            { 3, "Chocolate Drizzle" },
            { 4, "Nuts" }
        };

        return designs.ContainsKey(choice) ? designs[choice] : null;
    }

    static List<string> DesignCookie()
    {
        List<string> design = new List<string>();
        while (true)
        {
            DisplayDesignMenu();
            int choice = int.Parse(Console.ReadLine());
            if (choice == 5)
                break;

            string decoration = GetDesignChoice(choice);
            if (decoration != null)
            {
                design.Add(decoration);
                Console.WriteLine($"{decoration} added to your cookie.");
            }
            else
            {
                Console.WriteLine("Invalid choice. Please try again.");
            }
        }
        return design;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Let's bake a cookie!");
        List<string> cookie = BakeCookie();
        Console.WriteLine("\nYour cookie is baked with the following ingredients:");
        foreach (string ingredient in cookie)
        {
            Console.WriteLine($"- {ingredient}");
        }

        Console.WriteLine("\nLet's design your cookie!");
        List<string> design = DesignCookie();
        Console.WriteLine("\nYour cookie is designed with the following decorations:");
        foreach (string decoration in design)
        {
            Console.WriteLine($"- {decoration}");
        }
    }
}

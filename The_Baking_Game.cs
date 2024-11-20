//This code is for a game designed for baking and decorating a cake. This was created with MS Copilot by asking it to create a simple game in C# then refined with personal preferences. It was test ran in VS Code.

using System;
using System.Collections.Generic;

class BakingGame
{
    static void Main()
    {
        Console.WriteLine("Welcome to the Baking Game!");
        List<string> ingredients = new List<string>();
        HashSet<string> chosenIngredients = new HashSet<string>();

        while (ingredients.Count < 5)
        {
            string choice = ChooseIngredient();
            if (!chosenIngredients.Contains(choice))
            {
                switch (choice)
                {
                    case "1":
                        ingredients.Add("Flour");
                        chosenIngredients.Add("1");
                        break;
                    case "2":
                        ingredients.Add("Sugar");
                        chosenIngredients.Add("2");
                        break;
                    case "3":
                        ingredients.Add("Eggs");
                        chosenIngredients.Add("3");
                        break;
                    case "4":
                        ingredients.Add("Butter");
                        chosenIngredients.Add("4");
                        break;
                    case "5":
                        ingredients.Add("Baking Powder");
                        chosenIngredients.Add("5");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please choose a number between 1 and 5.");
                        break;
                }
            }
            else
            {
                Console.WriteLine("You have already chosen this ingredient. Please choose a different one.");
            }
        }

        string frostingColor = ChooseFrostingColor();
        List<string> decorations = ChooseDecorations();

        BakeCake(ingredients, frostingColor, decorations);
    }

    static string ChooseIngredient()
    {
        Console.WriteLine("Choose an ingredient to add to your cake:");
        Console.WriteLine("1. Flour");
        Console.WriteLine("2. Sugar");
        Console.WriteLine("3. Eggs");
        Console.WriteLine("4. Butter");
        Console.WriteLine("5. Baking Powder");
        Console.Write("Enter the number of your choice: ");
        return Console.ReadLine();
    }

    static string ChooseFrostingColor()
    {
        Console.WriteLine("\nChoose a frosting color for your cake:");
        Console.WriteLine("1. Red");
        Console.WriteLine("2. Blue");
        Console.WriteLine("3. Green");
        Console.WriteLine("4. Yellow");
        Console.WriteLine("5. White");
        Console.Write("Enter the number of your choice: ");
        string choice = Console.ReadLine();

        switch (choice)
        {
            case "1":
                return "Red";
            case "2":
                return "Blue";
            case "3":
                return "Green";
            case "4":
                return "Yellow";
            case "5":
                return "White";
            default:
                Console.WriteLine("Invalid choice. Defaulting to White.");
                return "White";
        }
    }

    static List<string> ChooseDecorations()
    {
        List<string> decorations = new List<string>();
        Console.WriteLine("\nChoose decorations to add to your cake (type 'done' when finished):");
        Console.WriteLine("1. Sprinkles");
        Console.WriteLine("2. Chocolate Chips");
        Console.WriteLine("3. Fruit");
        Console.WriteLine("4. Nuts");
        Console.WriteLine("5. Candies");

        while (true)
        {
            Console.Write("Enter the number of your choice: ");
            string choice = Console.ReadLine();

            if (choice.ToLower() == "done")
            {
                break;
            }

            switch (choice)
            {
                case "1":
                    decorations.Add("Sprinkles");
                    break;
                case "2":
                    decorations.Add("Chocolate Chips");
                    break;
                case "3":
                    decorations.Add("Fruit");
                    break;
                case "4":
                    decorations.Add("Nuts");
                    break;
                case "5":
                    decorations.Add("Candies");
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please choose a number between 1 and 5 or type 'done' to finish.");
                    break;
            }
        }

        return decorations;
    }

    static void BakeCake(List<string> ingredients, string frostingColor, List<string> decorations)
    {
        Console.WriteLine("\nBaking your cake with the following ingredients:");
        foreach (string ingredient in ingredients)
        {
            Console.WriteLine(ingredient);
        }

        Console.WriteLine($"\nFrosting your cake with {frostingColor} frosting.");

        if (decorations.Count > 0)
        {
            Console.WriteLine("\nAdding the following decorations:");
            foreach (string decoration in decorations)
            {
                Console.WriteLine(decoration);
            }
        }
        else
        {
            Console.WriteLine("\nNo decorations added.");
        }

        Console.WriteLine("\nYour cake is ready! Enjoy your delicious creation!");
    }
}

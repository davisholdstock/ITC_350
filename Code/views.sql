-- VIEW Statement for User Shopping Lists
CREATE VIEW myShoppingList AS
SELECT UserID, Username, SLUserID, SLItemID, ItemID, ItemName
FROM ShoppingList
INNER JOIN User ON User.UserID = ShoppingList.SLUserID
INNER JOIN Item ON ShoppingList.SLItemID = Item.ItemID;

-- VIEW Statement for Recipe Search page. Up to date.
CREATE VIEW FindRecipe AS
SELECT ItemID, ItemName, I_ItemID, RecipeID, Category
FROM Ingredient
INNER JOIN Item ON Item.ItemID = Ingredient.I_ItemID
INNER JOIN Recipe ON Ingredient.IRecipeID = Recipe.RecipeID;

-- VIEW Statement for Items based on recipe
CREATE VIEW ItemsForRecipe AS
SELECT RecipeID, Rating, Difficulty, Directions, Duration, Title, Category, Picture, ItemID, ItemName, Count, Units
FROM Recipe
INNER JOIN Ingredient ON Recipe.RecipeID = Ingredient.IRecipeID
INNER JOIN Item ON Ingredient.I_ItemID = Item.ItemID;
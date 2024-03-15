-- VIEW Statement for User Cookbook
CREATE VIEW myCookbook AS 
SELECT UserID, Username, RecipeID, Title, Rating, Difficulty, Duration 
FROM Cookbook 
INNER JOIN User ON User.UserID = Cookbook.CBUserID 
INNER JOIN Recipe ON Cookbook.CBRecipeID = Recipe.RecipeID;

-- VIEW Statement for individual recipes
CREATE VIEW IndividualRecipe AS
SELECT RecipeID, Rating, Difficulty, Directions, Category, Picture, Duration, Title, IngredientID, Count, Units, ItemName
FROM Recipe
INNER JOIN Ingredient ON Recipe.RecipeID = Ingredient.IRecipeID
INNER JOIN ITEM ON Ingredient.IngredientID = Item.ItemID;

-- VIEW Statement for User Shopping Lists
CREATE VIEW myShoppingList AS
SELECT UserID, Username, SLUserID, SLItemID, ItemID, ItemName
FROM Item
INNER JOIN User ON User.UserID = ShoppingList.SLUserID
INNER JOIN Item ON ShoppingList.SLItemID = Item.ItemID;

-- VIEW Statement for User Account information
CREATE VIEW AccountPage AS
SELECT UserID, Username, Password, PUserID, FUserID
FROM Friendship
INNER JOIN User ON User.UserID = Friendship.PUserID;

-- VIEW Statement for Recipe Search page, Do we need this one?
CREATE VIEW FindRecipe AS
SELECT ItemID, ItemName, IngredientID, RecipeID, Category
FROM Ingredient
INNER JOIN Item ON Item.ItemID = Ingredient.IngredientID
INNER JOIN Recipe ON Ingredient.IRecipeID = Recipe.RecipeID;

-- VIEW STATEMENT for All Recipes
CREATE VIEW AllRecipes AS
SELECT RecipeID, Rating, Difficulty, Category, Duration, Picture, Title, IngredientID, ItemName, ItemID
FROM Recipe
INNER JOIN Ingredient ON Recipe.RecipeID = Ingredient.IRecipeID
INNER JOIN Item ON Ingredient.IngredientID = Item.ItemID;

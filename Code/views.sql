-- VIEW Statement for User Cookbook
CREATE VIEW myCookbook AS 
SELECT UserID, Username, RecipeID, Title, Rating, Difficulty, Duration 
FROM Cookbook 
INNER JOIN User ON User.UserID = Cookbook.CBUserID 
INNER JOIN Recipe ON Cookbook.CBRecipeID = Recipe.RecipeID;

-- VIEW Statement for individual recipes
CREATE VIEW IndividualRecipe AS
SELECT RecipeID, Rating, Difficulty, Directions, Duration, Title, IngredientID, Count, Units
FROM Recipe
INNER JOIN Ingredient ON Recipe.RecipeID = Ingredient.RecipeID;

-- VIEW Statement for User Shopping Lists
CREATE VIEW myShoppingList AS
SELECT UserID, Username, SLUserID, SLItemID, ItemID, ItemName
FROM Item
INNER JOIN User ON User.UserID = ShoppingList.SLUserID
INNER JOIN Item ON ShoppingList.SLItemID = Item.ItemID;

-- VIEW Statement for User Account information
CREATE VIEW AccountPage AS
SELECT UserID, Username, Password
FROM User

-- VIEW Statement for Recipe Search page, Do we need this one?
CREATE VIEW FindRecipe AS


-- VIEW STATEMENT for All Recipes
CREATE VIEW AllRecipes AS
SELECT RecipeID, Rating, Difficulty, Directions, Duration, Title, IngredientID, Count, Units
FROM Recipe
INNER JOIN Ingredient ON Recipe.RecipeID = Ingredient.RecipeID;

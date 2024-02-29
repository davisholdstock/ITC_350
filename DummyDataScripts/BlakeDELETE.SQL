DELETE FROM ShoppingList WHERE SLUserID = (SELECT User.UserID FROM User WHERE Username = 'Shaggy') AND SLItemID = (SELECT Item.ItemName FROM Item WHERE ItemName = 'Scooby Snacks');

DELETE FROM ShoppingList WHERE SLUserID = (SELECT User.UserID FROM User WHERE Username = 'Shaggy');

DELETE FROM Ingredient WHERE Ingredient.IngredientID = (SELECT Item.ItemID FROM Item WHERE ItemName = 'Scooby Snacks');

DELETE FROM Item WHERE Item.ItemName = 'Scooby Snacks';

DELETE FROM User WHERE User.Username = 'Shaggy';

DELETE FROM User WHERE User.Username = 'scoobydooby';

DELETE FROM Recipe WHERE Recipe.RecipeID = 'Scooby Snack Snack';
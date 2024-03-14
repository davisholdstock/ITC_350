DELETE FROM ShoppingList WHERE SLUserID = (SELECT UserID FROM User WHERE Username = 'Shaggy') AND SLItemID = (SELECT ItemName FROM Item WHERE ItemName = 'Scooby Snacks');

DELETE FROM ShoppingList WHERE SLUserID = (SELECT UserID FROM User WHERE Username = 'Shaggy');

DELETE FROM Ingredient WHERE IngredientID = (SELECT ItemID FROM Item WHERE ItemName = 'Scooby Snacks');

DELETE FROM Item WHERE ItemName = 'Scooby Snacks';

DELETE FROM User WHERE Username = 'Shaggy';

DELETE FROM User WHERE Username = 'scoobydooby';

DELETE FROM Recipe WHERE RecipeID = 'Scooby Snack Snack';
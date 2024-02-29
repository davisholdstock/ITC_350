INSERT INTO Recipe (Rating, Difficulty, Directions, Duration, Title)
VALUES (5.0, 1.0, 'Go ahead and open the box, then eat 16 scooby snacks', 1, 'Scooby Snack Snack');

INSERT INTO User (Username, Password)
VALUES ('scoobydooby', 'doooo123');

INSERT INTO User (Username, Password)
VALUES ('Shaggy', 'feedme');

INSERT INTO Item (ItemName)
VALUES ('Scooby Snacks');

INSERT INTO Ingredient (Count, Units, IRecipeID, IngredientID)
VALUES (16, 'biscuits', 1, 1);

INSERT INTO ShoppingList (SLUserID, SLItemID)
VALUES (1, 1);

DELETE FROM ShoppingList WHERE SLUserID = 1 AND SLItemID = 1;

DELETE FROM Ingredient WHERE Count = 16 AND Units = 'biscuits' AND IRecipeID = 1 AND IngredientID = 1;

DELETE FROM Item WHERE ItemName = 'Scooby Snacks';

DELETE FROM User WHERE User.Username = 'Shaggy';

DELETE FROM User WHERE User.Username = 'scoobydooby';

DELETE FROM Recipe WHERE Recipe.RecipeID = 1;
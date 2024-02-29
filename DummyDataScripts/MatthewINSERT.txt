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
VALUES (1, 2);
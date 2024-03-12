CREATE VIEW myCookbook AS 
SELECT UserID, Username, RecipeID, Title, Rating, Difficulty, Duration 
FROM Cookbook 
INNER JOIN User ON User.UserID = Cookbook.CBUserID 
INNER JOIN Recipe ON Cookbook.CBRecipeID = Recipe.RecipeID;

-- select * from myCookbook;
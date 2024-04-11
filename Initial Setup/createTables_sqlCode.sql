CREATE DATABASE cupboard_cooking;

CREATE TABLE IF NOT EXISTS cupboard_cooking.Recipe
(
  RecipeID INT AUTO_INCREMENT NOT NULL,
  Rating FLOAT,
  Difficulty FLOAT,
  Directions VARCHAR(4500) NOT NULL,
  Duration INT NOT NULL,
  Title VARCHAR(100) NOT NULL,
  Category VARCHAR(30),
  Picture VARCHAR(100),
  PRIMARY KEY (RecipeID)
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.User
(
  UserID INT AUTO_INCREMENT NOT NULL,
  Username VARCHAR(30) UNIQUE NOT NULL,
  Password VARCHAR(30) NOT NULL,
  PRIMARY KEY (UserID)
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.Friendship
(
  PUserID INT NOT NULL,
  FUserID INT NOT NULL,
  PRIMARY KEY (PUserID, FUserID),
  FOREIGN KEY (PUserID) REFERENCES User(UserID) ON DELETE CASCADE,
  FOREIGN KEY (FUserID) REFERENCES User(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.Item
(
  ItemID INT AUTO_INCREMENT NOT NULL,
  ItemName VARCHAR(30) UNIQUE NOT NULL IF NOT EXISTS,
  PRIMARY KEY (ItemID)
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.Cookbook
(
  CBRecipeID INT NOT NULL,
  CBUserID INT NOT NULL,
  PRIMARY KEY (CBRecipeID, CBUserID),
  FOREIGN KEY (CBRecipeID) REFERENCES Recipe(RecipeID) ON DELETE CASCADE,
  FOREIGN KEY (CBUserID) REFERENCES User(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.Ingredient
(
  Count FLOAT NOT NULL,
  Units VARCHAR(10),
  IRecipeID INT NOT NULL,
  I_ItemID INT NOT NULL,
  PRIMARY KEY (IRecipeID, I_ItemID),
  FOREIGN KEY (IRecipeID) REFERENCES Recipe(RecipeID) ON DELETE CASCADE,
  FOREIGN KEY (I_ItemID) REFERENCES Item(ItemID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cupboard_cooking.ShoppingList
(
  SLUserID INT NOT NULL,
  SLItemID INT NOT NULL,
  PRIMARY KEY (SLUserID, SLItemID),
  FOREIGN KEY (SLUserID) REFERENCES User(UserID) ON DELETE CASCADE,
  FOREIGN KEY (SLItemID) REFERENCES Item(ItemID) ON DELETE CASCADE
);

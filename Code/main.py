import os
import re
from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
from dotenv import load_dotenv
# from passlib.hash import sha256_crypt
from functools import wraps


# Load environment variables from .env file
load_dotenv(override=True)

# Initialize the flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")


# ------------------------ BEGIN FUNCTIONS ------------------------ #
# Function to retrieve DB connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        port=os.getenv("DB_PORT")
    )
    return conn

# Get all items from the "items" table of the db
def get_all_items():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    # Query the db
    query = "SELECT * FROM Item"
    cursor.execute(query)
    # Get result and close
    result = cursor.fetchall() # Gets result from query
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return result

def get_user_info():
    conn = get_db_connection()
    cursor = conn.cursor()
    if (session['username'] == "admin_davis@gmail.com"):
        query = "SELECT * FROM User"
        cursor.execute(query)
    else:
        query = "SELECT * FROM User WHERE UserID = %s"
        cursor.execute(query, (session['user_id'],))
    result = cursor.fetchall()
    conn.close()
    return result

# Get all recipes from the "recipes" table of the db
def get_all_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Recipe"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap
# ------------------------ END FUNCTIONS ------------------------ #


# ------------------------ BEGIN ROUTES ------------------------ #
@app.route("/", methods=["GET"])
@is_logged_in
def home():
    items = get_user_info()
    return render_template("index.html", items=items) # Return the page to be rendered

@app.route("/recipeview", methods=["POST"])
@is_logged_in
def recipe():
    data = request.form
    recipe = data["recipe_id"]
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """SELECT * FROM recipe WHERE RecipeID = %s;"""
    cursor.execute(query, (recipe,))
    result = cursor.fetchall()[0]
    conn.close()
    return render_template("recipe_view.html", result=result) # Return the page to be rendered

@app.route("/mycookbook", methods=["GET"])
@is_logged_in
def my_cookbook():
    return render_template("myCookbook.html") # Return the page to be rendered

@app.route("/findrecipe", methods=["GET"])
@is_logged_in
def find_recipe():
    return render_template("findRecipe.html") # Return the page to be rendered

@app.route("/findsomerecipes", methods=["GET"])
@is_logged_in
def get_some_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = request.args
    include = data["Ingredients"]
    category = data["category"]
    ingredients = include.strip().split(",")
    print(include)
    print(category)
   
    item_names = tuple(ingredients)
    # Generate the placeholders for the IN clause
    placeholders = ', '.join(['%s'] * len(item_names))
    # Query to retrieve RecipeIDs from the FindRecipe view
    query = """
        SELECT * FROM recipe WHERE RecipeID IN
        (SELECT DISTINCT RecipeID
        FROM FindRecipe
        WHERE ItemName IN ({})
        GROUP BY RecipeID
        HAVING COUNT(DISTINCT ItemName) = %s);
    """.format(placeholders)
    # Count of ingredients to match
    ingredient_count = len(item_names)
    # Execute the query
    cursor.execute(query, item_names + (ingredient_count,))

    result = cursor.fetchall()
    recipelist = []
    for recipe in result:
        if recipe[6] == category:
            recipelist.append(recipe)
    conn.close()
    return render_template("recipes.html", recipes=recipelist)

@app.route("/recipes", methods=["GET"])
def recipes():
    recipes = get_all_recipes()
    return render_template("recipes.html", recipes=recipes)

@app.route("/addrecipe", methods=["GET"])
@is_logged_in
def add_recipe():
    return render_template("addRecipe.html") # Return the page to be rendered

@app.route("/shoppinglist", methods=["GET"])
@is_logged_in
def shopping_list():
    return render_template("shoppingList.html") # Return the page to be rendered

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

# POST a new user
@app.route("/new-user", methods=["POST"])
def add_user():
    try:
        # error = None
        # Get items from the form
        data = request.form
        user_password = data["password2"]
        user_email = data["emailaddress2"]
        confirm_password = data["confirmpassword2"]
        # if password != confirm_password:
        #     # error = 'Passwords do not match'
        #     flash("Passwords do not match", "error")
        # else:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO User (Username, Password) VALUES (%s, %s)"""
        cursor.execute(query, (user_email, user_password))
        conn.commit()
        conn.close
        # Send message to page. There is code in index.html that checks for these messages
        flash("Item added successfully", "success")
        # Redirect to home. This works because the home route is named home in this file
        return redirect(url_for("home"))

    # If an error occurs, this code block will be called
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error") # Send the error message to the web page
        return redirect(url_for("home")) # Redirect to home
    
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        row = request.form
        username = row["email"]
        password_candidate = row["password"]

        # Create cursor
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get user by username
        query = """SELECT * FROM User WHERE Username = %s"""
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        conn.close()
        print(result)

        if result != None:
            # Get stored hash
            password = result[2]

            # Compare Passwords
            if password_candidate == password: # sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username
                session['user_id'] = result[0]

                flash('You are now logged in', 'success')
                return redirect(url_for('home'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            conn.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')
# ------------------------ END ROUTES ------------------------ #


# listen on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # TODO: Students PLEASE remove debug=True when you deploy this for production!!!!!

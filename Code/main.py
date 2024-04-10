import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv


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

# Get all recipes from the "recipes" table of the db
def get_all_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Recipe"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
# ------------------------ END FUNCTIONS ------------------------ #


# ------------------------ BEGIN ROUTES ------------------------ #
# EXAMPLE OF GET REQUEST
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html") # Return the page to be rendered

@app.route("/", methods=["GET"])
def register():
    return render_template("register.html") # Return the page to be rendered

@app.route("/home", methods=["GET"])
def home():
    items = get_all_items() # Call defined function to get all items
    return render_template("index.html", items=items) # Return the page to be rendered

@app.route("/recipes", methods=["GET"])
def recipes():
    recipes = get_all_recipes()
    return render_template("recipes.html", recipes=recipes) # Return the page to be rendered

# EXAMPLE OF POST REQUEST
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
            # TODO: Insert this data into the database
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
# ------------------------ END ROUTES ------------------------ #


# listen on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # TODO: Students PLEASE remove debug=True when you deploy this for production!!!!!

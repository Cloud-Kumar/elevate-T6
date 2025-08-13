# app.py
# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# --- Routes ---

# Route for the home page
@app.route('/')
def index():
    """
    Renders the home page of the portfolio.
    """
    # The render_template function looks for the file in a 'templates' folder
    return render_template('index.html')

# Route for the contact page, handling both GET and POST requests
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Renders the contact page and handles form submission.
    """
    if request.method == 'POST':
        # This block is executed when the user submits the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # --- Form processing logic ---
        # In a real application, you would do something with this data, like:
        # - Send an email
        # - Save it to a database
        # For this example, we'll just print it to the console.
        print(f"Received message from: {name} ({email})")
        print(f"Message: {message}")
        # --- End of form processing logic ---

        # Redirect to a 'thank you' page or back to the contact page
        # For simplicity, we'll just show a success message on the same page
        return render_template('contact.html', success=True)

    # This is executed for a GET request (when the user just visits the page)
    return render_template('contact.html', success=False)

# --- Running the App ---

# This allows you to run the app directly from the command line
if __name__ == '__main__':
    # The debug=True argument allows for live reloading during development
    app.run(debug=True)

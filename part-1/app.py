"""
Part 1: Hello Flask - Your First Web Server
============================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""
from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "<h1>Hello Mayuri!</h1><p>Welcome to my first Flask web server.</p>"

# About route
@app.route('/about')
def about():
    return "This is the about page"

if __name__ == '__main__':
    app.run(debug=True)

# =============================================================================
# EXERCISES - Try these after running the basic app:
# =============================================================================
#
# Exercise 1.1: Change the return message
#   - Modify the return statement to say "Hello [Your Name]!"
#   - Save the file and refresh your browser (server auto-reloads!)
#
# Exercise 1.2: Return HTML instead of plain text
#   - Change the return to: return "<h1>Hello Flask!</h1><p>This is HTML</p>"
#   - Notice how the browser renders it as formatted HTML
#
# Exercise 1.3: Add a second route
#   - Add another function with @app.route('/about')
#   - Return something like "This is the about page"
#   - Visit http://localhost:5000/about in your browser
#
# =============================================================================

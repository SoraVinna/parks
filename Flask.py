from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data placeholders
users = {}
feedbacks = []

# Routes
@app.route('/')
def home():
    # Render homepage HTML
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            # Successful login, redirect to dashboard
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed, redirect to login page with error message
            return render_template('login.html', error="Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Create new user
        username = request.form['username']
        password = request.form['password']
        users[username] = {'password': password}
        # Redirect to login page after successful registration
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Render dashboard HTML
    return render_template('dashboard.html', feedbacks=feedbacks)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Save submitted feedback
    feedback = request.form['feedback']
    feedbacks.append(feedback)
    # Redirect back to dashboard
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

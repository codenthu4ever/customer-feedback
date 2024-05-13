from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variable for storing feedback data
feedback = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_feedback', methods=['POST'])
def start_feedback():
    name = request.form['name']
    feedback_text = request.form['feedback']
    feedback[name] = feedback_text
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)

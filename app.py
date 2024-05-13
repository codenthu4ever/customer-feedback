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
    requirements_met = request.form['requirements_met']
    no_defect = request.form['no_defect']
    satisfaction = request.form['satisfaction']
    improvements = request.form['improvements']
    comments = request.form.get('comments', '')  # Use get() to handle optional field
    
    feedback[name] = {
        'requirements_met': requirements_met,
        'no_defect': no_defect,
        'satisfaction': satisfaction,
        'improvements': improvements,
        'comments': comments
    }
    
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)

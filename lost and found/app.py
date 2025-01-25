from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Capture form data
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'location': request.form['location'],
        'date': request.form['date'],
        'category': request.form['category'],
        'contact': request.form['contact']
    }
    # Render the data in the submit.html template
    return render_template('submit.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

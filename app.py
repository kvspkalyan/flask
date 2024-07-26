from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # Add code here to process the form data
        return "Form submitted successfully!"
    else:
        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
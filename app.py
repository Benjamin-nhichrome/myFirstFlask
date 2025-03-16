from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates/greet.html', methods=['POST'])
def greet():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    name = request.form.get('name')

    return render_template('greet.html', name=name, current_time=current_time, current_date=current_date)


if __name__ == '__main__':
    app.run(debug=True)



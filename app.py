from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_string = request.form['date']
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        day_as_number = date_object.weekday()
        days_of_week_array = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']
        day_of_week = days_of_week_array[day_as_number] 
        return render_template('result.html', day_of_week=day_of_week)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
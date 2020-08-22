import os
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv

app = Flask(__name__)


def save_to_file(data):
    with open('database.txt', mode='a') as db_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db_file.write(f'\n{email}, {subject}, {message}')
    return None


def save_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = csv.writer(csv_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email, subject, message])


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_csv(data)
        return redirect("thankyou.html")
    else:
        return 'something went sideways'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

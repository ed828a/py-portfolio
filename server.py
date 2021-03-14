import os
from flask import Flask, render_template, url_for, request, redirect
import csv  # built-in with Python


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# handle requests from Browser
# # receive either POST or GET


@app.route('/submit_form', methods=['POST', "GET"])
def submit_form():
    # app.add_url_rule('/favicon.ico',
    #              redirect_to=url_for('static', filename='favicon.ico'))

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

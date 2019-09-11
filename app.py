from flask import Flask, request, render_template, redirect
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = EmailMessage()
        msg['From'] = email
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
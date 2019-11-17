from flask import Flask, request, render_template

from workers import send_email

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    reveiver = request.form['receiver']
    subject = 'flcelery'
    body = request.form['mail_body']
    send_email.delay(reveiver, subject, body)
    return 'your mail has been sent'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = f"Message from {name}"
    msg['From'] = email
    msg['To'] = 'codeclinics22@gmail.com'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('codeclinics22@gmail.com', 'gjdo xlxi opua sgrk')
            server.sendmail(email, 'codeclinics22@gmail.com', msg.as_string())
        return "Message sent successfully!"
    except Exception as e:
        return f"Failed to send message: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

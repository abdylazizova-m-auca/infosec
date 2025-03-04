import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_phishing_email(receiver_email):
    sender_email = "pdkfrl@gmail.com" 
    sender_password = "ndjpdrnj"

    subject = "Urgent: Action Required for Your Payment"
    body = """
    <html>
    <head></head>
    <body>
        <h2>Secure Payment Gateway</h2>
        <p>Click the link below to complete your payment:</p>
        <a href="http://localhost:5000">Complete Your Payment</a>
    </body>
    </html>
    """

    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the HTML content
    msg.attach(MIMEText(body, 'html'))

    # Sending the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Example
send_phishing_email("ndjsppqnn@example.com")

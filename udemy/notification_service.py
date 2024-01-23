import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, message):
    # Email configuration
    sender_email = 'gadkarimayuresh97@gmail.com'  # Replace with your email
    sender_password = 'Maya@1997'      # Replace with your email password
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())

    print("Email sent successfully!")

# Example usage
to_email = 'Mayuresh.Gadkari@ril.com'
subject = 'Test Email'
message = 'This is a test email from Python.'

send_email(to_email, subject, message)
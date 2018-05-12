import smtplib
import imaplib


# sends an email
def send_email(recipient, subject, message):
    # Gmail Sign In
    gmail_sender = "sundarlab@gmail.com"
    gmail_password = "password"

    # connect to gmail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_password)

    # create message body
    body = '\r\n'.join(["To: " + recipient,
                        "From: " + gmail_sender,
                        "Subject: " + subject,
                        "", message])

    try:
        server.sendmail(gmail_sender, [recipient], body)  # sends the email
        #log("  [LOG] message sent to " + recipient)
    except Exception as e:
        log("  [ERROR] could not send message to " + recipient + ": " + str(e))

    server.quit()
    return 1

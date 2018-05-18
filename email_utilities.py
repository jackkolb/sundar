import smtplib
import logs


# sends an email
def send_email(recipient, subject, message):
    # Gmail Sign In
    gmail_sender = "sundarlabucr@gmail.com"
    gmail_password = "Motor1234"

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
        logs.log("  [LOG] message sent to " + recipient)
    except Exception as e:
        logs.log("  [ERROR] could not send message to " + recipient + ": " + str(e))

    server.quit()
    return 1

import smtplib
def     SendMail():
    port=587
    smtp_server="smtp.gmail.com"
    sender_email=input("Enter the sender's gmail.id")
    password=input("Type your password and peess enter:")
    receiver_email=input("Enter the receiver's mail id")
    subject="Notification about the status of Refrigerator"
    message="Your refrigerator door is not closed properly close it to reduce power consumption"
    header="From:%s\n %sender_email"
    header+="To:%s\n %receiver_email"
    header+="subject: %s\n %subject"
    message=message+header
    server=smtplib.SMTP(smtp_server,port)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
SendMail()
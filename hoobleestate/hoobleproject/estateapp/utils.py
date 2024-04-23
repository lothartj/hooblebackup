import os
import imghdr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_email(receiver_email, subject, body, file_paths):
    sender_name = "LotharsApp.com"
    sender_email = "streamlitt@gmail.com"  # Update with your email address
    sender_password = "qias amqt donl wvgk"  # Update with your email password
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    for file_path in file_paths:
        file_type_info = imghdr.what(file_path) if os.path.isfile(file_path) else (None, None)
        file_type = file_type_info[0] if file_type_info else None

        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(file_path)}",
        )
        if file_type:
            part.add_header("Content-Type", f"image/{file_type}")

        msg.attach(part)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

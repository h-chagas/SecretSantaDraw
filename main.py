import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Email content
sender_email = '' ################# Replace with your email address
password = ''  ################### Replace with your email password (if gmail, you should create Apps password - Check README.md file)

# List of Secret Santa participants with their names and emails
participants = [
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'},
    {'name': 'Maria', 'email': 'maria@gmail.com'}
]

# Shuffle the list to randomize participant order
random.shuffle(participants)

# Ensure no participant gets their own name
for i, participant in enumerate(participants):
    # Get the next participant in the list, ensuring the last one doesn't draw themselves
    next_index = (i + 1) % len(participants)
    # Assign the drawn person to the current participant
    participant['drawn_name'] = participants[next_index]['name']

# Email body
subject = 'Secret Santa 2023'

# Establishing a connection with the SMTP server (Gmail in this case)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

# Sending individual emails to each participant with their assigned person
for participant in participants:
    receiver_name = participant['name']
    receiver_email = participant['email']
    drawn_person = participant['drawn_name']
    
    body = f'Hi {receiver_name},\n You are invited to participate in Secret Santa 2023! \n\n Your secret santa is: ** {drawn_person.upper()} **. \n\n The budget of the gift exchange is from £ 25. Here is the wishlist: https://docs.google.com/document/blablabla/edit. \n Please, add your suggestions in the wish list. \n\n\n Enjoy and see you there! \n Merry Christmas!!! \n 🤖hccBot' 

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    # Sending the email
    server.sendmail(sender_email, receiver_email, message.as_string())

# Quitting the server
server.quit()

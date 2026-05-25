from mailerpy import Mailer
my_mailer=Mailer("smtp.gmail.com", 587, "snehayadav1109@gmail.com", "gmll jouo yewu jdsm")
to_emails=['snyadav939@gmail.com', 'sahpreeti206@gmail.com']
subject="test email from mailerpy"
body="Hello I am Sneha Yadav, from Kathmandu.This is a test email from mailerpy."
my_mailer.send_mail(to_emails, subject, body)
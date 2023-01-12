import random
import smtplib
import datetime as dt


def send_quote(quote, author):
    email_sender = "stingzld.test.email@gmail.com"
    email_recipient = "stingzld.other.test.email@gmail.com"
    password = "aaeddmspdtbyixxw"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs=email_recipient,
                            msg="Subject:Monday Motivational Quote\n\n"
                                f"{quote}\n{author}")


def select_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
    random_quote = random.choice(quotes).split('"')
    quote = random_quote[1]
    author = random_quote[2]
    return quote, author


# If today is Monday, send a random motivational quote
now = dt.datetime.now()
if now.weekday() == 0:
    quote, author = select_quote()
    send_quote(quote, author)

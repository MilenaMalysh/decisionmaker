import yagmail


def send_invitation(invitation):
    print(yagmail.SMTP('zenclosure').send("esquilo1994@gmail.com", "Hello world!", "Hello World!"))

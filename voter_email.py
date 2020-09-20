import yagmail

def email_update(f, last, email, status):
    status = status.upper()
    if (status.lower() == "inactive"):
        body = f"""{f} {last},\n
        We've noticed that your voter registration status has recently changed to INACTIVE.\n
        You can visit Vote.org to reregister. Your vote matters!""".format(f, last)

    elif (status.lower() == "active"):
        body = f"""{f} {last},\n
        Congratulations! Your voter registration status has successfully been changed to ACTIVE.\n
        You can visit Vote.org to find your polling location!""".format(f, last)

    elif (status.lower() == "invalid"):
        body = f"""{f} {last},\n
        We've noticed that you are not registered to vote. 
        You can visit Vote.org to register and find your polling location. Your vote matters!""".format(f, last)

    else:
        body = f"""{f} {last},\n
        An error seems to have occurred within our system. 
        Please try signing up again and double checking your credentials.""".format(f, last)
        
    yag = yagmail.SMTP("hackmit2020votecheck@gmail.com", oauth2_file="~/oauth2_creds.json")
    yag.send(
        to=email,
        subject="VOTER REGISTRATION CHANGE",
        contents=body,
    )
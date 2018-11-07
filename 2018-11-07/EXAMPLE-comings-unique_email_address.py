def numUniqueEmails(self, emails):
    a = {}
    for email in emails:
        new_email = email
        email_to_add = ''
        for letter in email:
            if letter == ".":
                new_email = new_email[1:]
            elif letter == "@":
                break
            else:
                email_to_add += (new_email[0])
                new_email = new_email[1:]
        a[new_email] = email_to_add
    return len(a)

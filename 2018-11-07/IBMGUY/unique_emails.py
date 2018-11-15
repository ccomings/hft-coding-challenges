def split_local_domain(email):
    split_email = email.split('@')
    return {'local': split_email[0], 'domain': split_email[1]}

def sanitize_dots(email):
    split_email = split_local_domain(email)
    sanitized = split_email['local'].replace('.', '')
    return "{}@{}".format(sanitized, split_email['domain'])

def sanitize_plus(email):
    split_email = split_local_domain(email)
    sanitized = split_email['local'].split('+')[0]
    return "{}@{}".format(sanitized, split_email['domain'])

def num_unique_emails(emails):
    unique_emails = set()
    for email in emails:
        sanitized_email = sanitize_plus(sanitize_dots(email))
        if sanitized_email not in unique_emails:
            unique_emails.add(sanitized_email)

    return len(unique_emails)

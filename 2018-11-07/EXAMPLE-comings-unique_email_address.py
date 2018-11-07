def numUniqueEmails(self, emails):
    seen = set()
    for email in emails:
        local, _, domain = email.partition('@')
        if '+' in local:
            local = local[:local.index('+')]
        seen.add(local.replace('.','') + '@' + domain)
    return len(seen)

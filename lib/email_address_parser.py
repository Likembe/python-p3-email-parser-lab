import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email_addresses = re.findall(email_pattern, self.email_string)
        email_addresses.sort()

        return email_addresses
    

# Example usage:
email_string = "Please contact support@example.com or sales@company.com for assistance."
parser = EmailAddressParser(email_string)
parsed_emails = parser.parse()
print(parsed_emails)
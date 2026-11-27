
import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(pattern, text)

    return emails


# Sample text
text = """
Contact us at abc@gmail.com
or xyz@yahoo.com.
Invalid email: abc@com
Another email: student123@mit.edu
"""

# Find email addresses
result = find_emails(text)

print("Email Addresses Found:")

for email in result:
    print(email)

print("Total Emails:", len(result))

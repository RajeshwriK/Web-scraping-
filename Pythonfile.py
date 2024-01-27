import requests
import re

def extract_data(url):
    # Make a request to the specified URL
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    # Extract phone numbers using a regular expression
    phone_numbers = re.findall(r'\b(?:\+91|0)?[6-9][0-9]{9}\b', response.text)

    # Extract email addresses using a regular expression
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Z|a-z]{2,}\b', response.text)

    # Filter valid phone numbers (not landline or toll-free)
    valid_phone_numbers = [number for number in phone_numbers if is_valid_mobile_number(number)]

    # Filter valid email addresses ending with '.com' or '.in'
    valid_email_addresses = [email for email in email_addresses if email.endswith(('.com', '.in'))]

    # Display the results
 
    print("Valid Mobile Numbers:")
    unique_numbers = [item for index, item in enumerate(valid_phone_numbers) if item not in valid_phone_numbers[:index]]
    
    print(unique_numbers)
    #print(valid_phone_numbers)

    print("\nValid Email Addresses:")
    unique_emails = [item for index, item in enumerate(valid_email_addresses) if item not in valid_email_addresses[:index]]
    print(unique_emails)
    #print(valid_email_addresses)

def is_valid_mobile_number(number):
    # Add more sophisticated validation logic if needed
    return True

# Take user input for the URL
url = input("Enter the URL: ")
extract_data(url)

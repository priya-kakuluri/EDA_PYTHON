# test.py

# Store credentials
credentials = {
    "vishnupriya@gmail.com": "your_secure_password"
}

# Function to get password for a given email
def get_password(email):
    return credentials.get(email, None)

# Retrieve password
my_password = get_password("vishnupriya@gmail.com")

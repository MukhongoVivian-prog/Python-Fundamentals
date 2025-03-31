""""'
We are building a simple authentication system that allows  you to authenticate with Google
***steps***
1. Import the google-auth library
2. Create a client for Google OAuth2
3. Request a user's access token
4. Validate the access token
5. Get user information

Note: You'll need to replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your own client ID and client secret from Google Cloud Console


"""
known_username="Vivian"
known_password="pass1234567"

username = input("Enter your username: ")
password = input("Enter your password: ")

# print("Username is: ", username)
# print("Password is: ", password)

if username == "vivian" and password == "pass1234567":
    print("Hello,Vivian")

elif username == "Fatma":
    print("Hello, Fatma")

else:
    print("Username not found")
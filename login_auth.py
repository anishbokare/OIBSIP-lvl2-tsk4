import hashlib

user_data = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_data:
        return "Username already exists. Please choose a different username."
    
    hashed_password = hash_password(password)
    user_data[username] = hashed_password
    return "Registration successful!"

def login(username, password):
    if username not in user_data:
        return "Username does not exist."
    
    hashed_password = hash_password(password)
    if user_data[username] == hashed_password:
        return "Login successful!"
    else:
        return "Incorrect password."

def secured_page():
    return "Welcome to the secured page!"

def main():
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            print(register(username, password))
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_result = login(username, password)
            print(login_result)
            if login_result == "Login successful!":
                print(secured_page())
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

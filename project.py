import hashlib

users = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def check_password_strength(password):
    strength = 0 

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_+=" for char in password):
        strength += 1

    if strength == 4:
        return "Strong Password"
    elif strength == 3:
        return "Moderate Password"      
    else:
        return "Weak Password"
    
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Password Strength:", check_password_strength(password))
    users[username] = hash_password(password)
    print(" User Registration successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    if username in users and users[username] == hashed_password:
        print("Login successful!\n")
    else:
        print("Invalid username or password.\n")

while True:
    print("1.Register")
    print("2.Login")
    print("3.Check Password Strength")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        password = input("Enter password to check strength: ")
        print("Password Strength:", check_password_strength(password), "\n")
    elif choice == "4":
        break
    else:

        print("Invalid choice. Please try again.\n")

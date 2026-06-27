print("FarSayBondBridge")

# Set the owner's personal login details here
OWNER_USERNAME = "kolkar nisha"
OWNER_PASSWORD = "njz"


def user_login():
    print("Welcome to Event Management System")
    print("Please login to continue")

    for attempt in range(3):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username == OWNER_USERNAME and password == OWNER_PASSWORD:
            print("Login successful!")
            return True

        print("Invalid username or password. Try again.")

    print("Too many failed attempts. Access denied.")
    return False


if __name__ == "__main__":
    user_login()


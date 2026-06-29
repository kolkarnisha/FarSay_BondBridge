print("FarSayBondBridge")

# Set the owner's personal login details here
OWNER_USERNAME = "kolkar nisha"
OWNER_PASSWORD = "njz"

# Dictionary to store user credentials
users = {}

# Occasion details with price ranges and facilities
occasions = {
    "Birthday": {
        "min_price": 5000,
        "max_price": 20000,
        "facilities": {
            "5000": "Basic decoration, cake, and music",
            "10000": "Decoration, cake, DJ, photography",
            "20000": "Luxury venue, catering, DJ, photography, themed decor"
        }
    },
    "Wedding": {
        "min_price": 50000,
        "max_price": 500000,
        "facilities": {
            "50000": "Simple ceremony setup, basic catering",
            "200000": "Venue, catering, photography, decoration",
            "500000": "Luxury venue, premium catering, photography, videography, live music"
        }
    },
    "Anniversary": {
        "min_price": 10000,
        "max_price": 100000,
        "facilities": {
            "10000": "Dinner setup, flowers, cake",
            "50000": "Venue, catering, decoration, photography",
            "100000": "Luxury venue, premium catering, live music, themed decor"
        }
    },
    "Graduation": {
        "min_price": 8000,
        "max_price": 50000,
        "facilities": {
            "8000": "Basic hall setup, snacks, photography",
            "20000": "Venue, catering, DJ, photography",
            "50000": "Premium venue, catering, DJ, photography, decor"
        }
    }
}


def register_user():
    print("=== User Registration ===")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try another.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print(f"User '{username}' registered successfully!\n")


def login_user():
    print("=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == OWNER_USERNAME and password == OWNER_PASSWORD:
        print("Owner login successful!")
        print("Owner access does not include event planning details.\n")
        return

    if username in users and users[username] == password:
        print(f"Welcome back, {username}! You are logged in to farsaybondbridge.\n")
        occasion_planner()
    else:
        print("Invalid username or password. Please try again.\n")


def occasion_planner():
    print("=== Occasion Planner ===")
    options = list(occasions.keys())
    print("Available occasions:")
    for index, occasion in enumerate(options, start=1):
        print(f"{index}. {occasion}")

    choice = input("Select an occasion by number or name: ").strip()
    selected_occasion = None

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(options):
            selected_occasion = options[index]
    else:
        lowered = choice.lower()
        for occasion in options:
            if occasion.lower() == lowered:
                selected_occasion = occasion
                break

    if selected_occasion is None:
        print("Invalid occasion selected.\n")
        return

    details = occasions[selected_occasion]
    print(f"\n{selected_occasion} celebration price range: {details['min_price']} - {details['max_price']} INR")

    try:
        budget = int(input("Enter your budget: "))
    except ValueError:
        print("Invalid budget. Please enter a number.\n")
        return

    closest = min(details["facilities"].keys(), key=lambda x: abs(int(x) - budget))
    print(f"\nBased on your budget ({budget} INR), we recommend:")
    print(details["facilities"][closest])
    print("\nFor enquiries, call or message us at: [9876543210](tel:9876543210)")


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()



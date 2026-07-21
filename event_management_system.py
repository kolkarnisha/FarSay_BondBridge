from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

print("FarSayBondBridge")

# Load environment variables from .env file
load_dotenv()

# MongoDB Connection - Load from environment variables
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER = os.getenv("MONGODB_CLUSTER")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Owner credentials - Load from environment variables
OWNER_USERNAME = os.getenv("OWNER_USERNAME")
OWNER_PASSWORD = os.getenv("OWNER_PASSWORD")

# Validate that all required environment variables are set
if not all([MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, DATABASE_NAME]):
    print("✗ Error: Missing MongoDB configuration in .env file")
    print("Please ensure MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, and DATABASE_NAME are set")
    exit(1)

# MongoDB Connection String
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/{DATABASE_NAME}?retryWrites=true&w=majority"

# Initialize MongoDB client
try:
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    users_collection = db["users"]
    events_collection = db["events"]
    print("✓ Connected to MongoDB successfully!")
except Exception as e:
    print(f"✗ MongoDB connection failed: {e}")
    db = None
    users_collection = None
    events_collection = None

# Fallback dictionary to store user credentials if DB fails
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
    
    # Check if user exists in MongoDB
    if users_collection and users_collection.find_one({"username": username}):
        print("Username already exists. Try another.")
        return
    
    # Fallback check for in-memory storage
    if username in users:
        print("Username already exists. Try another.")
        return
    
    password = input("Enter a password: ")
    
    # Store in MongoDB
    if users_collection:
        try:
            user_data = {
                "username": username,
                "password": password,
                "created_at": datetime.now()
            }
            users_collection.insert_one(user_data)
            print(f"User '{username}' registered successfully in database!\n")
        except Exception as e:
            print(f"Database error: {e}")
            users[username] = password
            print(f"User '{username}' registered locally!\n")
    else:
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

    # Check MongoDB first
    user_valid = False
    if users_collection:
        try:
            user = users_collection.find_one({"username": username, "password": password})
            if user:
                user_valid = True
        except Exception as e:
            print(f"Database query error: {e}")
    
    # Fallback to in-memory storage
    if not user_valid and username in users and users[username] == password:
        user_valid = True

    if user_valid:
        print(f"Welcome back, {username}! You are logged in to farsaybondbridge.\n")
        occasion_planner(username)
    else:
        print("Invalid username or password. Please try again.\n")


def occasion_planner(username):
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
    print("\nFor enquiries, call or message us at: [8688581098](tel:8688581098)")
    
    # Save event booking to MongoDB
    if events_collection:
        try:
            event_data = {
                "username": username,
                "occasion": selected_occasion,
                "budget": budget,
                "recommended_package": details["facilities"][closest],
                "created_at": datetime.now()
            }
            events_collection.insert_one(event_data)
            print("✓ Event booking saved to database!")
        except Exception as e:
            print(f"Could not save event to database: {e}")


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



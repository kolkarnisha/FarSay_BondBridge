"""
MongoDB Connection Test Script
Run this to verify your MongoDB Atlas connection is working properly
"""

from pymongo import MongoClient
from datetime import datetime

# Your MongoDB credentials
MONGODB_USERNAME = "neeshakolkar_db_user"
MONGODB_PASSWORD = "K9vpkBlYe9fzaVsw"
MONGODB_CLUSTER = "cluster0.mongodb.net"  # Update this with your actual cluster address
DATABASE_NAME = "farsay_bondbridge"

# Connection string
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/{DATABASE_NAME}?retryWrites=true&w=majority"

print("=" * 60)
print("MongoDB Connection Test")
print("=" * 60)
print()

# Test 1: Connection
print("Test 1: Attempting to connect to MongoDB Atlas...")
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Force connection
    client.server_info()
    print("✓ Connection successful!")
except Exception as e:
    print(f"✗ Connection failed: {e}")
    print("\nTroubleshooting tips:")
    print("1. Check your internet connection")
    print("2. Update MONGODB_CLUSTER with your actual cluster URL")
    print("3. Verify your username and password are correct")
    print("4. Make sure your IP is whitelisted in MongoDB Atlas Network Access")
    exit(1)

print()

# Test 2: Database access
print("Test 2: Accessing database...")
try:
    db = client[DATABASE_NAME]
    print(f"✓ Database '{DATABASE_NAME}' accessed successfully!")
except Exception as e:
    print(f"✗ Database access failed: {e}")
    exit(1)

print()

# Test 3: Collection operations
print("Test 3: Testing collection operations...")
try:
    test_collection = db["test_collection"]
    
    # Insert a test document
    test_doc = {
        "test": "connection",
        "timestamp": datetime.now(),
        "message": "This is a test document"
    }
    result = test_collection.insert_one(test_doc)
    print(f"✓ Test document inserted with ID: {result.inserted_id}")
    
    # Read the document back
    found_doc = test_collection.find_one({"_id": result.inserted_id})
    if found_doc:
        print("✓ Test document retrieved successfully!")
    
    # Delete the test document
    test_collection.delete_one({"_id": result.inserted_id})
    print("✓ Test document deleted successfully!")
    
except Exception as e:
    print(f"✗ Collection operations failed: {e}")
    exit(1)

print()

# Test 4: List existing collections
print("Test 4: Listing existing collections...")
try:
    collections = db.list_collection_names()
    if collections:
        print(f"✓ Found {len(collections)} collection(s):")
        for col in collections:
            count = db[col].count_documents({})
            print(f"   - {col}: {count} document(s)")
    else:
        print("ℹ No collections exist yet (this is normal for a new database)")
except Exception as e:
    print(f"✗ Failed to list collections: {e}")

print()
print("=" * 60)
print("All tests completed successfully!")
print("Your MongoDB connection is ready to use.")
print("=" * 60)
print()
print("Next steps:")
print("1. Update MONGODB_CLUSTER in event_management_system.py")
print("2. Run: python event_management_system.py")

# MongoDB Setup Instructions for FarSay BondBridge

## Prerequisites
1. Python 3.x installed
2. MongoDB Atlas account (free tier available)

## Step 1: Install Required Package
Run this command in your terminal:
```bash
pip install pymongo
```

## Step 2: Set Up MongoDB Atlas

### Create a MongoDB Atlas Account
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up for a free account or log in

### Create a Cluster
1. Click "Build a Cluster" or "Create New Cluster"
2. Choose the free tier (M0 Sandbox)
3. Select your preferred cloud provider and region
4. Click "Create Cluster" (this may take a few minutes)

### Create Database User
Your credentials are already set up in the code:
- **Username**: neeshakolkar_db_user
- **Password**: K9vpkBlYe9fzaVsw

To add this user in MongoDB Atlas:
1. Go to "Database Access" in the left sidebar
2. Click "Add New Database User"
3. Choose "Password" authentication
4. Enter username: `neeshakolkar_db_user`
5. Enter password: `K9vpkBlYe9fzaVsw`
6. Set privileges to "Atlas Admin" or "Read and write to any database"
7. Click "Add User"

### Configure Network Access
1. Go to "Network Access" in the left sidebar
2. Click "Add IP Address"
3. Click "Allow Access from Anywhere" (for development)
   - This adds `0.0.0.0/0` to the whitelist
4. Click "Confirm"

### Get Your Connection String
1. Go back to "Clusters" and click "Connect" on your cluster
2. Choose "Connect your application"
3. Select "Python" as the driver and version 3.12 or later
4. Copy the connection string (it looks like this):
   ```
   mongodb+srv://neeshakolkar_db_user:<password>@cluster0.xxxxx.mongodb.net/
   ```
5. Note the cluster address (the part like `cluster0.xxxxx.mongodb.net`)

## Step 3: Update Configuration
Open `event_management_system.py` and update the `MONGODB_CLUSTER` variable on line 10:

```python
MONGODB_CLUSTER = "cluster0.xxxxx.mongodb.net"  # Replace with your actual cluster address
```

Replace `cluster0.mongodb.net` with your actual cluster URL from the connection string.

## Step 4: Run Your Application
```bash
python event_management_system.py
```

If the connection is successful, you'll see:
```
✓ Connected to MongoDB successfully!
```

## Database Structure

### Collections Created:
1. **users** - Stores registered user accounts
   - username
   - password
   - created_at

2. **events** - Stores event bookings
   - username
   - occasion (Birthday, Wedding, Anniversary, Graduation)
   - budget
   - recommended_package
   - created_at

## Features
- User registration stored in MongoDB
- User authentication against MongoDB
- Event bookings saved to database
- Fallback to in-memory storage if database connection fails

## Troubleshooting

### Connection Error
If you see "MongoDB connection failed":
1. Check your internet connection
2. Verify the cluster address is correct
3. Ensure your IP is whitelisted in Network Access
4. Confirm the database user credentials are correct

### Authentication Error
If authentication fails:
1. Verify the username and password in Database Access
2. Make sure the user has proper permissions
3. Check that you're using the correct password (not `<password>` placeholder)

## Security Notes
⚠️ **Important**: For production use:
1. Use environment variables for credentials instead of hardcoding them
2. Restrict network access to specific IP addresses
3. Use stronger passwords
4. Enable additional MongoDB security features

## Support
For issues or questions, contact: 8688581098

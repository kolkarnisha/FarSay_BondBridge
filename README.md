# FarSay_BondBridge
A full-stack Event Management System that connects organizers and attendees. Create, manage, and book events with real-time updates, ticketing, and user dashboards. Built to bridge the gap between planning and participation.

## Features
- User registration and authentication with MongoDB
- Event planning for Birthdays, Weddings, Anniversaries, and Graduations
- Budget-based package recommendations
- Real-time database storage for users and event bookings
- Owner dashboard access

## Technologies
- **Backend**: Python
- **Database**: MongoDB Atlas (Cloud Database)
- **Frontend**: HTML, CSS

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up MongoDB
Follow the detailed instructions in [MONGODB_SETUP.md](MONGODB_SETUP.md) to:
- Create a MongoDB Atlas account (free)
- Set up your cluster
- Configure database user and network access
- Get your connection string

### 3. Configure Database Connection
Update the `MONGODB_CLUSTER` variable in `event_management_system.py` with your actual cluster URL from MongoDB Atlas.

### 4. Test Connection
```bash
python test_mongodb_connection.py
```

### 5. Run the Application
```bash
python event_management_system.py
```

## Database Structure
- **users** collection: Stores user credentials and registration info
- **events** collection: Stores event bookings with occasion, budget, and recommendations

## Contact
For enquiries: 8688581098

## Security Note
For production deployment, use environment variables for sensitive credentials instead of hardcoding them.

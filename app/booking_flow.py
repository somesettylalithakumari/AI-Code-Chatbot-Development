import re

FIELDS = ["name", "email", "phone", "booking_type", "date", "time"]

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def next_missing_field(state):
    """
    Returns the next missing field from booking state.
    """
    for field in FIELDS:
        if not state.get(field):
            return field
    return None

def summarize_booking(state):
    """
    Returns a summary of the booking for user confirmation.
    """
    return f"""
### 📋 Booking Summary

- **Name:** {state['name']}
- **Email:** {state['email']}
- **Phone:** {state['phone']}
- **Service:** {state['booking_type']}
- **Date:** {state['date']}
- **Time:** {state['time']}

✅ Please confirm by typing **YES** or **NO**.
"""

from datetime import datetime

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Booking:
    def __init__(self, customer_id, booking_type, date, time, status="CONFIRMED"):
        self.customer_id = customer_id
        self.booking_type = booking_type
        self.date = date
        self.time = time
        self.status = status
        self.created_at = datetime.utcnow()
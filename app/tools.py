from db.database import get_connection
import smtplib
from email.mime.text import MIMEText

# ---------- Booking Persistence Tool ----------
def save_booking(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO customers (name,email,phone) VALUES (?,?,?)",
                (data['name'], data['email'], data['phone']))
    customer_id = cur.lastrowid

    cur.execute("""
        INSERT INTO bookings (customer_id, booking_type, date, time, status)
        VALUES (?,?,?,?,?)
    """, (customer_id, data['booking_type'], data['date'], data['time'], "CONFIRMED"))

    booking_id = cur.lastrowid
    conn.commit()
    conn.close()
    return booking_id

# ---------- Email Tool ----------
def send_email(to_email, subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "your_email@gmail.com"
        msg['To'] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "APP_PASSWORD")
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        return False
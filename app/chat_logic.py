from app.booking_flow import next_missing_field, summarize_booking
from app.tools import save_booking, send_email
from app.rag_pipeline import rag_answer
from app.config import EMAIL_SUBJECT

def handle_chat(user_input, state):
    user_input_lower = user_input.lower()

    # ---------- 1. Detect booking intent ----------
    if any(word in user_input_lower for word in ["book", "appointment", "schedule", "reserve"]):
        state["intent"] = "booking"

    # ---------- 2. Booking flow ----------
    if state.get("intent") == "booking":

        # If waiting for confirmation
        if state.get("awaiting_confirmation"):
            if user_input_lower in ["yes", "y", "confirm"]:
                booking_id = save_booking(state)

                email_body = f"""
Hello {state['name']},

Your booking is confirmed!

Booking ID: {booking_id}
Service: {state['booking_type']}
Date: {state['date']}
Time: {state['time']}

Thank you!
"""
                email_sent = send_email(
                    state["email"],
                    EMAIL_SUBJECT,
                    email_body
                )

                # Clear booking state after saving
                state.clear()
                return (
                    f"✅ Booking confirmed!\n\n"
                    f"🆔 Booking ID: {booking_id}\n"
                    + ("📧 Confirmation email sent." if email_sent else "⚠️ Email failed, but booking saved.")
                )
            else:
                state.clear()
                return "❌ Booking cancelled. You can start a new booking anytime."

        # ---------- 3. Slot filling ----------
        missing_field = next_missing_field(state)
        if missing_field:
            # Only set the field if it hasn't been filled yet
            if not state.get(missing_field):
                state[missing_field] = user_input

            next_field = next_missing_field(state)
            if next_field:
                return f"Please provide your **{next_field.replace('_', ' ')}**."
            else:
                # All fields collected, ask confirmation
                state["awaiting_confirmation"] = True
                return summarize_booking(state)

    # ---------- 4. RAG fallback ----------
    return rag_answer(user_input)

import streamlit as st
import sqlite3


def admin_ui():
    st.subheader("Admin Dashboard")

    password = st.text_input("Admin Password", type="password")
    if password != "admin123":
        st.warning("Unauthorized")
        return

    conn = sqlite3.connect("bookings.db")
    df = conn.execute("SELECT * FROM bookings").fetchall()
    st.dataframe(df)
    conn.close()
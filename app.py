import streamlit as st
import time
import pandas as pd
from datetime import datetime
from playsound import playsound
import os

CSV_FILE = "violations.csv"

if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["Vehicle Number", "Time of Violation"]).to_csv(CSV_FILE, index=False)

violations = pd.read_csv(CSV_FILE)

st.title("🚫 Smart No-Parking Violation Detection System")
st.markdown("### Simulate a vehicle entering the No-Parking zone:")

vehicle_number = st.text_input("Enter Vehicle Number:", max_chars=10)

if st.button("🚗 Vehicle Enters No-Parking Zone"):
    if not vehicle_number:
        st.warning("Please enter a vehicle number before starting.")
    else:
        st.info("Vehicle detected in No-Parking Zone. Monitoring...")
        with st.spinner("Checking for 10 seconds..."):
            time.sleep(10)

        # Play alert
        st.audio("alert.mp3", format='audio/mp3')
        st.error("🚨 ALERT: No Parking! Vehicle violation detected.")

        # Log violation
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_row = pd.DataFrame([[vehicle_number, now]], columns=["Vehicle Number", "Time of Violation"])
        new_row.to_csv(CSV_FILE, mode='a', header=False, index=False)

        st.success("✅ Violation Logged & Notified Traffic Control Room")

# Show history
st.markdown("### 🧾 Violation History:")
violations = pd.read_csv(CSV_FILE)
st.dataframe(violations)

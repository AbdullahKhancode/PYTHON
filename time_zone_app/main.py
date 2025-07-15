import streamlit as st 
import time as t
from datetime import datetime
from zoneinfo import ZoneInfo


Time_zone=[
    "UTC",
    "Asia/Karachi",
    "Asia/Tokyo",
    "Asia/Kolkata",
    "Europe/London",
    "Asia/Dubai",
    "Australia/Sydney",
    "America/Los_Angeles",
]


st.title("Time zone application")
selected_timezone= st.multiselect("Select Timezone",Time_zone,default=["UTC","Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone:
    current_time=datetime.now(ZoneInfo(tz)).strftime("%d-/-%m/-%Y,%I %H:%M:%S")
    st.write(f"{tz}:{current_time}")
st.button("Convert time ")
current_time= st.time_input("current time" ,value=datetime.now().time())
from_tz=st.selectbox("Timezone_from",Time_zone,index=0)
to_tz=st.selectbox("Timezone_to",Time_zone,index=1)
if st.button("Convert time"):
    dt=datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    converted_time=dt.astimezone(ZoneInfo(to_tz)).strftime("%d-/-%m/-%Y,%I %H:%M:%S")
    st.success(f"converted time{to_tz}:{converted_time}")
    
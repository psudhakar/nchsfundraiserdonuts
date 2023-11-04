import streamlit as st
from email_validator import validate_email, EmailNotValidError

st.title("NCHS After Prom Fundraiser")
st.markdown("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

quantity = st.selectbox("Select quantity", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=0)

email = st.text_input("Email Address")

if st.button("Submit"):
    try:
        valid = validate_email(email)
        st.success("Form submitted!")
    except EmailNotValidError:
        st.error("Please enter a valid email address")

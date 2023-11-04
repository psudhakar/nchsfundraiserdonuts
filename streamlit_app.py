Python
import streamlit as st

# Set the heading to be centered on the screen
st.title("NCHS After Prom Fundraiser", align="center")

# Add a text field
st.write("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

# Add a dropdown
dropdown_options = [str(i) for i in range(1, 11)]
default_value = "1"
dropdown_value = st.selectbox("Select the number of tickets you want:", dropdown_options, index=dropdown_options.index(default_value))

# Add an email field
email_address = st.text_input("Email Address")

# Validate the email address format before submitting the form
def is_valid_email(email_address):
  import re
  email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
  if re.fullmatch(email_regex, email_address):
    return True
  else:
    return False

# Submit the form
if st.button("Submit"):
  # Check if the email address is valid
  if not is_valid_email(email_address):
    st.error("Please enter a valid email address.")
  else:
    st.submit()

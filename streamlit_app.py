import streamlit as st

# Set the heading
st.header("NCHS After Prom Fundraiser")

# Add a text field
st.write("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

# Add a dropdown menu
options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quantity = st.selectbox("Quantity", options)

# Add a text field for the email address
email_address = st.text_input("Email Address")

# Submit the form
if st.button("Submit"):
    # Send an email with the digital coupon
    # ...
    st.success("Your order has been submitted!")

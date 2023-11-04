import streamlit as st
import smtplib
from email.message import EmailMessage
import re

def send_email(subject, body, to_email):
    # Your email credentials
    sender_email = 'sudhakar.parsi123@gmail.com'  # Update with your email
    sender_password = 'gjjz ulzw oqzp qody'  # Update with your password

    # Create the email message
    message = EmailMessage()
    message['From'] = "sudhakar.parsi@gmail.com"
    message['To'] = to_email
    message['Subject'] = subject
    message.set_content(body)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    return re.match(pattern, email)

st.image("https://drive.google.com/uc?id=1mTbNpv2DyU2zv8xm73wBc1GVH2EJYdqR")

st.title("NCHS After Prom - Krispy Kreme Fundraiser")

# Text field
st.write("Once an order is submitted, digital certificate will be delivered to your email in 24-48 hours. You can redeem the certificate at any Krispy Kreme location in US.", max_chars=200)

form_data = {
    "Name": "",
    "Email": "",
    "Count": "",
    "Comments": ""
}

# Display the form
col1, col2 = st.columns(2)
with col1:
    form_data["Name"] = st.text_input("Name:")
    form_data["Email"] = st.text_input("Email to send krispy kreme certificate:")

with col2:
    form_data["Count"] = st.selectbox("Number of dozens: (Each dozen costs 12$)", list(range(1, 11)), index=0)
    form_data["Comments"] = st.text_input("Comments (Optional):")

# Define the data for the table
payment_data = {
    "Payment Method": ["Zelle", "Venmo", "Cash app"],
    "ID": ["sudhakar.parsi@gmail.com", "sudhakar.pasi@gmail.com", "sudhakar.parsi@gmail.com"]
}

# Submit button
if st.button("Submit"):
    if validate_email(form_data["Email"]):
        # Process form submission here
        st.markdown(':green[Your order submitted. Payment due : ' + str(form_data["Count"]*12) + '$]')
        st.markdown(':blue[Use any payment format below and include the same email address in comments section while making payment !]')
        subject = "KKD Req: " + form_data["Name"] + "-" + form_data["Email"] + ", count : " +  str(form_data["Count"])
        body = "KKD Req: " + form_data["Name"] + "-" + form_data["Email"] + ", count : " +  str(form_data["Count"])
        st.table(payment_data)
        send_email(subject, body, "sudhakar.parsi@gmail.com")
    else:
        st.markdown(':red[Please enter a valid email address!]')





import streamlit as st
import smtplib
from email.message import EmailMessage

#st.image("https://www.teamunify.com/ilbnsc/__eventpic__/590118_nchs%20knight.gif")


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
        
left_co, cent_co,last_co = st.columns(3)
with left_co:
    st.image("https://drive.google.com/uc?id=1kZiBgm5toHSwtYt3HPICjwQPl-ulJK2a")
with cent_co:
    st.image("https://drive.google.com/uc?id=1mTbNpv2DyU2zv8xm73wBc1GVH2EJYdqR")
with last_co:
    st.image("https://drive.google.com/uc?id=1kZiBgm5toHSwtYt3HPICjwQPl-ulJK2a")

st.title("NCHS After Prom - Fundraiser")

# Text field
st.write("Once an order is submitted, the digital certificate will be delivered to your email in 24-48 hours.", max_chars=200)

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
    form_data["Count"] = st.selectbox("Number of dozens (Each dozen costs 12$:)", list(range(1, 11)), index=0)
    form_data["Comments"] = st.text_input("Comments (Optional):")



# Dropdown
#selected_value = st.selectbox("Select number of dozens", list(range(1, 11)), index=0)

# Text field for email
#email = st.text_input("Email Address:  (Your Krispy Creme donut gift cetificate will be emailed to this address.)")

# Submit button
if st.button("Submit"):
    # Process form submission here
    st.write("Submitted " + str(selected_value) + " dozens. Please make your payment at the earliest. Thanks for your support!" )
    send_email("KK Donut Request", "body here", email)

# Define the data for the table
payment_data = {
    "Payment Method": ["Zelle", "Venmo", "Cash app"],
    "ID": ["sudhakar.parsi@gmail.com", "sudhakar.pasi@gmail.com", "sudhakar.parsi@gmail.com"]
}

# Display the table
st.write("Please send your payments as below:")
st.table(payment_data)



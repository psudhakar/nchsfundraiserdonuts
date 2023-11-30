import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Function to send email
def send_email(to_email, data, cc_email="nchsjr.board@gmail.com"):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'nchsjr.board@gmail.com'  # Replace with your email address
    smtp_password = st.secrets["MAIL_APP_PWD"]  # Replace with your email password

    # Email content
    message = MIMEMultipart()
    message['From'] = smtp_user
    message['To'] = to_email
    message['Cc'] = cc_email
    message['Subject'] = 'NCHS After Prom 2023 Trivia Night Registration'

    body = f"Here is the registration data submitted:\n\n{data}"
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(message)
    server.quit()

# Streamlit app layout
#st.set_page_config(page_title='Trivia Night Registration', layout='centered')
logo_url = "https://drive.google.com/uc?id=1mTbNpv2DyU2zv8xm73wBc1GVH2EJYdqR"

# Display the logo
st.image(logo_url)

# Replicate the text and formatting from the screenshot
st.markdown("""
    ## Trivia Night by NCHS After Prom Team
    ###### Saturday, February 3, 2024 - 7 to 9 pm
    ###### Parke Regency, 1413, Lesley Dr, Bloomington - IL
    ###### <span style="background-color:yellow; color:black; ">***Must be 21 or older to attend***</span> 
""", unsafe_allow_html=True)

st.markdown("""
    ### Looking for a fun night out for a good cause?
    Come join us for a night of Trivia while dressing up in your favorite NEON themed outfit (optional)! All proceeds from the Trivia Night help support NCHS After Prom, which is an event organized and supported by Junior Class parents. Students who attend After Prom enjoy games, entertainment, food, and prizes. The event is a safe, alternative event for our students on Prom night.
""")

st.markdown("""
    **Details:**
    - Register your team now! Space is limited.
    - Tables are sold for an 8 person team.
    - Lock in last year's price of $160 per table
    - Break out your NEON and bring your own decorations and snacks (optional).
    - Prizes will be awarded for most creative table, costumes, and high/low scores.
    - There will be a cash bar available.
    - Other highlights include basket raffle and 50/50 raffle.
    - Trivia begins promptly at 7 pm.
""", unsafe_allow_html=True)

st.markdown("""
    **Registration:**
    Reserve your table by filling the form below. Payments can be made by cheeck, or using any payment methods below:
""", unsafe_allow_html=True)
venmourl = "https://venmo.com/u/Jayshri-Patel-5"
recipient_id = 'Jayshri-Patel-5'
cash_app_link = f'https://cash.app/$${recipient_id}'

# Data for the payment options table
payments_data = {
    "Payment Method": ["Venmo", "Zelle/Paypal", "Cash App", "Check"],
    "Instructions": [
        f"To pay with Venmo, click [here]({venmourl}), or send it to Venmo id: Jayshri-Patel-5",
        "For Zelle or Paypal, send your payments to: sudhakar.parsi@gmail.com",
        f"To pay with Cash App, click [here]({cash_app_link}) or send it to Cash id: $SudhakarParsi",
        "Make checks payable to 'NCHS After Prom' and mail to 5018 Londonderry Road, Bloomington, IL - 61705"
    ]
}

# Create DataFrame
df = pd.DataFrame(payments_data)

# Adjust the DataFrame index to start from 1
df.index += 1

# Display the table in Streamlit
st.table(df)


#st.markdown("Click [here](%s), or send it to Venmo id: Jayshri-Patel-5" % venmourl)
#st.markdown("send your payments to: sudhakar.parsi@gmail.com")
#st.markdown(f'Click [here]({cash_app_link}) or send it to Cash id: $SudhakarParsi')
#st.markdown("Make checks payable to 'NCHS After Prom' and mail to 5018 Londonderry Road, Bloomington, IL - 61705")

# Form for registration
with st.form(key='registration_form'):
    st.markdown("#### Team Registration - NCHS After Prom 2024 Trivia Night")
    team_contact = st.text_input("Team Contact:")
    team_name = st.text_input("Team Name:")
    team_contact_email = st.text_input("Email address for Team Contact:")
    team_contact_phone = st.text_input("Phone number for Team Contact:")
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Prepare the data to be sent via email
    data = f"""
    Team Contact: {team_contact}
    Team Name: {team_name}
    Team Contact Email: {team_contact_email}
    Team Contact Phone: {team_contact_phone}
    """
    data += "Use any payment methods below. Please add your name or email address in the comments section of the payment. \n"
    data += "Using Venmo, pay to  : Jayshri-Patel-5 \n"
    data += "Using Zelle/Paypal, pay to  : sudhakar.parsi@gmail.com \n"
    data += "Using Cash, pay to  : $SudhakarParsi \n\n"
    data += "Once the payment is made, you will receive an email with Krispy Kreme gift voucher in next 24-28 hours. \n"
    data += "For any questions, please contact nchsjr.board@gmail.com or call (404)800-3312] \n"
    data += "Make checks payable to 'NCHS After Prom' and mail to 5018 Londonderry Road, Bloomington, IL - 61705"


    
    # Send the email
    send_email(team_contact_email, data)
    st.success("Registration submitted successfully! You will receive a confirmation email shortly.")

# Run this in your terminal: streamlit run your_script.py

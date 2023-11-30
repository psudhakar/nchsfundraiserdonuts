import streamlit as st

st.set_page_config(page_title='NCHS After Prom Trivia Night', layout='wide')

# Heading
st.title('NCHS After Prom 2023 Trivia Night')

# Event details
st.header('Looking for a fun night out for a good cause?')
st.write("""
- **Date**: Saturday, February 4, 2023
- **Time**: 6 - 10 pm
- **Location**: Moose Lodge, 614 IAA Dr, Bloomington
- **Must be 21 or older to attend**
""")

# Registration details
st.subheader('Details:')
st.write("""
- Register your team now! Space is limited.
- Tables are sold for an 8 person team.
- Lock in last year's price of $160 per table if registered by January 14th.
- Registration is $200 per table after the early bird deadline.
- Break out your NEON and bring your own decorations and snacks (optional).
- Prizes will be awarded for most creative table, costumes, and highest score.
- There will be a cash bar available.
- Other highlights include basket raffle and 50/50 raffle.
- Trivia begins promptly at 7 pm.
""")

# Registration form
st.subheader('Team Registration')
with st.form("team_registration_form"):
    team_contact = st.text_input("Team Contact:")
    team_name = st.text_input("Team Name:")
    email = st.text_input("Email address for Team Contact:")
    phone = st.text_input("Phone number for Team Contact:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you for registering. We look forward to seeing you at the event!")

# Instructions for payment
st.write("""
Thank you for supporting NCHS After Prom.

Please complete, detach, and send the form below with payment.
""")

# Additional instructions if needed
# ...

# Run the Streamlit app by saving this script and running `streamlit run your_script.py` in your command line.

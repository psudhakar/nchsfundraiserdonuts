import streamlit as st

st.title("NCHS After Prom Fundraiser")
st.markdown("<h1 style='text-align: center;'>NCHS After Prom Fundraiser</h1>", unsafe_allow_html=True)
st.markdown("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

quantity = st.selectbox("Select quantity", list(range(1, 11)), index=0)

email = st.text_input("Email Address")

st.header("Please send your payments to:")
payment_table = [
    ["Zelle", "sudhakar.parsi@gmail.com"],
    ["Venmo", "lkjdalsd"],
    ["Cash app", "ajdlkada"]
]

st.table(payment_table)

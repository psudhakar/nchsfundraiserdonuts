import streamlit as st

st.title("NCHS After Prom Fundraiser")
st.markdown("<h1 style='text-align: center;'>NCHS After Prom Fundraiser</h1>", unsafe_allow_html=True)
st.markdown("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

quantity = st.selectbox("Select quantity", list(range(1, 11)), index=0)

email = st.text_input("Email Address")

st.subheader("Please send your payments to:")
payment_methods = ["Zelle", "Venmo", "Cash app"]
payment_ids = ["sudhakar.parsi@gmail.com", "lkjdalsd", "ajdlkada"]

payment_details = {
    "Payment Method": payment_methods,
    "ID": payment_ids
}

st.table(payment_details)

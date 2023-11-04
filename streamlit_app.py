import streamlit as st

st.title("NCHS After Prom Fundraiser")
st.markdown("Once an order is submitted, the digital coupon will be delivered in 24-48 hours to your email address given below.")

quantity = st.selectbox("Select quantity", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=0)

email = st.text_input("Email Address")

st.header("Please send your payments to:")

payment_methods = [["Payment Method", "ID"],
                   ["Zelle", "sudhakar.parsi@gmail.com"],
                   ["Venmo", "lkjdalsd"], 
                   ["Cash app", "ajdlkada"]]

st.table(payment_methods)

if st.button("Submit"):
    st.success("Form submitted!")

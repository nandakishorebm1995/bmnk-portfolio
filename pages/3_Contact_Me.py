import streamlit as st
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication


def send_email(message, sender):
    host = "smtp.gmail.com"
    port = 465

    sender_id = sender
    sender_pass = os.getenv("PASSWORD")

    receiver_id = "nandakishorebm1995@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender_id, sender_pass)
        server.sendmail(sender_id, receiver_id, message)


st.set_page_config(layout="wide")

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.text(" ")
st.header("Contact me")

with st.form(key="email_forms"):
    sender_name = st.text_input("Name")
    sender_email = st.text_input("Email address")
    sender_subject = st.text_input("Subject")
    raw_message = st.text_area("Write your message")
    message = f"""\
Subject: {sender_subject}

From: {sender_name} {sender_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, sender_email)
        st.info("Your email was sent successfully!")




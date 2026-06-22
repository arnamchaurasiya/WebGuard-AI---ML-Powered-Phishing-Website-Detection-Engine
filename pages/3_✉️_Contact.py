import streamlit as st
from streamlit_lottie import st_lottie
import requests

contactForm = """
<form action="https://formsubmit.co/your@email.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required style="width:100%;padding:10px;margin:8px 0;border-radius:5px;border:1px solid #ccc;">
    <input type="email" name="email" placeholder="Your Email" required style="width:100%;padding:10px;margin:8px 0;border-radius:5px;border:1px solid #ccc;">
    <textarea name="message" placeholder="Your message here" required style="width:100%;padding:10px;margin:8px 0;border-radius:5px;border:1px solid #ccc;height:120px;"></textarea>
    <button type="submit" style="background:#2ecc71;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">Send Message</button>
</form>
"""

st.set_page_config(page_title="Contact", page_icon="✉️", layout="wide")
st.title("Contact Us 📬")
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "WebGuard AI🛡️";
                margin-left: 15px;
                # margin-top: 20px;
                font-size: 40px;
                font-weight: bold;
                position: relative;
                top: 50px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- LOCAL CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style//style.css")

# --- LOAD LOTTIE FILES ---
def load_lottieurl(url):
    rcontact = requests.get(url)
    if rcontact.status_code != 200:
        return None
    return rcontact.json()

lottie_contact = load_lottieurl("https://lottie.host/829cc1d2-6834-4d26-b419-0ccc5d35663d/eNCKbjiSFQ.json")


# --- CONTACT US FORM ---
contact_form = contactForm

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st_lottie(lottie_contact, height=300, key="phish")
    
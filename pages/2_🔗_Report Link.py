import streamlit as st
from streamlit_lottie import st_lottie
import requests

reportForm = """
<form action="https://formsubmit.co/your@email.com" method="POST">
    <input type="text" name="url" placeholder="Paste phishing URL here" required style="width:100%;padding:10px;margin:8px 0;border-radius:5px;border:1px solid #ccc;">
    <button type="submit" style="background:#e74c3c;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">Report</button>
</form>
"""

# --- PAGE CONFIGURATIONS ---
st.set_page_config(page_title="Report Link", page_icon="🔗", layout="wide")
st.title("Report Phishing Website Link 🎣")
st.header("Join The Cause! 🫱🏻‍🫲🏻")
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
    rphish = requests.get(url)
    if rphish.status_code != 200:
        return None
    return rphish.json()

lottie_phish = load_lottieurl("https://lottie.host/65348f44-4d59-4a58-9905-ea814bf9fd7f/3ahxW4Awp8.json")

# --- REPORT LINK FORM ---
report_form = reportForm

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(report_form, unsafe_allow_html=True)
with right_column:
    st_lottie(lottie_phish, height=300, key="phish")
    
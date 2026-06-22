import streamlit as st
from ml_app_screen import ml_app
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

# --- LOCAL CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main_app():
    st.set_page_config(page_title="PhishGuardian", page_icon="🛡️", layout="wide")
    local_css("style//style.css")
    ml_app()

if __name__ == "__main__":
    main_app()
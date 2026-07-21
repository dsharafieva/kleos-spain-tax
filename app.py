"""
Kleos — Spain contractor taxation landing page (Streamlit prototype wrapper).

Run locally:
    pip install streamlit
    streamlit run app.py

The whole page lives in index.html (self-contained: styling, EN/ES toggle,
calculator logic). This wrapper just renders it full-width with Streamlit's
chrome hidden. index.html also opens directly in a browser or on GitHub Pages
with no changes.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kleos · Hiring a contractor in Spain",
    page_icon="🟠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome so the page renders edge-to-edge.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      .stApp {background: #ffffff;}
      [data-testid="stAppViewBlockContainer"] {padding: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")

# scrolling=True lets the embedded page manage its own full height.
components.html(html, height=6200, scrolling=True)

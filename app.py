"""Penetapan Kadar Thiamin dalam Sampel Tablet Vitamin B1 secara Spektrofotometri UV
Simulasi 3D interaktif Spektrofotometer UV-Vis Double-Beam (Streamlit + Three.js).

Politeknik AKA Bogor · Program Studi D3 Analisis Kimia · 
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulasi 3D Spektrofotometer UV-Vis — Penetapan Thiamin",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hilangkan header, footer, toolbar, dan padding bawaan Streamlit; iframe memenuhi viewport.
st.markdown(
    """
<style>
    header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"], footer, #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }
    .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        overflow: hidden !important;
        background-color: #0e1030 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 99999 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

HTML_PATH = Path(__file__).parent / "index.html"


@st.cache_data(show_spinner=False)
def load_html(path: str, mtime: float) -> str:
    """Baca index.html; cache diperbarui otomatis bila file berubah."""
    return Path(path).read_text(encoding="utf-8")


if not HTML_PATH.exists():
    st.error("File index.html tidak ditemukan. Letakkan index.html satu folder dengan app.py.")
    st.stop()

components.html(load_html(str(HTML_PATH), HTML_PATH.stat().st_mtime), height=900, scrolling=False)

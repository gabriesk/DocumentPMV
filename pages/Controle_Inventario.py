import streamlit as st
import base64
import styles.headers as h
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
import scripts.doc_individual as doc
import time
from io import BytesIO

st.set_page_config(
    page_title="Controle de Inventário",
    page_icon="📊"
)

h.header()
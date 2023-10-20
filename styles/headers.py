import streamlit as st
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval


def header():
    add_logo("images/brasao1.png")
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer  {visibility: hidden;}
                </style>
                """
                
    change_sidebar_color = """
                <style>

                [data-testid="stSidebar"] {
                    background-image: linear-gradient(#2e7bcf, #00b5f4);
                    color: white;
                }
                
                [data-testid="stSidebarNav"] {
                    background-position: 20px 40px;
                }
                                 
                .st-emotion-cache-pkbazv {color: #fff;}
                .st-emotion-cache-17lntkn {color: #dfdfdf}
                
                </style>
                """
                
                
    with open("styles/styles.css") as s:
        st.markdown(f"<styles>{s.read()}</styles>", unsafe_allow_html=True)
                        
    st.markdown(change_sidebar_color, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
#                [data-testid="stSidebarUserContent"] {
#                    background-color: red;
#                } 